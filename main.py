from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel


app = FastAPI()
class PasswordRequest(BaseModel):
    password: str

@app.post("/api/v1/validade-password")
def validate_password(request: PasswordRequest):
    password = request.password
    
    """
    Validate the password based on the following rules:
    - At least 8 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return Response(content='{"valid": False, "reason": "Password must be at least 8 characters long."}', media_type="application/json", status_code=400)
    
    if not any(char.isupper() for char in password):
        return Response(content='{"valid": False, "reason": "Password must contain at least one uppercase letter."}', media_type="application/json", status_code=400)
    
    if not any(char.islower() for char in password):
        return Response(content='{"valid": False, "reason": "Password must contain at least one lowercase letter."}', media_type="application/json", status_code=400)

    if not any(char.isdigit() for char in password):
        return Response(content='{"valid": False, "reason": "Password must contain at least one digit."}', media_type="application/json", status_code=400)
    
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    if not any(char in special_characters for char in password):
        return Response(content='{"valid": False, "reason": "Password must contain at least one special character."}', media_type="application/json", status_code=400)

    return Response(status_code=204)