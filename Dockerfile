FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:0.13.9 /uv /uvx /bin/

WORKDIR /app

ENV PYTHONPATH=/app

COPY pyproject.toml .
COPY uv.lock .

run uv sync

COPY src/ ./src/

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]