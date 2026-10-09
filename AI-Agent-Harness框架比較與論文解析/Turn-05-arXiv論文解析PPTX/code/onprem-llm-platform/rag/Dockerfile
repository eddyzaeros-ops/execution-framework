FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
# 離線環境：可改為 pip install --no-index --find-links=/wheels -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
RUN useradd -m appuser && mkdir -p /app/data && chown -R appuser /app/data
USER appuser
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
