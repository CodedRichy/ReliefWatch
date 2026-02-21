from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import events, alerts

app = FastAPI(
    title="ReliefWatch API",
    description="Humanitarian early-warning intelligence API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router)
app.include_router(alerts.router)


@app.get("/")
async def root():
    return {"status": "ok", "service": "reliefwatch"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
