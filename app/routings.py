from app.views.test import TestView


all_url = {
    'url_test': [
        {"method": "get", "path": "/todos", "handler": TestView.get_todos},
        {"method": "post", "path": "/todos", "handler": TestView.post_todos},
    ]
}