from bson import ObjectId
from bson.errors import InvalidId

from database.connection import db


class ProductRepository:

    def __init__(self):

        self.collection = db["products"]

    # =====================================================
    # CREATE PRODUCT
    # =====================================================

    def create_product(self, product_data):

        result = self.collection.insert_one(
            product_data
        )

        return result.inserted_id

    # =====================================================
    # GET ALL PRODUCTS
    # =====================================================

    def get_all_products(self):

        return list(
            self.collection.find().sort(
                "created_at",
                -1
            )
        )

    # =====================================================
    # GET PRODUCT BY ID
    # =====================================================

    def get_product_by_id(
        self,
        product_id
    ):

        try:

            object_id = ObjectId(product_id)

        except (InvalidId, TypeError):

            return None

        return self.collection.find_one({
            "_id": object_id
        })

    # =====================================================
    # UPDATE PRODUCT
    # =====================================================

    def update_product(
        self,
        product_id,
        product_data
    ):

        try:

            object_id = ObjectId(product_id)

        except (InvalidId, TypeError):

            return False

        result = self.collection.update_one(

            {
                "_id": object_id
            },

            {
                "$set": product_data
            }
        )

        # -------------------------------------------------
        # matched_count means the product existed.
        #
        # modified_count can be 0 when the submitted
        # values are exactly the same as existing values.
        # -------------------------------------------------

        return result.matched_count > 0

    # =====================================================
    # DELETE PRODUCT
    # =====================================================

    def delete_product(
        self,
        product_id
    ):

        try:

            object_id = ObjectId(product_id)

        except (InvalidId, TypeError):

            return False

        result = self.collection.delete_one({
            "_id": object_id
        })

        return result.deleted_count > 0

    # =====================================================
    # TOTAL PRODUCT COUNT
    # =====================================================

    def count_products(self):

        return self.collection.count_documents({})

    # =====================================================
    # CATEGORY COUNTS
    # =====================================================

    def get_category_counts(self):

        pipeline = [

            {
                "$match": {
                    "category": {
                        "$exists": True,
                        "$ne": ""
                    }
                }
            },

            {
                "$group": {
                    "_id": "$category",
                    "count": {
                        "$sum": 1
                    }
                }
            },

            {
                "$sort": {
                    "count": -1
                }
            }
        ]

        return list(
            self.collection.aggregate(
                pipeline
            )
        )

    # =====================================================
    # TOTAL UNIQUE CATEGORY COUNT
    # =====================================================

    def count_categories(self):

        return len(
            self.get_category_counts()
        )