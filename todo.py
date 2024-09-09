from fastapi import APIRouter, HTTPException
from fastapi import Path
from starlette import status

# from models import  TodoItem, TodoItems

router = APIRouter()
todo_list = []

#
# @router.get("/todo", response_model=TodoItems)
# async def retrieve_todo() -> dict:
#     return {
#         "todos": todo_list
#     }
#
#
# @router.post('/todo', status_code=status.HTTP_201_CREATED)
# async def add_todo(todo: TodoItem):
#     todo_list.append(todo)
#     return f"Record todo ={todo} added successfully"
#
#
# @router.get('/todo/{todo_id}')
# async def get_todo_by_id(todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
#     todo = list(filter(lambda todo_element: todo_element.id == todo_id, todo_list))
#
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
#
#     return {"todo": todo[0]}
#
#
# @router.put("/todo/{todo_id}")
# async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
#     todo = next((element for element in todo_list if element.id == todo_id), None)
#     if todo:
#         todo.item = todo_data
#         return {
#             "message": "Todo updated successfully."
#         }
#     return {
#         "message": "Todo with supplied ID doesn't exist."
#     }
#
#
# @router.delete('/todo/')
# async def delete_todo() -> dict:
#     todo_list.clear()
#     return {"message": "Todo deleted successfully."}
