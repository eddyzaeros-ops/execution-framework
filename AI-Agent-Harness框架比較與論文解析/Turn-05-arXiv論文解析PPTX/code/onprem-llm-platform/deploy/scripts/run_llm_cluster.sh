#!/usr/bin/env bash
# 多節點 vLLM：每台 GPU 節點執行一次
#   head 節點:   ./run_llm_cluster.sh head
#   worker 節點: ./run_llm_cluster.sh worker
# 全部 worker 加入後，在 head 節點執行: ./run_llm_cluster.sh serve
set -euo pipefail
cd "$(dirname "$0")/.."
source .env

ROLE=${1:?usage: head|worker|serve}
NAME=vllm-node

case "$ROLE" in
  head)
    RAY_CMD="ray start --head --port=6379 --block" ;;
  worker)
    RAY_CMD="ray start --address=${RAY_HEAD_IP}:6379 --block" ;;
  serve)
    docker exec -d "$NAME" bash -c "vllm serve ${LLM_MODEL} \
      --served-model-name ${LLM_SERVED_NAME} \
      --tensor-parallel-size ${TENSOR_PARALLEL} \
      --pipeline-parallel-size ${PIPELINE_PARALLEL} \
      --max-model-len ${MAX_MODEL_LEN} \
      --gpu-memory-utilization ${GPU_MEM_UTIL} \
      --distributed-executor-backend ray \
      --host 0.0.0.0 --port 8000 > /tmp/vllm.log 2>&1"
    echo "vLLM 啟動中，log: docker exec $NAME tail -f /tmp/vllm.log"
    exit 0 ;;
  *) echo "unknown role"; exit 1 ;;
esac

# 高速網路請依環境設定 NCCL_SOCKET_IFNAME / NCCL_IB_HCA
docker run -d --name "$NAME" --restart unless-stopped \
  --gpus all --network host --ipc host --shm-size 16g \
  -e HF_HUB_OFFLINE=1 \
  -e NCCL_SOCKET_IFNAME="${NCCL_SOCKET_IFNAME:-eth0}" \
  -e VLLM_HOST_IP="$(hostname -I | awk '{print $1}')" \
  -v "${MODELS_DIR}:/models:ro" \
  --entrypoint bash "${VLLM_IMAGE}" -c "$RAY_CMD"

echo "$ROLE 已啟動；在 head 上用 'docker exec $NAME ray status' 確認節點數"
