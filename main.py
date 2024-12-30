import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
class Student(BaseModel):
    name: str
    age: int
    information: str
students = []
app = FastAPI()
@app.get('/students/')
def get_students() -> list[dict[str, str | int]]:
    return students
@app.get('/students/get_{id}/')
def get_student(id) -> dict[str, str | int] | None:
    for student in students:
        if student['id'] == id:
            return student
    raise HTTPException(status_code=404,detail='page not found')
@app.post('/students/post/')
def add_student(st) -> None:
    students.append({
        'id': max([s['id'] for s in students],default=0)+1,
        'name': st.name,
        'age': st.age,
        'information': st.information

    })
@app.put('/students/edit/{id}/')
def edit_student(id,name=None,age=None,information=None) -> dict[str, str | int]:
    if id not in get_ids():
        raise HTTPException(status_code=404,
                            detail='page not found')
def get_ids():
    ids = []
    for student in students:
        ids.append(student['id'])
if __name__ == '__main__':
    uvicorn.run('main:app')