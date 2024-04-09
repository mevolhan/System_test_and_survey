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
        self.connect_myBD()
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

    def save_answers_options(self, answers_options, number_right_answers, right_answer):
        self.connect_myBD()
        try:
            with self.connection.cursor() as cursor:

                self.insert_query = "INSERT INTO `answers` (answers_options, number_right_answers, right_answer) " \
                                               f"VALUES (%s, %s, %s);"

                cursor.execute(self.insert_query, (answers_options, number_right_answers, right_answer))
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

    def get_answers_id(self, answers_options, number_right_answers, right_answer):
        self.connect_myBD()
        try:
            with self.connection.cursor() as cursor:

                self.insert_query = "SELECT id_answers" \
                                    "FROM testing_system.answers" \
                                    f"WHERE JSON_CONTAINS(`answers_options`, {answers_options})" \
                                    f"AND JSON_CONTAINS(`number_right_answers`, {number_right_answers})" \
                                    f"AND `right_answer` = {right_answer};"

                cursor.execute(self.insert_query, (answers_options, number_right_answers, right_answer))
                id_answer = cursor.fetchone()


        except Exception as e:
            print("Failed to:", e)
            print("Connection closed ...")
            return None

        else:
            self.connection.close()
            print("Successfully inserted")
            print("Connection closed ...")
            return id_answer


    def save_one_question(self, tittle, is_closed, name_question, answers_options, number_right_answers, right_answer):
        self.connect_myBD()
        self.save_answers_options(name_question, answers_options, number_right_answers)
        id_answer = self.get_answers_id(name_question, answers_options, number_right_answers)

        try:
            with self.connection.cursor() as cursor:

                self.insert_query_title_test = "INSERT INTO `test_questions` (is_closed, name_queshtion) " \
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