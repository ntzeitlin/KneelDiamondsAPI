from .ring_option import RingOption


class Style(RingOption):
    def get_all(self) -> list:
        return super().get_all(
            """
            SELECT
                id,
                style,
                price
            FROM Styles
            """
        )

    def get_one(self, id) -> str:
        return super().get_one(
            primary_key=id,
            sql_command="""
            SELECT
                id,
                style,
                price
            FROM Styles
            WHERE id = ?
            """,
        )

    def update_one(self, id, style_data) -> bool:
        return super().update_one(
            """
            UPDATE Styles
            SET
                style = ?,
                price = ?
            WHERE id = ?
        """,
            (style_data["style"], style_data["price"], id),
        )

    def create_one(self, style_data):
        return super().create_one(
            """
            INSERT INTO Styles
            (style, price)
            VALUES (?, ?)
            """,
            (style_data["style"], style_data["price"]),
        )

    def delete_one(self, id):
        return super().delete_one("Styles", id)
