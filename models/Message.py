class Message:
    __id = None
    from_id = None
    to_id = None
    text = None
    creation_date = None

    def __init__(self):
        self.__id = -1
        self.from_id = 0
        self.to_id = 0
        self.text = ""
        self.creation_date = ""

    @property
    def id(self):
        return self.__id

    @staticmethod
    def load_message_by_id(cursor, message_id):
        sql = "SELECT id, to_id, from_id, text, creation_date FROM messages WHERE id=%s"
        cursor.execute(sql, (message_id,))
        data = cursor.fetchone()
        if data:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.to_id = data[1]
            loaded_message.from_id = data[2]
            loaded_message.text = data[3]
            loaded_message.creation_date = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_messages_for_user(cursor, user_id):
        sql = f"SELECT id, to_id, from_id, text, creation_date FROM messages WHERE to_id={user_id}"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message.__id = row[0]
            loaded_message.to_id = row[1]
            loaded_message.from_id = row[2]
            loaded_message.text = row[3]
            loaded_message.creation_date = row[4]
            ret.append(loaded_message)
        return ret

    def save_to_db(self, cursor):
        sql = """INSERT INTO Messages(to_id, from_id, text, creation_date)
                 VALUES(%s, %s, %s, %s)"""
        values = (self.to_id, self.from_id, self.text, self.creation_date)
        cursor.execute(sql, values)
        return True
