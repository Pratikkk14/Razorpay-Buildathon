"""ML Model Service registry and factory."""
import logging
from typing import Dict, List, Any
from app.services.ml.interface import MLModelService
from app.services.ml.mock_service import MockMLModelService
from app.services.ml.catboost_service import CatBoostMLModelService
from app.core.config import settings

logger = logging.getLogger(__name__)

# Registry of available ML model service implementations
_SERVICES: Dict[str, MLModelService] = {
    "mock": MockMLModelService(),
}

# Instantiate CatBoost service
try:
    catboost_svc = CatBoostMLModelService()
    if catboost_svc.is_loaded:
        _SERVICES["catboost"] = catboost_svc
        _SERVICES["production"] = catboost_svc
        logger.info("Successfully registered CatBoost ML Model Service as 'catboost' and 'production'.")
    else:
        logger.info("CatBoost model file not found or not loaded yet.")
except Exception as e:
    logger.warning(f"Could not initialize CatBoost ML Model Service: {e}")

_ACTIVE_SERVICE_KEY = settings.ACTIVE_ML_SERVICE if settings.ACTIVE_ML_SERVICE in _SERVICES else "mock"


def get_ml_service(name: str = None) -> MLModelService:
    """Returns the requested or currently active ML Model Service."""
    target = name or _ACTIVE_SERVICE_KEY
    if target not in _SERVICES:
        logger.warning(f"ML service '{target}' not found. Falling back to 'mock'.")
        target = "mock"
    return _SERVICES[target]


def register_ml_service(key: str, service: MLModelService, set_active: bool = False):
    """
    Registers a new ML Model Service (e.g. Kaggle model wrapper, XGBoost, PyTorch, CatBoost).
    """
    global _ACTIVE_SERVICE_KEY
    _SERVICES[key] = service
    if set_active:
        _ACTIVE_SERVICE_KEY = key
    logger.info(f"Registered ML service '{key}' (version {service.model_version}). Active: {set_active}")


def set_active_service(key: str) -> bool:
    """Sets the active ML model service key."""
    global _ACTIVE_SERVICE_KEY
    if key in _SERVICES:
        _ACTIVE_SERVICE_KEY = key
        logger.info(f"Active ML service switched to: {key}")
        return True
    logger.warning(f"Cannot switch to unknown ML service '{key}'")
    return False


def list_available_services() -> Dict[str, Dict[str, Any]]:
    """Lists all registered ML model services and their metadata."""
    return {
        key: {
            "name": svc.model_name,
            "version": svc.model_version,
            "is_active": (key == _ACTIVE_SERVICE_KEY),
        }
        for key, svc in _SERVICES.items()
    }

