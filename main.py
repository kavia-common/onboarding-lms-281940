from fastapi import FastAPI
from fastapi.responses import JSONResponse

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
