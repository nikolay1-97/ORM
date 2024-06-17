"""Операции с данными для сущности дефект."""
from fastapi import HTTPException
from starlette import status

from ORM import MyORM
from pydantic_models.pydantic_models import (
    Defect,
    DefectResponseUpdate,
    CreateDefect,
    DefectUpdate,
 )


class DefectRepository:
    """Репозиторий для сущности дефект."""

    TABLE_NAME = 'defects'

    @classmethod
    def get_defect_by_id(cls, defect_id: int):
        """Возвращает сущность дефект по id."""
        defect = MyORM.select(cls.TABLE_NAME, 'id', defect_id)
        if defect:
            return defect
        return False
    
    @classmethod
    def get_defect_by_name(cls, defect_name: str):
        """Возвращает сущность дефект по имени."""
        defect = MyORM.select(cls.TABLE_NAME, 'defect', defect_name)
        if defect:
            return defect
        return False
    
    @classmethod
    def create_defect(cls, request: CreateDefect):
        """Создает сущность дефект."""
        MyORM.insert(
            cls.TABLE_NAME,
            code = request.code,
            defect = request.defect.lower(),
            name_of_works = request.name_of_works,
            measure = request.measure,
            number = request.number,
        )
        defect = cls.get_defect_by_name(request.defect.lower())

        return Defect(
            id = defect[0],
            code = defect[1],
            defect = defect[2],
            name_of_works = defect[3],
            measure = defect[4],
            number = defect[5],
        )
    
    @classmethod
    def get_defect(cls, defect_id: int):
        """Возвращает сущность дефект по id."""
        defect = cls.get_defect_by_id(defect_id)
        if defect:
            return Defect(
                id = defect[0],
                code = defect[1],
                defect = defect[2],
                name_of_works = defect[3],
                measure = defect[4],
                number = defect[5]
            )
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Дефекта с id {defect_id} не существует',
            )

    @classmethod
    def get_defects_list(cls):
        """Возвращает список дефектов."""
        response = {}
        data = MyORM.select(cls.TABLE_NAME)
        for defect in data:
            response[defect[0]] = {
                'id': defect[0],
                'код': defect[1],
                'дефект': defect[2],
                'вид работ': defect[3],
                'единицы измерения': defect[4],
                'численность': defect[5],
            }
        return response
    
    @classmethod
    def update_defect(cls, defect_id: int, request: DefectUpdate):
        """Обновляет сущность дефект."""
        exists_defect = cls.get_defect_by_id(defect_id)
        if exists_defect:
            MyORM.update(
                cls.TABLE_NAME,
                'id',
                defect_id,
                code = request.code,
                defect = request.defect.lower(),
                name_of_works=request.name_of_works,
                measure = request.measure,
                number = request.number,
            )
            defect = cls.get_defect_by_id(defect_id)
            return DefectResponseUpdate(
                id = defect_id,
                new_code = defect[1],
                new_defect = defect[2],
                new_name_of_works = defect[3],
                new_measure = defect[4],
                new_number = defect[5],
            )
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Дефекта с id {defect_id} не существует',
            )
    
    @classmethod
    def delete_defect(cls, defect_id: int):
        """Удаляет сущность дефект."""
        exists_defect = cls.get_defect_by_id(defect_id)
        if exists_defect:
            MyORM.delete(cls.TABLE_NAME, 'id', defect_id)
            return {'message': f'Позиция с id {defect_id} успешно удалена'}
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Дефекта с id {defect_id} не существует',
            )
