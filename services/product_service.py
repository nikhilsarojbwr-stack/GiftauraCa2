from datetime import datetime, timezone

from models.product import Product
from repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self):

        self.repository = ProductRepository()

    # =====================================================
    # VALIDATE PRODUCT DATA
    # =====================================================

    def _validate_product_data(
        self,
        name,
        description,
        price,
        category
    ):

        if name is None:
            return None

        if description is None:
            description = ""

        if category is None:
            return None

        # -------------------------------------------------
        # Clean text
        # -------------------------------------------------

        name = name.strip()

        description = description.strip()

        category = category.strip()

        # -------------------------------------------------
        # Required fields
        # -------------------------------------------------

        if not name:
            return None

        if not category:
            return None

        # -------------------------------------------------
        # Price validation
        # -------------------------------------------------

        try:

            price = float(price)

        except (TypeError, ValueError):

            return None

        if price < 0:

            return None

        return {
            "name": name,
            "description": description,
            "price": price,
            "category": category
        }

    # =====================================================
    # CREATE PRODUCT
    # =====================================================

    def create_product(
        self,
        name,
        description,
        image,
        price,
        category
    ):

        data = self._validate_product_data(
            name=name,
            description=description,
            price=price,
            category=category
        )

        if data is None:

            return None

        image = (
            image.strip()
            if image
            else ""
        )

        product = Product(
            name=data["name"],
            description=data["description"],
            image=image,
            price=data["price"],
            category=data["category"]
        )

        return self.repository.create_product(
            product.to_dict()
        )

    # =====================================================
    # GET ALL PRODUCTS
    # =====================================================

    def get_all_products(self):

        return self.repository.get_all_products()

    # =====================================================
    # GET PRODUCT BY ID
    # =====================================================

    def get_product_by_id(
        self,
        product_id
    ):

        return self.repository.get_product_by_id(
            product_id
        )

    # =====================================================
    # UPDATE PRODUCT
    # =====================================================

    def update_product(
        self,
        product_id,
        name,
        description,
        image,
        price,
        category
    ):

        data = self._validate_product_data(
            name=name,
            description=description,
            price=price,
            category=category
        )

        if data is None:

            return False

        image = (
            image.strip()
            if image
            else ""
        )

        update_data = {

            "name": data["name"],

            "description": data["description"],

            "image": image,

            "price": data["price"],

            "category": data["category"],

            "updated_at": datetime.now(
                timezone.utc
            )
        }

        return self.repository.update_product(
            product_id,
            update_data
        )

    # =====================================================
    # DELETE PRODUCT
    # =====================================================

    def delete_product(
        self,
        product_id
    ):

        return self.repository.delete_product(
            product_id
        )

    # =====================================================
    # TOTAL PRODUCT COUNT
    # =====================================================

    def count_products(self):

        return self.repository.count_products()

    # =====================================================
    # TOTAL CATEGORY COUNT
    # =====================================================

    def count_categories(self):

        return self.repository.count_categories()

    # =====================================================
    # CATEGORY SUMMARY
    # =====================================================

    def get_category_counts(self):

        return self.repository.get_category_counts()