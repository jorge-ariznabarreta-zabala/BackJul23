#shift = id, day, hour
import mariadb
import http

class Shift:
    def __init__(self, id, day, hour):
        self.id = id
        self.day = day
        self.hour = hour

    import mariadb

class Shift:
    def __init__(self, id, day, hour):
        self.id = id
        self.day = day
        self.hour = hour
    
    @classmethod
    def create_table(cls):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="localhost",
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS shifts (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    day INTEGER NOT NULL,
                    hour INTEGER NOT NULL
                )
            ''')
            conn.commit()
        except mariadb.Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            conn.close()

        
    @classmethod
    def get_shifts(cls):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM shifts"
            cursor.execute(query)
            rows = cursor.fetchall()
            shifts = []

            for row in rows:
                shifts.append({
                    "id": row[0],
                    "day": row[1],
                    "hour": row[2]
                })

            return shifts, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_shift(cls, shift_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM shifts WHERE id = ?"
            cursor.execute(query, (shift_id,))
            row = cursor.fetchone()

            if row:
                shift = {
                    "id": row[0],
                    "day": row[1],
                    "hour": row[2]
                }

                return shift, http.HTTPStatus.OK
            else:
                return {'message': '404 Shift not found'}, http.HTTPStatus.NOT_FOUND
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def post_shift(cls, shift):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "INSERT INTO shifts (day, hour) VALUES (?, ?)"

        try:
            cursor.execute(query, (
                shift["day"], shift["hour"]
            ))

            conn.commit()

            return {'message': 'Shift created successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def put_shift(cls, data, shift_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM shifts WHERE id = ?"
            cursor.execute(query, (shift_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Shift not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE shifts SET day = ?, hour = ? WHERE id = ?"
            cursor.execute(query, (data['day'], data['hour'], shift_id))
            conn.commit()

            return {'message': 'Shift updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def patch_shift(cls, data, shift_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM shifts WHERE id = ?"
            cursor.execute(query, (shift_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Shift not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE shifts SET "
            params = []

            for key, value in data.items():
                query += key + " = ?, "
                params.append(value)

            query = query[:-2] + " WHERE id = ?"
            params.append(shift_id)

            cursor.execute(query, tuple(params))
            conn.commit()

            return {'message': 'Shift updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete_shift(cls, shift_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "DELETE FROM shifts WHERE id = ?"

        try:
            cursor.execute(query, (shift_id,))
            if cursor.rowcount == 0:
                return {'message': 'Shift not found'}, http.HTTPStatus.NOT_FOUND

            conn.commit()

            return {"message": "Shift deleted successfully"}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()
#Crea la tabla si no existe
Shift.create_table()