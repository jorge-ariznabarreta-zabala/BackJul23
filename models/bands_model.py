import mariadb
import http

class Band:
    def __init__(self, id, bandname, style, website, email):
        self.id = id
        self.bandname = bandname
        self.style = style
        self.website = website
        self.email = email
        
    @classmethod
    def get_bands(cls):
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
            query = "SELECT * FROM bands"
            cursor.execute(query)
            rows = cursor.fetchall()
            bands = []

            for row in rows:
                bands.append({
                    "id": row[0],
                    "bandname": row[1],
                    "style": row[2],
                    "website": row[3],
                    "email": row[4]
                })

            return bands, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_band(cls, band_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="juan",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        try:
            query = "SELECT * FROM bands WHERE id = ?"
            cursor.execute(query, (band_id,))
            row = cursor.fetchone()

            if row:
                band = {
                    "id": row[0],
                    "bandname": row[1],
                    "style": row[2],
                    "website": row[3],
                    "email": row[4]
                }

                return band, http.HTTPStatus.OK
            else:
                return {'message': '404 Band not found'}, http.HTTPStatus.NOT_FOUND
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def post_band(cls, band):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "INSERT INTO bands (bandname, style, website, email) VALUES (?, ?, ?, ?)"

        try:
            cursor.execute(query, (
                band["bandname"], band["style"], band["website"], band["email"]
            ))

            conn.commit()

            return {'message': 'Band created successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def put_band(cls, data, band_id):
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
            query = "SELECT * FROM bands WHERE id = ?"
            cursor.execute(query, (band_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Band not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE bands SET bandname = ?, style = ?, website = ?, email = ? WHERE id = ?"
            cursor.execute(query, (data['bandname'], data['style'], data['website'], data['email'], band_id))
            conn.commit()

            return {'message': 'Band updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def patch_band(cls, data, band_id):
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
            query = "SELECT * FROM bands WHERE id = ?"
            cursor.execute(query, (band_id,))
            row = cursor.fetchone()

            if not row:
                return {'message': 'Band not found'}, http.HTTPStatus.NOT_FOUND

            query = "UPDATE bands SET "
            params = []

            for key, value in data.items():
                query += key + " = ?, "
                params.append(value)

            query = query[:-2] + " WHERE id = ?"
            params.append(band_id)

            cursor.execute(query, tuple(params))
            conn.commit()

            return {'message': 'Band updated successfully'}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete_band(cls, band_id):
        # Conexión a la base de datos
        conn = mariadb.connect(
            user="root",
            password="penascal",
            host="127.0.0.1",
            port=3306,
            database="concerts"
        )
        cursor = conn.cursor()

        query = "DELETE FROM bands WHERE id = ?"

        try:
            cursor.execute(query, (band_id,))
            if cursor.rowcount == 0:
                return {'message': 'Band not found'}, http.HTTPStatus.NOT_FOUND

            conn.commit()

            return {"message": "Band deleted successfully"}, http.HTTPStatus.OK
        except mariadb.Error as e:
            return {'Error': str(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            cursor.close()
            conn.close()

