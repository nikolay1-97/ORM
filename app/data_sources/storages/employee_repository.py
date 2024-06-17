"""Операции с данными для сущности сотрудник."""
from fastapi import HTTPException
from starlette import status

from ORM import MyORM
from pydantic_models.pydantic_models import (
    Employee,
    EmployeeUpdateResponse,
    EmployeeUpdate,
)


class EmployeeRepository:
    """Репозиторий для сущности сотрудник."""

    TABLE_NAME = 'employees'

    @classmethod
    def get_employee_by_id(cls, employee_id: int):
        """Возвращает сущнсть сотрудник."""
        employee = MyORM.select(cls.TABLE_NAME, 'id', employee_id)
        if employee:
            return employee
        return False
    
    @classmethod
    def create_employee(cls, request: Employee):
        """Создает сущность сотрудник."""
        exists_employee = cls.get_employee_by_id(request.id)
        if not exists_employee:
            MyORM.insert(
                cls.TABLE_NAME,
                id = request.id,
                employee = request.employee,
                surname = request.surname,
                name = request.name,
                otchestvo = request.otchestvo,
                amount_of_sheets = request.amount_of_sheets,
            )
            employee = cls.get_employee_by_id(request.id)
            return Employee(
                id = employee[0],
                employee = employee[1],
                surname = employee[2],
                name = employee[3],
                otchestvo = employee[4],
                amount_of_sheets = employee[5],
            )

        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Сотрудник с id {request.id} уже существует',
            )
    
    @classmethod
    def get_employees_list(cls):
        """Возвращает список сотрудников."""
        response = {}
        data = MyORM.select(cls.TABLE_NAME)
        for employee in data:
            response[employee[0]] = {
                'id': employee[0],
                'сотрудник': employee[1],
                'фамилия': employee[2],
                'имя': employee[3],
                'отчество': employee[4],
                'количество отправленных листов': employee[5],
            }
        return response
    
    @classmethod
    def get_employee(cls, employee_id: int):
        """Возвращает сущность сотрудник."""
        employee = cls.get_employee_by_id(employee_id)
        if employee:
            return Employee(
                id = employee[0],
                employee = employee[1],
                surname = employee[2],
                name = employee[3],
                otchestvo = employee[4],
                amount_of_sheets = employee[5],
            )
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Сотрудника с id {employee_id} не существует',
            )
    
    @classmethod
    def update_employee(cls, employee_id: int, request: EmployeeUpdate):
        """Обновляет сущность сотрудник."""
        exists_employee = cls.get_employee_by_id(employee_id)
        if exists_employee:
            MyORM.update(
                cls.TABLE_NAME,
                'id',
                employee_id,
                employee = request.employee,
                surname = request.surname,
                name = request.name,
                otchestvo = request.otchestvo,
                amount_of_sheets = request.amount_of_sheets,
            )
            employee = cls.get_employee_by_id(employee_id)
            return EmployeeUpdateResponse(
                id = employee[0],
                new_employee = employee[1],
                new_surname = employee[2],
                new_name = employee[3],
                new_otchestvo = employee[4],
                new_amount_of_sheets = employee[5],
            )
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Сотрудника с id {employee_id} не существует',
            )
    
    @classmethod
    def delete_employee(cls, employee_id: int):
        """Удаляет сущность сотрудник."""
        exists_employee = cls.get_employee_by_id(employee_id)
        if exists_employee:
            MyORM.delete(cls.TABLE_NAME, 'id', employee_id)
            return {'message': f'Позиция с id {employee_id} успешно удалена'}
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Позиции с id {employee_id} не существует',
            )
    