from typing import Optional
from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
    # class Config:
    #     from_attributes = True  # Включаємо підтримку ORM


class STaskAddId(BaseModel):
    ok: bool = True
    task_id: int

