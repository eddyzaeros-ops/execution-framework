#!/usr/bin/env bash
# 在可連網的建置機執行：匯出映像並產生 SHA256 清單
set -euo pipefail
cd "$(dirname "$0")/.."
source .env
OUT=${1:-./offline_bundle}
mkdir -p "$OUT"

docker pull "$VLLM_IMAGE"
docker pull "$QDRANT_IMAGE"
docker compose build rag-api

for img in "$VLLM_IMAGE" "$QDRANT_IMAGE" onprem/rag-api:0.1; do
  f="$OUT/$(echo "$img" | tr '/:' '__').tar"
  docker save "$img" -o "$f"
done

# 模型檔請另外放到 $OUT/models，並只保留 safetensors
(cd "$OUT" && find . -type f ! -name SHA256SUMS -print0 | xargs -0 sha256sum > SHA256SUMS)
echo "完成：$OUT（請先送資安掃描再帶入內網）"
