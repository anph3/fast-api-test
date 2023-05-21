from fastapi import FastAPI
from app.urls import UrlPatterns
from app.routings import all_url

app = FastAPI()

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]

app.include_router(UrlPatterns(urlpatterns=urlpatterns).router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
