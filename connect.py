from psycopg2 import connect, OperationalError
from models.User import User
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


cur = connecting()
# example = User()
# example.username = "example_name"
# example.email = "example@mail.pl"
# example.set_password("example_password")
# example.save_to_db(connecting())
#
# k = User.load_user_by_id(connecting(), 6)
# print(k)
# print("username = ",k.username,"email = ", k.email,"password = ", k.hashed_password,"id = ", k.id)

# t = User.load_all_users(cur)
# print(t)
# print(t[0].username)

# a = User.load_user_by_id(cur, 3)
# print(a)
# a.username = "Nietykalny"
# a.save_to_db(cur)
