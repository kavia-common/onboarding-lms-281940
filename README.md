# onboarding-lms

Backend service for the onboarding LMS.

## ASGI App and Health Check

This repository includes a minimal FastAPI application to ensure a valid ASGI entrypoint for Uvicorn:

- Entrypoint module: `main.py`
- Exported ASGI app: `app`
- Health endpoint: `GET /health` returns `{"status": "ok"}` with 200 OK

## Running Locally

1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the server (binds to 0.0.0.0 on port 3001):
   ```
   uvicorn main:app --host 0.0.0.0 --port 3001
   ```

Now open:
- Health check: http://localhost:3001/health
- OpenAPI docs: http://localhost:3001/docs

## Deployment Start Command

A `Procfile` is provided to run the service:
```
web: uvicorn main:app --host 0.0.0.0 --port 3001
```

If your platform uses a different mechanism to start the service, ensure it points to `main:app` and binds to `0.0.0.0:3001`.

## Notes

- If your environment expects a different port (e.g., 3010), update the Procfile and your start command accordingly and keep it consistent everywhere.
