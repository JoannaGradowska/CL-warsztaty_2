from psycopg2 import connect, OperationalError
from local_settings import user, password, host, database


def connecting():
    try:
        cnx = connect(user=user, password=password, host=host, database=database)
    except OperationalError as e:
        return f"Nie udało się ustanowić połączenia ({e})"
    else:
        cnx.autocommit = True
        cursor = cnx.cursor()
        return cursor
