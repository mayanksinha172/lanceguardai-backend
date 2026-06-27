from typing import Optional
from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    email: EmailStr
    name: str
    source: str = "hero"
    freelance_type: str = ""
    pain_point: str = ""
    current_tool: str = ""
    utm_source: str = ""
    utm_medium: str = ""
    utm_campaign: str = ""


class SignupResponse(BaseModel):
    position: int
    count: int
    already_registered: bool = False


class CountResponse(BaseModel):
    count: int


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    token: str


class WaitlistEntry(BaseModel):
    id: int
    email: str
    name: str
    source: str
    freelance_type: Optional[str] = None
    pain_point: Optional[str] = None
    current_tool: Optional[str] = None
    signed_up_at: str
    user_agent: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_campaign: Optional[str] = None


class WaitlistListResponse(BaseModel):
    entries: list[WaitlistEntry]
    total: int
    page: int
    per_page: int


class StatsResponse(BaseModel):
    total: int
    today: int
    this_week: int
    hero_count: int
    cta_count: int
    utm_sources: dict = {}
