from .ring_option import RingOption


class Metal(RingOption):
    def get_all_metals(self) -> list:
        return super().get_all(
            """
            SELECT
                id,
                metal,
                price
            FROM Metals
            """
        )

    def get_a_metal(self, id) -> str:
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

    def update_metal(self, id, metal_data) -> bool:
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
