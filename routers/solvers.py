from fastapi import APIRouter ,status, HTTPException , Depends
from services import cloudflare_service , recaptcha_service
from schema import Recaptcha , CloudFlare
from typing import Annotated , List
from sqlalchemy.orm import Session
import requests

# internal package
from database import SessionLocal

router = APIRouter(prefix='/solver')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()

# return token-captcha
@router.post('/recaptchaV2')
def recaptchaV2(db:Annotated[Session,Depends(get_db)],URL:Recaptcha):
    try:
        response  = recaptcha_service.recaptcha(db,str(URL.url))
        if response :
            return {'response':response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# return content and status
@router.post('/cloudflare')
def cloudflare(URL:CloudFlare):
    try:
        content , status = cloudflare_service.cloudflare(str(URL.url))
        if content and status :
            return {'status':status,'content':content}
    except Exception as e:
        raise HTTPException(status_code=status, detail=str(e))

@router.post('/request_test')
def cloudflare_test(URL:CloudFlare):
    res = requests.get(str(URL.url)).status_code
    if res :
        return {'status':res}
    else :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=("can't find your website"))