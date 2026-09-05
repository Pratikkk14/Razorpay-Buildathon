"""ML Model Service registry and factory."""
import logging
from typing import Dict
from app.services.ml.interface import MLModelService
from app.services.ml.mock_service import MockMLModelService
from app.core.config import settings

logger = logging.getLogger(__name__)

# Registry of available ML model service implementations
_SERVICES: Dict[str, MLModelService] = {
    "mock": MockMLModelService(),
}

_ACTIVE_SERVICE_KEY = "mock"


def get_ml_service(name: str = None) -> MLModelService:
    """Returns the requested or currently active ML Model Service."""
    target = name or _ACTIVE_SERVICE_KEY
    if target not in _SERVICES:
        logger.warning(f"ML service '{target}' not found. Falling back to 'mock'.")
        target = "mock"
    return _SERVICES[target]


def register_ml_service(key: str, service: MLModelService, set_active: bool = False):
    """
    Registers a new ML Model Service (e.g. Kaggle model wrapper, XGBoost, PyTorch).
    """
    global _ACTIVE_SERVICE_KEY
    _SERVICES[key] = service
    if set_active:
        _ACTIVE_SERVICE_KEY = key
    logger.info(f"Registered ML service '{key}' (version {service.model_version}). Active: {set_active}")
