from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    username: str
    age: int = Field(gt=0, description="Age must be positive")
    email: str

# Validates and raises errors automatically if types don't match!
user = UserProfile(username="mahidi", age=22, email="mahidi@example.com")
print(user.model_dump_json())