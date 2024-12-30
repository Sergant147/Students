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
    raise HTTPException(status_code=404, detail='page not found')


@app.post('/students/post/')
def add_student(st) -> None:
    students.append({
        'id': max([s['id'] for s in students], default=0) + 1,
        'name': st.name,
        'age': st.age,
        'information': st.information

    })


@app.put('/students/edit/{id}/')
def edit_student(id, name=None, age=None, information=None):
    if id not in get_ids():
        raise HTTPException(status_code=404,
                            detail='page not found')
    index = get_index_by_id(id)
    if name is not None:
        students[index]['name'] = name
    if age is not None:
        students[index]['age'] = age
    if information is not None:
        students[index]['information'] = information


@app.delete('/students/delete/{id}/')
def remove_student(id) -> None:
    if id not in get_ids():
        raise HTTPException(status_code=404, detail='page not found')
    index = get_index_by_id(id)
    students.remove(students[index])


def get_ids():
    ids = []
    for student in students:
        ids.append(student['id'])
    return ids


def get_index_by_id(id):
    for index, element in enumerate(students):
        if element['id'] == id:
            return index


if __name__ == '__main__':
    uvicorn.run('main:app')
