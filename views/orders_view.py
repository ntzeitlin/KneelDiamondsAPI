import sqlite3
import json


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
               SELECT
                orders.id ordersId,
                orders.metal_id,
                orders.size_id,
                orders.style_id,
                metals.id metalId,
                metals.metal metalName,
                metals.price metal_price,
                sizes.id,
                sizes.size sizeName,
                sizes.price size_price,
                styles.id,
                styles.style styleName,
                styles.price style_price

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
            metal = {
                "metal": row["metalName"],
                "price": row["metal_price"],
            }
            size = {"size": row["sizeName"], "price": row["size_price"]}
            style = {"style": row["styleName"], "price": row["style_price"]}
            order = {
                "id": row["ordersId"],
                "metal_id": row["metal_id"],
                "metal": metal,
                "style_id": row["style_id"],
                "style": style,
                "size_id": row["size_id"],
                "size": size,
            }
            orders.append(order)

        serialized_orders = json.dumps(orders) if orders else {}
    return serialized_orders


def get_single_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                orders.id,
                orders.metal_id,
                orders.size_id,
                orders.style_id,
                metals.id,
                metals.metal,
                metals.price metal_price,
                sizes.id,
                sizes.size,
                sizes.price size_price,
                styles.id,
                styles.style,
                styles.price style_price

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


def create_order(order_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Orders
            (metal_id, size_id, style_id)
            VALUES (?, ?, ?)
            """,
            (order_data["metal_id"], order_data["size_id"], order_data["style_id"]),
        )

        rows_affected = db_cursor.rowcount

    return True if rows_affected > 0 else False


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        # SQL Delete Query
        db_cursor.execute(
            """
            DELETE
            FROM Orders
            WHERE id = ?
            """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount
    return True if number_of_rows_deleted > 0 else False
