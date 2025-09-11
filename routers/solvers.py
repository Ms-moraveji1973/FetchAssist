from fastapi import APIRouter ,status, HTTPException
from services import cloudflare_service , recaptcha_service
from schema import Recaptcha , CloudFlare
import requests
router = APIRouter(prefix='/solver')

# return token-captcha
@router.post('/recaptchaV2')
def recaptchaV2(URL_and_WebisteKey:Recaptcha):
    try:
        response  = recaptcha_service.recaptcha(str(URL_and_WebisteKey.url),URL_and_WebisteKey.website_key)
        if response :
            return {'token':response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# return content and status
@router.post('/cloudflare')
def cloudflare(URL:CloudFlare):
    try:
        content , status = cloudflare_service.cloudflare(str(URL.url))
        if content and status :
            return {'content':content,'status':status}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))

@router.post('/request_test')
def cloudflare_test(URL:CloudFlare):
    res = requests.get(str(URL.url)).status_code
    if res :
        return {'status':res}
    else :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=("can't find your website"))