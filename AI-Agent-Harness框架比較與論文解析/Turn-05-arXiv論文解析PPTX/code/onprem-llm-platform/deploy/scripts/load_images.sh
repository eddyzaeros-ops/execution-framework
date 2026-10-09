#!/usr/bin/env bash
# 在內網執行：驗證雜湊後載入映像
set -euo pipefail
IN=${1:-./offline_bundle}
cd "$IN"
sha256sum -c SHA256SUMS --quiet || { echo "雜湊驗證失敗，停止載入"; exit 1; }
for f in *.tar; do docker load -i "$f"; done
# 檢查模型目錄中是否有不安全的 pickle 格式
if find . -name "*.bin" -o -name "*.pt" -o -name "*.pkl" | grep -q .; then
  echo "警告：發現 .bin/.pt/.pkl 檔，請改用 safetensors"
fi
echo "載入完成"
