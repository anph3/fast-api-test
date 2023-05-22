from fastapi.exceptions import RequestValidationError
from fastapi import Request
from configs.response import ResponseData
from fastapi.responses import JSONResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = ""
    for error in exc.errors():
        error_messages+=str(error["loc"])
    response =  ResponseData(
            status=2,
            message=error["msg"], 
            data=error_messages
        )
    return JSONResponse(response.dict())