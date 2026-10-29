from fastapi import HTTPException
from models.student_model import StudentCreate, StudentUpdate

students = []


def create_student(student: StudentCreate):
    student_id = max((s["id"] for s in students), default=0) + 1

    new_student = {
        "id": student_id,
        **student.model_dump()
    }

    students.append(new_student)
    return new_student


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def update_student(student_id: int, student: StudentUpdate):
    for index, current in enumerate(students):
        if current["id"] == student_id:
            updated_student = {
                "id": student_id,
                **student.model_dump()
            }

            students[index] = updated_student
            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )