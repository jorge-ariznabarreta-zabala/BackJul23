import mariadb
from flask import jsonify
from gestor_jwt import token_required

DATABASE = {
    'host': 'localhost',
    'user': 'root',
    'password': 'penascal',
    'database': 'Concerts'
}

class Band:
    def __init__(self, id, bandname, style, website, email):
        self.id = id
        self.bandname = bandname
        self.style = style
        self.website = website
        self.email = email

    @classmethod
    #@token_required
    def create_table(cls):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bands (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    bandname TEXT,
                    style TEXT,
                    website TEXT,
                    email TEXT
                )
            ''')

            conn.commit()
            cursor.close()
            conn.close()
            print("Table 'bands' created successfully.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")

    @classmethod
    @token_required
    def post_band(cls, band):
        print ('BAND L53 ',band)
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                INSERT INTO bands (
                    bandname,
                    style,
                    website,
                    email
                )
                VALUES (?, ?, ?, ?)
            '''

            cursor.execute(query, (
                band["bandname"], band["style"], band["website"], band["email"]
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({'message': 'band created successfully'}), 200
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def get_band_by_id(cls, band_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT id, bandname, style, website, email FROM bands WHERE id = ?"
            cursor.execute(query, (band_id,))
            result = cursor.fetchone()

            if result:
                band = {
                    "id": result[0],
                    "bandname": result[1],
                    "style": result[2],
                    "website": result[3],
                    "email": result[4]
                }
                print("get_band_by_id @#@#@#", band)
                return band
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def get_all_bands(cls):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT * FROM bands"
            cursor.execute(query)
            results = cursor.fetchall()

            bands = []
            for result in results:
                band = {
                    "id": result[0],
                    "bandname": result[1],
                    "style": result[2],
                    "website": result[3],
                    "email": result[4]
                }

                bands.append(band)

            return bands
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def put_band(cls, data, band_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                UPDATE bands SET
                bandname = ?, style = ?, website = ?, email = ?
                WHERE id = ?
            '''

            cursor.execute(query, (
                data['bandname'], data['style'], data['website'], data['email'], band_id
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)

    @classmethod
    #@token_required
    def delete_band(cls, band_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "DELETE FROM bands WHERE id = ?"
            cursor.execute(query, (band_id,))

            conn.commit()
            cursor.close()
            conn.close()
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def patch_band(cls, data, band_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            update_query = "UPDATE bands SET "
            params = []

            for key, value in data.items():
                update_query += f"{key} = ?, "
                params.append(value)

            update_query = update_query[:-2]  # Eliminar la coma y el espacio extra al final
            update_query += " WHERE id = ?"
            params.append(band_id)

            cursor.execute(update_query, tuple(params))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)
