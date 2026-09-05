# Machine Learning Model Integration Contract

## Overview
This application is completely decoupled from model training pipelines and specific ML frameworks.
You can develop your models independently in Kaggle / Jupyter notebooks (e.g. using XGBoost, LightGBM, Uplift Trees, PyTorch, Scikit-learn) and plug them into this application by implementing the single `MLModelService` interface.

---

## 1. Input Data Contract (`MLModelInput`)

Every inference request receives a structured Pydantic object:

```python
class MLModelInput(BaseModel):
    case_id: str
    amount: float                       # Payment amount in INR (e.g. 4999.0)
    currency: str = "INR"
    payment_method: str                 # "card", "upi", "netbanking", "wallet"
    failure_code: Optional[str]         # e.g. "INSUFFICIENT_FUNDS", "GATEWAY_TIMEOUT"
    issuing_bank: Optional[str]         # e.g. "HDFC", "ICICI", "SBI"
    attempt_count: int                  # Number of consecutive failures (e.g. 1, 2, 3)
    
    # Customer history & behavioral attributes
    customer_tenure_days: int           # Account age in days
    customer_ltv: float                 # Estimated lifetime value in INR
    customer_segment: str               # "standard", "enterprise", "vip", "dormant"
    total_lifetime_payments: int
    successful_lifetime_payments: int
    failed_lifetime_payments: int
    days_since_last_success: Optional[int]
    is_first_ever_failure: int          # 1 if first failure in account history, else 0
    
    # Timing & Channel attributes
    time_since_failure_minutes: float
    previous_interventions_count: int
    hours_since_last_contact: Optional[float]
    device_type: str                    # "mobile_android", "mobile_ios", "desktop_web"
    
    # Extensible arbitrary metadata dictionary
    additional_features: Optional[Dict[str, Any]]
```

---

## 2. Prediction Output Contract (`MLModelPrediction`)

Your model must return predictions conforming to:

```python
class MLModelPrediction(BaseModel):
    model_name: str                     # e.g. "KaggleUpliftXGBoost"
    model_version: str                  # e.g. "2.1.0"
    
    # Natural recovery baseline probability P(recovery | no action) in [0.0, 1.0]
    natural_recovery_probability: float
    
    # Predicted recovery probability for each candidate intervention action in [0.0, 1.0]
    action_outcomes: Dict[str, float] = {
        "retry": 0.20,
        "payment_link": 0.71,
        "reminder": 0.45,
        "alternate_method": 0.65,
        "human_escalation": 0.70
    }
    
    # Incremental lift = action_outcomes[a] - natural_recovery_probability
    uplift: Dict[str, float] = {
        "retry": 0.08,
        "payment_link": 0.59,
        "reminder": 0.33,
        "alternate_method": 0.53,
        "human_escalation": 0.58
    }
    
    # Confidence score in [0.0, 1.0]
    confidence: float = 0.91
    
    explanation_notes: Optional[str] = None
    feature_attributions: Optional[Dict[str, float]] = None
```

---

## 3. How to Plug In Your Trained Model

1. Save your trained model artifact (e.g. `model.pkl`, `model.joblib`, `model.json`, `model.onnx`, or `model.pt`) inside a directory such as `backend/app/services/ml/artifacts/`.
2. Create a new service file (e.g. `backend/app/services/ml/kaggle_service.py`):

```python
import joblib
from app.services.ml.interface import MLModelService
from app.schemas.ml import MLModelInput, MLModelPrediction

class KaggleUpliftModelService(MLModelService):
    def __init__(self, model_path: str = "path/to/model.pkl"):
        self.model = joblib.load(model_path)
        
    @property
    def model_name(self) -> str:
        return "KaggleTrainedUpliftV1"

    @property
    def model_version(self) -> str:
        return "1.0.0"

    def predict(self, input_data: MLModelInput) -> MLModelPrediction:
        # Extract feature vector from input_data
        # feature_vec = ...
        # nat_prob, action_probs = self.model.predict_proba(feature_vec)
        ...
```

3. Register your service in `backend/app/services/ml/registry.py`:

```python
from app.services.ml.registry import register_ml_service
from app.services.ml.kaggle_service import KaggleUpliftModelService

register_ml_service("kaggle_v1", KaggleUpliftModelService(), set_active=True)
```
