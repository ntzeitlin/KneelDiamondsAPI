from .ring_option import RingOption


class Size(RingOption):
    def get_all(self) -> list:
        return super().get_all(
            """
            SELECT
                id,
                size,
                price
            FROM Sizes
            """
        )

    def get_one(self, id) -> str:
        return super().get_one(
            primary_key=id,
            sql_command="""
            SELECT
                id,
                size,
                price
            FROM Sizes
            WHERE id = ?
            """,
        )

    def update_one(self, id, size_data) -> bool:
        return super().update_one(
            """
            UPDATE Sizes
            SET
                size = ?,
                price = ?
            WHERE id = ?
        """,
            (size_data["size"], size_data["price"], id),
        )

    def create_one(self, size_data):
        return super().create_one(
            """
            INSERT INTO Sizes
            (size, price)
            VALUES (?, ?)
            """,
            (size_data["size"], size_data["price"]),
        )

    def delete_one(self, id):
        return super().delete_one("Sizes", id)
