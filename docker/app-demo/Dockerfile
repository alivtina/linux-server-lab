FROM python:alpine

COPY app.py /app.py

EXPOSE 8000

RUN adduser -D appuser

USER appuser

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
    CMD wget -q -O - http://127.0.0.1:8000/health

CMD ["python", "/app.py"]
