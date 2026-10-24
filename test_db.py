from datetime import datetime

import psycopg


def test_database_connection():
    with psycopg.connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW()")
            row = cursor.fetchone()


    assert row is not None, "Запрос не вернул строку"
    assert isinstance(row[0], datetime), (
        f"Ожидалась дата и время, получено: {type(row[0]).__name__}"
    )
