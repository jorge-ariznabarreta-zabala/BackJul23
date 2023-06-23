#concert = id, id_stage, id_band, id_shift
import mariadb
from flask import jsonify
from gestor_jwt import token_required

DATABASE = {
    'host': 'localhost',
    'user': 'root',
    'password': 'penascal',
    'database': 'Concerts'
}

class Concert:
    def __init__(self, id, id_stage, id_band, id_shift):
        self.id = id
        self.id_stage = id_stage
        self.id_band = id_band
        self.id_shift = id_shift

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
                CREATE TABLE IF NOT EXISTS concerts (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_stage INT,
                    id_band INT,
                    id_shift INT
                )
            ''')

            conn.commit()
            cursor.close()
            conn.close()
            print("Table 'concerts' created successfully.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")

    @classmethod
    #@token_required
    def post_concert(cls, concert):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                INSERT INTO concerts (
                    id_stage,
                    id_band,
                    id_shift
                )
                VALUES (?, ?, ?)
            '''

            cursor.execute(query, (
                concert["id_stage"], concert["id_band"], concert["id_shift"]
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({'message': 'concert created successfully'}), 200
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    #@token_required
    def get_concert_by_id(cls, concert_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT id, id_stage, id_band, id_shift FROM concerts WHERE id = ?"
            cursor.execute(query, (concert_id,))
            result = cursor.fetchone()

            if result:
                concert = {
                    "id": result[0],
                    "id_stage": result[1],
                    "id_band": result[2],
                    "id_shift": result[3]
                }

                return concert
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    #@token_required
    def get_all_concerts(cls):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT * FROM concerts"
            cursor.execute(query)
            results = cursor.fetchall()

            concerts = []
            for result in results:
                concert = {
                    "id": result[0],
                    "id_stage": result[1],
                    "id_band": result[2],
                    "id_shift": result[3]
                }
                print (concerts)
                concerts.append(concert)
            print (concerts)
            return concerts
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    #@token_required
    def put_concert(cls, data, concert_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                UPDATE concerts SET
                id_stage = ?, id_band = ?, id_shift = ?
                WHERE id = ?
            '''

            cursor.execute(query, (
                data['id_stage'], data['id_band'], data['id_shift'], concert_id
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)

    @classmethod
    #@token_required
    def delete_concert(cls, concert_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "DELETE FROM concerts WHERE id = ?"
            cursor.execute(query, (concert_id,))

            conn.commit()
            cursor.close()
            conn.close()
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    #@token_required
    def patch_concert(cls, data, concert_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            update_query = "UPDATE concerts SET "
            params = []

            for key, value in data.items():
                update_query += f"{key} = ?, "
                params.append(value)

            update_query = update_query[:-2]  # Eliminar la coma y el espacio extra al final
            update_query += " WHERE id = ?"
            params.append(concert_id)

            cursor.execute(update_query, tuple(params))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)
