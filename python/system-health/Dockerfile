FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY system.py .

RUN useradd --create-home appuser

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "system.py"]
