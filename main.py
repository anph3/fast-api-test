from fastapi import FastAPI, Request
from app.urls import UrlPatterns
from app.routings import all_url
from fastapi.middleware.cors import CORSMiddleware
from middleware.auth_middleware import AuthMiddleware
from fastapi.exceptions import RequestValidationError
from middleware.validate_middleware import validation_exception_handler

app = FastAPI(
    debug=True
)

app.middleware("http")(AuthMiddleware(app))
app.add_middleware(CORSMiddleware, allow_origins=["*"])

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]
    
app.exception_handler(RequestValidationError)(validation_exception_handler)

app.include_router(UrlPatterns(urlpatterns=urlpatterns).router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    
# uvicorn main:app --reload
