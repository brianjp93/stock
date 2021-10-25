from fastapi import HTTPException

InvalidCredentials = HTTPException(
    status_code=400, detail="Incorrect username or password"
)
