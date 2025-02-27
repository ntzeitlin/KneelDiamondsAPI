import json
from .ring_option import RingOption


class Metal(RingOption):
    def get_all_metals(self) -> dict:
        metals_object_list = super().get_all(
            """
            SELECT
                id,
                metal,
                price
            FROM Metals
            """
        )

        metals_list = []
        for row in metals_object_list:
            metals_list.append(dict(row))

        serialized_metals = json.dumps(metals_list) if metals_list else {}
        return serialized_metals

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
