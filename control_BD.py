import pymysql
class MyDB():
    def __init__(self, host='localhost', port=3036, user='user', password='mypassword', dbname='mydb'):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connect_myBD()

    def connect_myBD(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.dbname,
                cursorclass=pymysql.cursors.DictCursor
                )
            print("Connection successful ...")
        except Exception as e:
            print("Connection error:", e)

    def save_title_quiz(self, title, description, type):
        try:
            with self.connection.cursor() as cursor:

                self.insert_query_title_test = "INSERT INTO `quizzes_all` (title, description, type) " \
                                          f"VALUES (%s, %s, %s);"

                cursor.execute(self.insert_query_title_test, (title, description, type))
                self.connection.commit()


        except Exception as e:
            print("Failed to:", e)
            print("Connection closed ...")
            return False

        else:
            self.connection.close()
            print("Successfully inserted")
            print("Connection closed ...")
            return True