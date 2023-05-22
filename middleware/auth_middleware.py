from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

class AuthMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, request: Request, call_next):
        
        response = await call_next(request)
        
        # return JSONResponse({"asdasd":"asdadas"})
    
        return response