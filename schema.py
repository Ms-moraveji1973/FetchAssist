from pydantic import BaseModel , HttpUrl

class Recaptcha(BaseModel):
    url : HttpUrl

class CloudFlare(BaseModel):
    url : HttpUrl