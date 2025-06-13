from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import psycopg2
from src.database import get_db
from src.auth import get_password_hash, authenticate_user, create_access_token
from src.models import UserCreate
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=dict)
async def register_user(user: UserCreate, conn=Depends(get_db)):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE username = %s", (user.username,))
        if cur.fetchone():
            cur.close()
            raise HTTPException(status_code=400, detail="Username already registered")
        
        hashed_password = get_password_hash(user.password)
        cur.execute(
            "INSERT INTO users (username, hashed_password) VALUES (%s, %s) RETURNING id, username",
            (user.username, hashed_password)
        )
        user_data = cur.fetchone()
        conn.commit()
        cur.close()
        return {"id": user_data[0], "username": user_data[1]}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), conn=Depends(get_db)):
    user = authenticate_user(conn, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}