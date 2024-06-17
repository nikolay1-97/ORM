"""Файл запуска приложения."""
from fastapi import FastAPI
import uvicorn

from views.defects import defect_router
from views.employees import employee_router
from config import APP_HOST, APP_PORT


def get_application() -> FastAPI:
    """Возвращает экземпляр приложения.

    Returns:
        FastAPI: _description_
    """
    application = FastAPI()
    return application


application = get_application()
application.include_router(defect_router)
application.include_router(employee_router)


if __name__ == '__main__':
    uvicorn.run(
        app=application,
        host=str(APP_HOST),
        port=int(APP_PORT),
    )
