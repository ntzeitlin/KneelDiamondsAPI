import sqlite3
import json


class RingOption:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    # NOTE: Functioning
    def get_all(self, sql_command) -> list:
        with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(sql_command)

            # retrieve results
            query_results = db_cursor.fetchall()

            results_list = []
            for row in query_results:
                results_list.append(dict(row))

            serialized_results = json.dumps(results_list) if results_list else {}
        return serialized_results

    # NOTE: Not Tested
    def get_one(self, primary_key, sql_command) -> str:
        with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(
                sql_command,
                (primary_key,),
            )

            query_results = db_cursor.fetchone()
            dictionary_version_of_object = dict(query_results) if query_results else {}

            serialized_return = json.dumps(dictionary_version_of_object)
        return serialized_return

    # NOTE: Not Tested
    def create_one(self, body_data, sql_command) -> bool:
        with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(body_data, sql_command)

            rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False

    # NOTE: Functioning!
    def update_one(self, sql_command, values):
        with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(sql_command, values)

            rows_affected = db_cursor.rowcount
        return True if rows_affected > 0 else False

    # NOTE: Not Tested
    def delete_one(self, primary_key, table_name) -> bool:
        with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
            DELETE
            FROM table_name = ?
            WHERE id = ?
            """,
                (
                    table_name,
                    primary_key,
                ),
            )
            number_of_rows_deleted = db_cursor.rowcount
        return True if number_of_rows_deleted > 0 else False
