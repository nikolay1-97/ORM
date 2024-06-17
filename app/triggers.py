import psycopg2
from config import DB_URL

with psycopg2.connect(DB_URL) as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE OR REPLACE FUNCTION set_defects() RETURNS TRIGGER AS $$\
            BEGIN\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
            return NEW;\
            END;\
        $$ LANGUAGE plpgsql;', (
            'неравномерное прокрашивание',
            'перекраска',
            'процент на 1 кв. метр',
            'наличие царапин',
            'полировка',
            'процент на 1 кв. метр',
            'наличие изгибов',
            'рихтовка',
            'количество на 1 единицу',
        ),
    )
    cursor.execute(
        'CREATE OR REPLACE FUNCTION set_employee() RETURNS TRIGGER AS $$\
            BEGIN\
                NEW.employee = concat(NEW.id, NEW.employee);\
                return NEW;\
            END;\
        $$ LANGUAGE plpgsql;'
    )
    cursor.execute(
        'CREATE TRIGGER set_defects_trigger\
        BEFORE INSERT ON defects FOR EACH ROW\
        EXECUTE PROCEDURE set_defects()'
    )
    cursor.execute(
        'CREATE TRIGGER set_employee_trigger\
        BEFORE INSERT ON employees FOR EACH ROW\
        EXECUTE PROCEDURE set_employee()'
    )
    cursor.execute(
        'CREATE OR REPLACE FUNCTION update_defects() RETURNS TRIGGER AS $$\
            BEGIN\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
                IF NEW.defect = %s THEN\
                    NEW.name_of_works = %s; NEW.measure = %s;\
                END IF;\
            return NEW;\
            END;\
        $$ LANGUAGE plpgsql;', (
            'неравномерное прокрашивание',
            'перекраска',
            'процент на 1 кв. метр',
            'наличие царапин',
            'полировка',
            'процент на 1 кв. метр',
            'наличие изгибов',
            'рихтовка',
            'количество на 1 единицу',
        ),
    )
    cursor.execute(
        'CREATE TRIGGER update_defects_trigger\
        BEFORE UPDATE ON defects FOR EACH ROW\
        EXECUTE PROCEDURE update_defects()'
    )
    cursor.execute(
        'CREATE OR REPLACE FUNCTION update_employee() RETURNS TRIGGER AS $$\
            BEGIN\
                NEW.employee = concat(NEW.id, NEW.employee);\
                return NEW;\
            END;\
        $$ LANGUAGE plpgsql;'
    )
    cursor.execute(
        'CREATE TRIGGER update_employee_trigger\
        BEFORE UPDATE ON employees FOR EACH ROW\
        EXECUTE PROCEDURE update_employee()'
    )
