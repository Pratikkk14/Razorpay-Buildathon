"""Configuration settings for Recovery Intelligence & Allocation Engine."""
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Recovery Intelligence & Allocation Engine"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_PREFIX: str = "/api"

    # Database
    DATABASE_URL: str = "sqlite:///./recovery_engine.db"

    # Razorpay Credentials (for Test Mode or Live, defaults to simulated test mode)
    RAZORPAY_KEY_ID: str = "rzp_test_mock_key_123456"
    RAZORPAY_KEY_SECRET: str = "mock_secret_key_abcdef"
    RAZORPAY_WEBHOOK_SECRET: str = "mock_webhook_secret_xyz789"
    SIMULATION_MODE: bool = True

    # Policy / Governance Defaults
    DEFAULT_MAX_RETRIES: int = 2
    DEFAULT_MAX_CONTACTS_PER_24H: int = 1
    DEFAULT_COOLDOWN_HOURS: int = 24
    DEFAULT_QUIET_HOURS_START: int = 21  # 9 PM (21:00)
    DEFAULT_QUIET_HOURS_END: int = 9    # 9 AM (09:00)
    DEFAULT_MIN_CONTRIBUTION_FLOOR: float = 0.0  # Require strictly positive contribution
    DEFAULT_HIGH_VALUE_THRESHOLD: float = 50000.0  # Transactions > 50,000 INR escalate to human review
    DEFAULT_INTERVENTION_BUDGET_DAILY: float = 5000.0

    # ML Interface Settings
    DEFAULT_ML_MODEL_NAME: str = "MockPropensityUpliftV1"
    DEFAULT_ML_MODEL_VERSION: str = "1.0.0"
    CONFIDENCE_THRESHOLD: float = 0.65

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173", "*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
