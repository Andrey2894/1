from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    father_name: Optional[str] = None
    department_id: Optional[int] = None

class UserOut(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    father_name: Optional[str] = None
    department_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
