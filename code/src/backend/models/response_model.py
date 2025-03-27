from pydantic import BaseModel

class ResponseModel(BaseModel):
    request_type: str
    sub_request_type: str
    confidence_score: float