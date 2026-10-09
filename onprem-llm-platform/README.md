# 地端模型平台與評估集

技術文件問答（附出處、分級權限、全程稽核）的地端平台，以及配套的評估框架。設計說明見 [docs/DESIGN.md](docs/DESIGN.md)。

## 目錄

```
deploy/        docker-compose、多節點 vLLM 腳本、離線匯出匯入腳本
rag/           RAG API（FastAPI）：切分、匯入、混合檢索、權限、稽核
config/        users.yaml（API Key 雜湊、密等、專案）
docs_corpus/   範例語料（.md + .meta.yaml）
eval/          評估集、評估執行與比較腳本
tools/         API Key 雜湊工具
```

## 快速開始

```bash
cd deploy && cp .env.example .env      # 修改模型路徑、IP、平行度
# 1. LLM（每台 GPU 節點）
./scripts/run_llm_cluster.sh head      # head 節點
./scripts/run_llm_cluster.sh worker    # 其他節點
./scripts/run_llm_cluster.sh serve     # 回到 head 節點啟動 vLLM
# 2. Embedding / reranker 節點
docker compose -f docker-compose.embed.yml up -d
# 3. Qdrant + RAG API
docker compose up -d --build
# 4. 匯入文件
docker compose exec rag-api python -m app.ingest /app/corpus
curl -s -X POST localhost:8080/admin/reload -H "X-API-Key: key-admin"
# 5. 提問
curl -s localhost:8080/ask -H "X-API-Key: key-alice" -H "Content-Type: application/json" \
     -d '{"question":"電源子系統的輸入電壓範圍是多少？"}'
```

## 評估

```bash
pip install httpx pyyaml
python eval/run_eval.py --dataset eval/datasets/doc_qa_v1.jsonl --api http://localhost:8080 \
    --judge-url http://<LLM_IP>:8000/v1 --judge-model domain-llm --tag baseline
python eval/compare.py eval/results/baseline.json eval/results/<新的tag>.json
```

- 發現越權洩漏時，程式以結束碼 2 結束，可接到 CI 當上線關卡。
- 範例評估集涵蓋：數值題、跨章節題、應拒答題、越權題、prompt injection。正式使用時請擴充到 50–200 題真實問題。

## 上線前必做

- 更換 `config/users.yaml` 與 `eval/eval_users.yaml` 中的測試帳號，並改接單位身分驗證系統。
- `.env` 中的映像改為固定版本號，經資安掃描後再離線帶入。
- 確認模型授權與來源符合單位規定，模型檔只用 safetensors。
