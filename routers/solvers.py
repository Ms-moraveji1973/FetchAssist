from fastapi import APIRouter ,status, HTTPException , Depends , UploadFile
from services import cloudflare_service , recaptcha_service , image_captcha_service
from schema import UrlSchema
from typing import Annotated
from sqlalchemy.orm import Session
import requests
import aiofiles

# internal package
from database import get_db

router = APIRouter(prefix='/solver')

# return token-captcha
@router.post('/recaptchaV2')
def recaptchaV2(db:Annotated[Session,Depends(get_db)],URL:UrlSchema):
    try:
        response  = recaptcha_service.recaptcha(db,str(URL.url))
        if response :
            return {'response':response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# return content and status
@router.post('/cloudflare')
def cloudflare(URL:UrlSchema):
    try:
        content , status = cloudflare_service.cloudflare(str(URL.url))
        if content and status :
            return {'status':status,'content':content}
    except Exception as e:
        raise HTTPException(status_code=status, detail=str(e))

@router.post('/request_test')
def cloudflare_test(URL:UrlSchema):
    res = requests.get(str(URL.url)).status_code
    if res :
        return {'status':res}
    else :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=("can't find your website"))

@router.post("/image_captcha/")
async def create_upload_file(image: UploadFile):
    output_image = "images/main.png"
    async with aiofiles.open(output_image, 'wb') as out_file:
        content = await image.read()  # async read
        await out_file.write(content)  # async write

    return image_captcha_service.image_processing(output_image)







