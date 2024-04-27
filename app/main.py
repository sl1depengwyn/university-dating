from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.profile_data import ProfileData
from app.models.user import User
from app.db.database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Here you would check if the email domain is correct (university domain),
    # hash the password, and add the new user to the database.
    pass

@app.put("/users/{user_id}/profile")
def update_profile(user_id: int, profile_data: ProfileData, db: Session = Depends(get_db)):
    # Logic to update the user's profile with the provided data
    pass


@app.put("/users/{user_id}/profile")
def update_profile(user_id: int, profile_data: ProfileData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.interests = profile_data.interests
    user.hobbies = profile_data.hobbies
    user.preferences = profile_data.preferences
    # Update any additional fields as necessary
    db.commit()
    return {"msg": "Profile updated successfully"}