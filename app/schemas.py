from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class URLCreate(URLBase):
    pass


class URLInfo(URLBase):
    key: str
    is_active: bool = True


    class Config:
        from_attributes = True