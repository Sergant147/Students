# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, HTTPException
from database import *

app = FastAPI()


@app.get('/students/', summary='Получить список всех студентов', tags=['GET'])
def get_students_api() -> dict[int, dict[str, int | str]]:
    return get_students()


@app.get('/students/{id}', summary='Получить конкреного студента', tags=['GET'])
def get_student_api(id: int) -> dict[str, str | int]:
    try:
        return get_student(id)
    except:
        raise HTTPException(status_code=404, detail='page not found')


@app.get('/students/clear/', summary='Отчистить таблицу студентов', tags=['NULL'])
def clear_table_api() -> str:
    clear_table()
    return 'success'


@app.put('/students/edit/{id}/{name}/{age}/{information}/{none_key}', summary='Изменить студента', tags=['PUT'])
def edit_student_api(id: int, none_key, name: str, age: int, information: str) -> str:
    try:
        if name == none_key:
            name = get_student(id)['name']
        if age == none_key:
            age = get_student(id)['age']
        if information == none_key:
            information = get_student(id)['information']
        edit_student(id, name, age, information)
    except:
        raise HTTPException(status_code=404, detail='page not found')
    return 'sucess'


@app.delete('/students/delete/{id}/', summary='Удалить студента', tags=['DELETE'])
def remove_student_api(id: int):
    try:
        remove_student(id)
    except:
        raise HTTPException(status_code=404, detail='page not found')
    return 'success'


@app.post('/students/add/{name}/{age}/{information}/', summary='Добавить студента', tags=['POST'])
def add_student_api(name: str, age: int, information: str) -> str:
    try:
        add_student(name, age, information)
    except:
        raise HTTPException(status_code=404, detail='page not found')
    return 'sucess'


if __name__ == '__main__':
    uvicorn.run('main:app')
