from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

# Initialize FastAPI app
app = FastAPI(
    title="Onboarding LMS API",
    description="Minimal FastAPI app to serve as ASGI entrypoint for the onboarding LMS service.",
    version="0.1.0",
    openapi_tags=[
        {"name": "Health", "description": "Health check endpoints"},
    ],
)

# PUBLIC_INTERFACE
@app.get("/health", tags=["Health"], summary="Health check", description="Returns service health status.")
def health() -> JSONResponse:
    """Health check endpoint returning 200 OK when the service is running."""
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    # Optional fallback: allow `python main.py` for local testing if uvicorn is not used explicitly.
    # Respect PORT env var if provided by platform; default to 3010 for preview.
    port = int(os.getenv("PORT", "3010"))
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
