# zt-be-billing-service

Billing Service for the ZeroTheft platform.

## Local Development

```bash
pip install -r requirements.txt
python app/main.py
```

## Docker

```bash
docker build -t zt-be-billing-service .
docker run -p 8002:8002 zt-be-billing-service
```

- **Port:** 8002
- **Health Check:** `GET /health`
- **Root Endpoint:** `GET /`
