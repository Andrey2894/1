from pydantic import BaseModel, ConfigDict

class DepartmentCreate(BaseModel):
    title: str
    boss_id: int

class DepartmentOut(BaseModel):
    id: int
    title: str
    boss_id: int

    model_config = ConfigDict(from_attributes=True)
