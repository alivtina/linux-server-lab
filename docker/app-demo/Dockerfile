FROM python:alpine

COPY app.py /app.py

EXPOSE 8000

RUN adduser -D appuser

USER appuser

CMD ["python", "/app.py"]
