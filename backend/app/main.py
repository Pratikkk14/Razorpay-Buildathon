"""FastAPI Application entry point for Recovery Intelligence & Allocation Engine."""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import init_db, SessionLocal
from app.core.logging import setup_logging
from app.api.routes_cases import router as cases_router
from app.api.routes_decisions import router as decisions_router
from app.api.routes_actions import router as actions_router
from app.api.routes_webhooks import router as webhooks_router
from app.api.routes_simulator import router as simulator_router
from app.api.routes_experiments import router as experiments_router
from app.api.routes_analytics import router as analytics_router
from app.api.routes_governance import router as governance_router
from app.api.routes_audit import router as audit_router
from app.api.routes_demo import router as demo_router
from app.services.simulator.simulator_service import SimulatorService
from app.models.case import Case

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events."""
    logger.info("Starting up Recovery Intelligence & Allocation Engine...")
    init_db()
    
    # Auto-seed initial demo scenarios if database is empty
    db = SessionLocal()
    try:
        case_count = db.query(Case).count()
        if case_count == 0:
            logger.info("Empty database detected. Auto-seeding 5 Buildathon Demo Scenarios...")
            sim = SimulatorService()
            for s in ["scenario_1_high_natural", "scenario_2_high_uplift", "scenario_3_multi_action_economics", "scenario_4_safety_veto", "scenario_5_high_value_escalation"]:
                try:
                    sim.load_demo_scenario(db, s)
                except Exception as e:
                    logger.error(f"Error seeding scenario {s}: {e}")
            logger.info("Demo scenarios seeded successfully.")
    finally:
        db.close()

    yield
    logger.info("Shutting down Recovery Intelligence & Allocation Engine.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "Production-grade Recovery Intelligence & Allocation Engine for Razorpay AI Buildathon 2026. "
        "Optimizes failed payment recovery for Incremental Contribution rather than raw recovery rate."
    ),
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(cases_router, prefix=settings.API_PREFIX)
app.include_router(decisions_router, prefix=settings.API_PREFIX)
app.include_router(actions_router, prefix=settings.API_PREFIX)
app.include_router(webhooks_router, prefix=settings.API_PREFIX)
app.include_router(simulator_router, prefix=settings.API_PREFIX)
app.include_router(experiments_router, prefix=settings.API_PREFIX)
app.include_router(analytics_router, prefix=settings.API_PREFIX)
app.include_router(governance_router, prefix=settings.API_PREFIX)
app.include_router(audit_router, prefix=settings.API_PREFIX)
app.include_router(demo_router, prefix=settings.API_PREFIX)


@app.get("/")
def health_check():
    return {
        "status": "online",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "thesis": "Recovery rate is the wrong optimization target. Incremental contribution is."
    }
