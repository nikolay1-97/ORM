"""Модуль с моделями данных для запрсов и ответов."""
from pydantic import BaseModel

class Defect(BaseModel):
    """Модель для сущности дефект."""
    id: int
    code: int
    defect: str
    name_of_works: str
    measure: str
    number: int

class DefectUpdate(BaseModel):
    """Модель для обновления сущности дефект."""
    code: int
    defect: str
    name_of_works: str
    measure: str
    number: int


class DefectResponseUpdate(BaseModel):
    """Модель ответа для обновления сущности дефект."""
    id: int
    new_code: int
    new_defect: str
    new_name_of_works: str
    new_measure: str
    new_number: int

class CreateDefect(BaseModel):
    """Модель для создания сущности дефект."""
    code: int
    defect: str
    name_of_works: str
    measure: str
    number: int


class Employee(BaseModel):
    """Модель для сущности сотрудник."""
    id: int
    employee: str
    surname: str
    name: str
    otchestvo: str
    amount_of_sheets: int


class EmployeeUpdate(BaseModel):
    """Модель для обновления сущности сотрудник."""
    employee: str
    surname: str
    name: str
    otchestvo: str
    amount_of_sheets: int


class EmployeeUpdateResponse(BaseModel):
    """Модель ответа для обновления сущности сотрудник."""
    id: int
    new_employee: str
    new_surname: str
    new_name: str
    new_otchestvo: str
    new_amount_of_sheets: int
