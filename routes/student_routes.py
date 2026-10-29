from fastapi import APIRouter, Response, status

from models.student_model import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)

from controllers import student_controller

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student_controller.create_student(student)


@router.get("", response_model=list[StudentResponse])
def get_all_students():
    return student_controller.get_all_students()


@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student_by_id(student_id: int):
    return student_controller.get_student_by_id(student_id)


@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(student_id: int, student: StudentUpdate):
    return student_controller.update_student(
        student_id,
        student
    )


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    student_controller.delete_student(student_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )