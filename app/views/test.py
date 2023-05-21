from ..serializers import test

fake_db = []

class TestView:
    async def get_todos():
        return fake_db
    
    async def post_todos(todo: test.TodoItem):
        todo.id = len(fake_db) + 1
        fake_db.append(todo)
        return todo