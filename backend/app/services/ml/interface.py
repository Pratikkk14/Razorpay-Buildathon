"""ML Model inference contract and base class."""
from abc import ABC, abstractmethod
from app.schemas.ml import MLModelInput, MLModelPrediction


class MLModelService(ABC):
    """
    Abstract interface for ML inference.
    All ML implementations (Mock, XGBoost, Scikit-learn, PyTorch, Kaggle export)
    must implement this interface.
    """

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Returns the identifier/name of the model."""
        pass

    @property
    @abstractmethod
    def model_version(self) -> str:
        """Returns the version string of the model."""
        pass

    @abstractmethod
    def predict(self, input_data: MLModelInput) -> MLModelPrediction:
        """
        Executes inference for a single recovery case input.
        Returns natural recovery probability, action outcome probabilities, uplift, and confidence.
        """
        pass
