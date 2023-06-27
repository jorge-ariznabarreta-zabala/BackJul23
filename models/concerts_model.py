import mariadb
import http

class Concert:
    def __init__(self, id, id_stage, id_band, id_shift):
        self.id = id
        self.id_stage = id_stage
        self.id_band = id_band
        self.id_shift = id_shift

    @classmethod
    def get_concerts(cls):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM concerts"
            cursor.execute(query)
            rows = cursor.fetchall()
            concerts = []

            for row in rows:
                concerts.append({
                    "id": row[0],
                    "id_stage": row[1],
                    "id_band": row[2],
                    "id_shift": row[3]
                })

            return concerts, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_concert(cls, concert_id):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM concerts WHERE id = ?"
            cursor.execute(query, (concert_id,))
            row = cursor.fetchone()

    
            if row:
                concert={
                    "id": row[0],
                    "id_stage": row[1],
                    "id_band": row[2],
                    "id_shift": row[3]
                }

                return concert, http.HTTPStatus.OK
            else:
                return {'message': '404 Concert not found'}, http.HTTPStatus.NOT_FOUND
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def post_concert(cls, concert):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()
        print ("L76 @#@@#@#@#@# ", concert)

        query = "INSERT INTO concerts (id_stage, id_band, id_shift) VALUES (?, ?, ?)"

        try:
            cursor.execute(query, (
                concert["id_stage"], concert["id_band"], concert["id_shift"]
            ))

            conn.commit()

            return {'message': 'Concert created successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def put_concert(cls, data, concert_id):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM concerts WHERE id = ?"
            cursor.execute(query, (concert_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Concert not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE concerts SET id_stage = ?, id_band = ?, id_shift = ? WHERE id = ?"
            cursor.execute(query, (data['id_stage'], data['id_band'], data['id_shift'], concert_id))
            conn.commit()

            return {'message': 'Concert updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def patch_concert(cls, data, concert_id):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM concerts WHERE id = ?"
            cursor.execute(query, (concert_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Concert not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE concerts SET "
            params = []

            for key, value in data.items():
                query += key + " = ?, "
                params.append(value)

            query = query[:-2] + " WHERE id = ?"
            params.append(concert_id)

            cursor.execute(query, tuple(params))
            conn.commit()

            return {'message': 'Concert updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete_concert(cls, concert_id):
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "DELETE FROM concerts WHERE id = ?"

        try:
            cursor.execute(query, (concert_id,))
            if cursor.rowcount == 0:
                return {'message': 'Concert not found'}, http.HTTPStatus.NOT_FOUND

            conn.commit()

            return {"message": "Concert deleted successfully"}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()
