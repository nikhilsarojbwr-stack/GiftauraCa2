from datetime import datetime, timezone


class Product:

    def __init__(
        self,
        name: str,
        description: str,
        image: str,
        price: float,
        category: str,
        created_at=None,
        updated_at=None
    ):

        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.category = category

        self.created_at = (
            created_at
            if created_at
            else datetime.now(timezone.utc)
        )

        self.updated_at = (
            updated_at
            if updated_at
            else datetime.now(timezone.utc)
        )

    def to_dict(self):

        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "price": self.price,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }