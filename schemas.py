from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    class Config:
        from_attributes = True  # Включаємо підтримку ORM


class STaskAddId(BaseModel):
    ok: bool = True
    task_id: int

