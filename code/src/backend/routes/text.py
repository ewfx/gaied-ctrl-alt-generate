from fastapi import APIRouter, Depends, status
from models.response_model import ResponseModel
from models.text_request import TextRequest

router = APIRouter()

@router.post("/text", response_model=ResponseModel, status_code=status.HTTP_200_OK)
def read_text(text_object: TextRequest = Depends(TextRequest)):
    """
        gets email content as text and passes it to the model and returns the response json
    """
    # Use the request model (TextRequest) to extract input
    input_text = text_object.text

    # Create a response using the response model (ResponseModel)
    response = ResponseModel(
        request_type=input_text,
        sub_request_type="positive",
        confidence_score=0.99
    )
    return response

