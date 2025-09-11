from pydantic import BaseModel , HttpUrl

class Recaptcha(BaseModel):
    url : HttpUrl
    website_key : str

class CloudFlare(BaseModel):
    url : HttpUrl