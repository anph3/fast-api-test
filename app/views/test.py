from ..serializers import test

fake_db = []

class TestView:
    async def get_todos():
        todo = test.TodoItem(id=1, title="Task 1")
        return todo.dict()
    
    async def post_todos(todo: test.TodoItem):
        todo.id = len(fake_db) + 1
        fake_db.append(todo)
        return todo