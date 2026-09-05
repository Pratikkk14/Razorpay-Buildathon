"""Base models and mixins."""
from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, func
from app.core.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class TimestampMixin:
    """Provides created_at and updated_at timestamps."""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class UUIDMixin:
    """Provides a UUID string primary key."""
    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
