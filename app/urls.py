from fastapi import APIRouter, HTTPException

fake_db = []

class UrlPatterns:
    def __init__(self, urlpatterns = []):
        self.urlpatterns = urlpatterns
        self.router = APIRouter()
        self.register_routes()
    
    def register_routes(self):
        for route_mapping in self.urlpatterns:
            method = route_mapping["method"]
            path = route_mapping["path"]
            handler = route_mapping["handler"]
            getattr(self.router, method)(path)(handler)
        
    async def get_todos(self):
        return fake_db