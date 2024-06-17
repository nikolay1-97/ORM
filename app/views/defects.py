"""Хендлеры для сущности дефект."""
from fastapi import APIRouter
from fastapi import Request

from data_sources.storages.defect_repository import DefectRepository
from pydantic_models.pydantic_models import DefectUpdate, CreateDefect


defect_router = APIRouter()

@defect_router.post('/api/v1/defects')
def create_defect(request: CreateDefect):
    return DefectRepository.create_defect(request)


@defect_router.get('/api/v1/defects')
def get_defects_list(request: Request):
    return DefectRepository.get_defects_list()


@defect_router.get('/api/v1/defects{target_defect_id}')
def get_defect(request: Request, target_defect_id: int):
    return DefectRepository.get_defect(target_defect_id)


@defect_router.patch('/api/v1/defects{target_defect_id}')
def update_defect(request: DefectUpdate, target_defect_id: int):
    return DefectRepository.update_defect(target_defect_id, request)


@defect_router.delete('/api/v1/defects{target_defect_id}')
def delete_defect(request: Request, target_defect_id: int):
    return DefectRepository.delete_defect(target_defect_id)
