import sqlite3
from .ring_option import RingOption


class Metal(RingOption):
    def get_all_metals(self):
        pass

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
