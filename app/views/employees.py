"""Хендлеры для сущности сотрудник."""
from fastapi import APIRouter
from fastapi import Request

from data_sources.storages.employee_repository import EmployeeRepository
from pydantic_models.pydantic_models import Employee, EmployeeUpdate


employee_router = APIRouter()

@employee_router.post('/api/v1/employees')
def create_employee(request: Employee):
    return EmployeeRepository.create_employee(request)


@employee_router.get('/api/v1/employees')
def get_employees_list(request: Request):
    return EmployeeRepository.get_employees_list()


@employee_router.get('/api/v1/employees{target_employee_id}')
def get_employee(request: Request, target_employee_id: int):
    return EmployeeRepository.get_employee(target_employee_id)


@employee_router.patch('/api/v1/employees{target_employee_id}')
def update_employee(request: EmployeeUpdate, target_employee_id: int):
    return EmployeeRepository.update_employee(target_employee_id, request)


@employee_router.delete('/api/v1/employees{target_employee_id}')
def delete_employee(request: Request, target_employee_id: int):
    return EmployeeRepository.delete_employee(target_employee_id)
