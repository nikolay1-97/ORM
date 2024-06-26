# Описание приложения.
Класс с ORM находится в файле "/app/ORM.py".
Для взаимодействия с ORM, был написан API на FastAPI.
При запуске приложения в Docker, таблицы базы данных заполняются подготовленными данными.
В каждую таблицу записываются по 3 записи.
# Описание логики заполнения таблиц.
## Логика заполнения таблицы "Дефекты".
При заполнении таблицы "defects", поле "name_of_works" заполняется исходя из условий:
- если поле "defect" имеет значение "неравномерное прокрашивание", поле "name_of_works" принимает значение "перекраска",
  поле "measure", принимает значение "процент на 1 кв. метр";
- если поле "defect" имеет значение "наличие царапин", поле "name_of_works" принимает значение "полировка",
  поле "measure", принимает значение "процент на 1 кв. метр";
- если поле "defect" имеет значение "наличие изгибов", поле "name_of_works" принимает значение "рихтовка",
поле "measure", принимает значение "количество на 1 единицу".

Данная логика реализуется с помощью триггеров базы данных.
## Логика заполнения таблицы "Сотрудники".
При заполнении таблицы "employees", поле "employee" заполняется объединением значений из полей "id" и "employee".
Данная логика реализуется с помощью триггеров базы данных.
# Описание структуры приложения.
Класc c ORM находится в файле "/app/ORM.py".

Зависимости находятся в файле "/app/pyproject.toml".

Файл запуска приложения- "/app/main.py".

Переменные окружения для локального запуска приложения- "/.env.py".

Переменные окружения для запуска приложения в Docker- "/.env-non-dev".

Репозиторий для сущности "Дефект"- "/app/data_sources/storages/defect_repository.py".

Репозиторий для сущности "Сотрудник"- "/app/data_souirces/storages/employee_repository.py".

Хендлеры для сущности "Дефект"- "/app/views/defects.py".

Хендлеры для сущности "Сотрудник"- "/app/views/employees.py".

Конфигурация приложения- "/app/config.py".

Триггеры базы данных- "/app/triggers.py".

Создание таблиц базы данных- "/app/create_tables.py".

Заполнение таблиц базы данных подготовленными значениями- "/app/database_entry.py".

Очистка таблиц базы данных- "/app/clear_database.py".

Баш скрипт для работы приложения в Docker- "/scripts_for_docker/app.sh".
# Запуск приложения в Docker.
## Подготовка к запуску.
Для запуска приложения в Docker, необходимо установить значения для переменных окружения в файле "/.env-non-dev".
В данном файле находятся следующие переменные окружения:
- POSTGRES_DB;
- POSTGRES_USER;
- POSTGRES_PASSWORD;
- DB_USER;
- PASSWORD;
- DB_HOST;
- DB_NAME;
- DB_PORT;
- APP_HOST=127.0.0.1
- APP_PORT=8000
## Запуск приложения в Docker.
Для сборки контейнеров, необходимо выполнить команду "docker compose build" из коневой директории.

Для запуска приложения в Docker, необходимо выполнить команду "docker compose up app" из корневой директории.

При запуске приложения в Docker, таблицы базы данных заполняются подготовленными данными.
В каждую таблицу записываются по 3 записи.

Для взаимодействия с приложением, перейдите по ссылке "127.0.0.1:8000/docs", после запуска приложения.
По данной ссылке, будет доступна автодокументация приложения.
Хост и порт, указанный в данной ссылке, устанавливаются через соответствующие переменные окружения,
которые находятся в файле "/.env-non-dev".
# Запуск приложения локально.
## Подготовка к запуску.
Для установки зависимостей, необходимо выполнить команду "poetry install" из корневой директории.

Для активации виртуального окружения, необходимо выполнить команду "poetry shell" из корневой директории.

Перед запуском приложения, необходимо установить значения для переменных окружения в файле "/.env".
В данном файле находятся следующие переменные окружения:
- DB_USER- имя пользователя базы данных;
- PASSWORD- пароль для базы данных;
- DB_HOST- хост базы данных;
- DB_NAME- имя базы данных;
- DB_PORT- порт базы данных;
- APP_HOST- хост для запуска приложения;
- APP_PORT- порт для запуска приложения.
## Запуск приложения.
Для запуска приложения, необходимо выполнить команду "python main.py" в терминале, из директории "/app".

Для создания таблиц базы данных, необходимо выполнить команду "python create_tables.py" в терминале, из директории "/app".

Для создания триггеров, необходимо выполнить команду "python triggers.py" в терминале, из директоии "/app".

Для заполнения таблиц базы данных подготовленными данными, необходимо выполнить команду "python database_entry.py"
в терминале, из директории "/app".

Для взаимодействия с приложением, перейдите по ссылке "127.0.0.1:8000/docs", после запуска приложения.
По данной ссылке, будет доступна автодокументация приложения.

Хост и порт, указанный в данной ссылке, устанавливаются через соответствующие переменные окружения,
которые находятся в файле "/.env".


