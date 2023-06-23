#stage = id, name, location
import mariadb
from flask import jsonify
from gestor_jwt import token_required

DATABASE = {
    'host': 'localhost',
    'user': 'root',
    'password': 'penascal',
    'database': 'Stages'
}

class Stage:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    @classmethod
    @token_required
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
                CREATE TABLE IF NOT EXISTS stages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name TEXT,
                    location TEXT
                )
            ''')

            conn.commit()
            cursor.close()
            conn.close()
            print("Table 'stages' created successfully.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")

    @classmethod
    @token_required
    def post_stage(cls, stage):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                INSERT INTO stages (
                    name,
                    location
                )
                VALUES (?, ?)
            '''

            cursor.execute(query, (
                stage["name"], stage["location"]
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({'message': 'stage created successfully'}), 200
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def get_stage_by_id(cls, stage_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT id, name, location FROM stages WHERE id = ?"
            cursor.execute(query, (stage_id,))
            result = cursor.fetchone()

            if result:
                stage = {
                    "id": result[0],
                    "name": result[1],
                    "location": result[2]
                }

                return stage
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def get_all_stages(cls):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "SELECT * FROM stages"
            cursor.execute(query)
            results = cursor.fetchall()

            stages = []
            for result in results:
                stage = {
                    "id": result[0],
                    "name": result[1],
                    "location": result[2]
                }

                stages.append(stage)

            return stages
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def put_stage(cls, data, stage_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = '''
                UPDATE stages SET
                name = ?, location = ?
                WHERE id = ?
            '''

            cursor.execute(query, (
                data['name'], data['location'], stage_id
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)

    @classmethod
    @token_required
    def delete_stage(cls, stage_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            query = "DELETE FROM stages WHERE id = ?"
            cursor.execute(query, (stage_id,))

            conn.commit()
            cursor.close()
            conn.close()
        except mariadb.Error as e:
            return jsonify({"Error": str(e)}), 500

    @classmethod
    @token_required
    def patch_stage(cls, data, stage_id):
        try:
            conn = mariadb.connect(
                host=DATABASE['host'],
                user=DATABASE['user'],
                password=DATABASE['password'],
                database=DATABASE['database']
            )
            cursor = conn.cursor()

            update_query = "UPDATE stages SET "
            params = []

            for key, value in data.items():
                update_query += f"{key} = ?, "
                params.append(value)

            update_query = update_query[:-2]  # Eliminar la coma y el espacio extra al final
            update_query += " WHERE id = ?"
            params.append(stage_id)

            cursor.execute(update_query, tuple(params))

            conn.commit()
            cursor.close()
            conn.close()

            return None
        except mariadb.Error as e:
            return str(e)
