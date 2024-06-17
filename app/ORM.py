import psycopg2

from config import DB_URL


class MyORM():
    """ORM."""

    DB_URL = DB_URL

    @classmethod
    def get_field_names(cls, data: dict):
        """Возвращает строку из имен полей таблицы,
        разделенных запятыми.

        Parameters
        ----------
        data : dict
            Словарь с данными для заполнения таблиц.
        """
        lst_name = [str(name) for name in data.keys()]
        field_names = ', '.join(lst_name)
        return field_names

    @classmethod
    def get_template(cls, data: dict):
        """Возвращает шаблон для запросов(%s) в виде строки.
        
        Parameters
        ----------
        data : dict
            Словарь с данными для заполнения таблиц.
        """
        template = '%s,'
        for i in range(len(data)-1):
            template += ' %s,'

        template = template[:-1]
        return template
    
    @classmethod
    def get_template_for_update(cls, data: dict):
        """Возвращает шаблон для обновления в виде строки.

        Parameters
        ----------
        data : dict
            Словарь с данными для обновления.
        """
        return ','.join([f'{key} = %s' for key, value in data.items()])

    @classmethod
    def insert(cls, table_name: str, **kwargs):
        """Производит вставку данных в таблицы базы данных.

        Parameters
        ----------
        table_name : str
            Имя таблицы базы данных.
        
        kwargs: dict
            Словарь с данными для заполнения таблиц.
        """
        conn = psycopg2.connect(cls.DB_URL)
        cursor = conn.cursor()
        template = cls.get_template(kwargs)
        field_names = cls.get_field_names(kwargs)
        try:
            cursor.execute(
                f'INSERT INTO {table_name}\
                ({field_names})\
                VALUES ({template})',
                tuple(kwargs.values()),
            )
            conn.commit()
        except Exception as some_ex:
            conn.rollback()
            print(some_ex)
        finally:
            conn.close()

    @classmethod
    def update(
        cls,
        table_name: str,
        field_name: str = None,
        field_value = None,
        **kwargs,
    ):
        """Производит обновление данных в таблицах базы данных.

        Parameters
        ----------
        table_name: str
            Имя таблицы базы данных.

        field_name: str
            Имя целевого поля.

        field_value: str
            Значение целевого поля.
        
        kwargs: dict
            Словарь с данными для заполнения таблиц.
        """
        conn = psycopg2.connect(cls.DB_URL)
        cursor = conn.cursor()
        template = cls.get_template_for_update(kwargs)
        try:
            cursor.execute(
                f'UPDATE {table_name} SET {template}\
                  WHERE {field_name} = {field_value}',
                tuple(kwargs.values())
            )
            conn.commit()
        except Exception as some_ex:
            conn.rollback()
            print(some_ex)
        finally:
            conn.close()

    @classmethod
    def select(
        cls,
        table_name: str,
        field_name: str = None,
        field_value=None,
    ):
        """Возвращает записи из таблиц базы данных.

        Parameters
        ----------

        table_name: str
            Имя таблицы базы данных.
        field_name: str
            Имя целевого поля.

        field_value: str
            Значение целевого поля.
        """
        conn = psycopg2.connect(cls.DB_URL)
        cursor = conn.cursor()
        try:
            if not field_name:
                cursor.execute(f'SELECT * FROM {table_name}')
                return cursor.fetchall()
            else:
                cursor.execute(
                    f'SELECT * FROM {table_name} WHERE {field_name} = %s',
                    (field_value,),
                )
                return cursor.fetchone()
        except Exception as some_ex:
            print(some_ex)
        finally:
            conn.close()

    @classmethod
    def delete(
        cls,
        table_name: str,
        field_name: str = None,
        field_value = None,
    ):
        """Удаляет записи из таблиц базы данных.
        
        Parameters
        ----------

        table_name: str
            Имя таблицы базы данных.

        field_name: str
            Имя целевого поля.

        field_value: str
            Значение целевого поля.
        """
        conn = psycopg2.connect(cls.DB_URL)
        cursor = conn.cursor()
        try:
            if field_name:
                cursor.execute(
                    f'DELETE FROM {table_name} WHERE {field_name} = {field_value}'
                )
                conn.commit()
            else:
                cursor.execute(f'DELETE FROM {table_name}')
                conn.commit()

        except Exception as some_ex:
            conn.rollback()
            print(some_ex)
        finally:
            conn.close()
