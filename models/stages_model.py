import mariadb
import http

class Stage:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
        
    @classmethod
    def get_stages(cls):
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
            query = "SELECT * FROM stages"
            cursor.execute(query)
            rows = cursor.fetchall()
            stages = []

            for row in rows:
                stage = {
                    "id": row[0],
                    "name": row[1],
                    "location": row[2]
                }
                stages.append(stage)

            return stages, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_stage(cls, stage_id):
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
            query = "SELECT * FROM stages WHERE id = ?"
            cursor.execute(query, (stage_id,))
            row = cursor.fetchone()

            if row:
                stage = {
                    "id": row[0],
                    "name": row[1],
                    "location": row[2]
                }

                return stage, http.HTTPStatus.OK
            else:
                return {'message': '404 Stage not found'}, http.HTTPStatus.NOT_FOUND
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def post_stage(cls, stage):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "INSERT INTO stages (name, location) VALUES (?, ?)"

        try:
            cursor.execute(query, (
                stage["name"], stage["location"]
            ))

            conn.commit()

            return {'message': 'Stage created successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def put_stage(cls, data, stage_id):
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
            query = "SELECT * FROM stages WHERE id = ?"
            cursor.execute(query, (stage_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Stage not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE stages SET name = ?, location = ? WHERE id = ?"
            cursor.execute(query, (data['name'], data['location'], stage_id))
            conn.commit()

            return {'message': 'Stage updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def patch_stage(cls, data, stage_id):
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
            query = "SELECT * FROM stages WHERE id = ?"
            cursor.execute(query, (stage_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Stage not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE stages SET "
            params = []

            for key, value in data.items():
                query += key + " = ?, "
                params.append(value)

            query = query[:-2] + " WHERE id = ?"
            params.append(stage_id)

            cursor.execute(query, tuple(params))
            conn.commit()

            return {'message': 'Stage updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete_stage(cls, stage_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "DELETE FROM stages WHERE id = ?"

        try:
            cursor.execute(query, (stage_id,))
            if cursor.rowcount == 0:
                return {'message': 'Stage not found'}, http.HTTPStatus.NOT_FOUND

            conn.commit()

            return {"message": "Stage deleted successfully"}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()
