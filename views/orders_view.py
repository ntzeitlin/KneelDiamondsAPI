import sqlite3
import json


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT 
                    orders.id,
                    metals.id,
                    metals.metal,
                    sizes.id,
                    sizes.size,
                    styles.id,
                    styles.style

                FROM Orders orders
                JOIN Metals metals
                    ON metals.id = orders.metal_id
                JOIN Sizes sizes
                    ON sizes.id = orders.size_id
                JOIN Styles styles
                    ON styles.id = orders.style_id
            """
        )
        query_results = db_cursor.fetchall()
        orders = []
        for row in query_results:
            orders.append(dict(row))

        serialized_orders = json.dumps(orders)
    return serialized_orders


def get_single_ship(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                orders.id,
                metals.id,
                metals.metal,
                sizes.id,
                sizes.size,
                styles.id,
                styles.style

                FROM Orders orders
                JOIN Metals metals
                    ON metals.id = orders.metal_id
                JOIN Sizes sizes
                    ON sizes.id = orders.size_id
                JOIN Styles styles
                    ON styles.id = orders.style_id
                WHERE orders.id = ?
                    """,
            (pk,),
        )
        query_results = db_cursor.fetchone()
        dictionary_version_of_object = dict(query_results) if query_results else {}

        # Serialize Python list to JSON encoded string
        serialized_order = json.dumps(dictionary_version_of_object)
    return serialized_order
