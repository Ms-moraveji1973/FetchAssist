from pydantic import BaseModel , HttpUrl
from typing import Optional

class Recaptcha(BaseModel):
    url : HttpUrl

class CloudFlare(BaseModel):
    url : HttpUrl

class LogSchema(BaseModel):
    id: int
    website_url: str
    duration: float
    error_message: Optional[str] = None

    class Config:
        orm_mode = True


class DashboardState(BaseModel):
    total : int
    success : int
    win_rate : float
    duration_average : float

class DashboardResponse(BaseModel):
    logs : LogSchema
    state: DashboardState


