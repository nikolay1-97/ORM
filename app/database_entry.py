"""Заполняет таблицы базы данных."""
from ORM import MyORM

MyORM.insert(
    'defects',
    code = 100,
    defect = 'неравномерное прокрашивание',
    name_of_works = '',
    measure = '',
    number = 3,
)

MyORM.insert(
    'defects',
    code = 200,
    defect = 'наличие царапин',
    name_of_works = '',
    measure = '',
    number = 2,
)

MyORM.insert(
    'defects',
    code = 300,
    defect = 'наличие изгибов',
    name_of_works = '',
    measure = '',
    number = 2,
)

MyORM.insert(
    'employees',
    id = 17504,
    employee = '23',
    surname = 'Зимин',
    name = 'Олег',
    otchestvo = 'Петрович',
    amount_of_sheets = 728,
)

MyORM.insert(
    'employees',
    id = 37104,
    employee = '37',
    surname = 'Петров',
    name = 'Федор',
    otchestvo = 'Алексеевич',
    amount_of_sheets = 1032,
)

MyORM.insert(
    'employees',
    id = 47194,
    employee = '19',
    surname = 'Семенова',
    name = 'Анастасия',
    otchestvo = 'Дмитриевна',
    amount_of_sheets = 1239,
)