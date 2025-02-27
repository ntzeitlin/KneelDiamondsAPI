from .ring_option import RingOption


class Metal(RingOption):
    def get_all(self) -> list:
        return super().get_all(
            """
            SELECT
                id,
                metal,
                price
            FROM Metals
            """
        )

    def get_one(self, id) -> str:
        return super().get_one(
            primary_key=id,
            sql_command="""
            SELECT
                id,
                metal,
                price
            FROM Metals
            WHERE id = ?
            """,
        )

    def update_one(self, id, metal_data) -> bool:
        return super().update_one(
            """
            UPDATE Metals
            SET
                metal = ?,
                price = ?
            WHERE id = ?
        """,
            (metal_data["metal"], metal_data["price"], id),
        )

    def create_one(self, metal_data):
        return super().create_one(
            """
            INSERT INTO Metals
            (metal, price)
            VALUES (?, ?)
            """,
            (metal_data["metal"], metal_data["price"]),
        )

    def delete_one(self, id):
        return super().delete_one("Metals", id)
