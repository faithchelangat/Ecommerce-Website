from django.core.management.base import BaseCommand
from storefront.models import Category, Product


class Command(BaseCommand):
    help = "Load ecommerce categories and products"

    def handle(self, *args, **kwargs):

        categories = {
            1: "Cell Phone",
            2: "Novels",
            3: "Beauty Products",
        }

        for category_id, name in categories.items():
            Category.objects.update_or_create(
                id=category_id,
                defaults={"name": name},
            )

        products = [
            {
                "id": 1,
                "name": "Iphone",
                "price": "999.99",
                "category_id": 1,
                "description": "This is an Iphone",
                "image": "uploads/product/iphone.jpeg",
                "on_sale": True,
                "sale_price": "888.00",
            },
            {
                "id": 2,
                "name": "Android",
                "price": "899.99",
                "category_id": 1,
                "description": "This is an android",
                "image": "uploads/product/android.jpeg",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 3,
                "name": "Lotion",
                "price": "29.99",
                "category_id": 3,
                "description": "This is a body Lotion",
                "image": "uploads/product/path_and_body_works.webp",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 4,
                "name": "Jelly",
                "price": "100.00",
                "category_id": 3,
                "description": "Body moisturiser",
                "image": "uploads/product/cerave_3k.webp",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 5,
                "name": "Lip Stick",
                "price": "200.00",
                "category_id": 3,
                "description": "This is a lipstick",
                "image": "uploads/product/img1.png",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 6,
                "name": "Beauty Blender",
                "price": "300.00",
                "category_id": 3,
                "description": "This is a beauty blender",
                "image": "uploads/product/images.jpg",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 7,
                "name": "Skin Care",
                "price": "1000.22",
                "category_id": 3,
                "description": "Skin care product",
                "image": "uploads/product/prod1.webp",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 8,
                "name": "Alchemist by Paulo Choelho",
                "price": "200.12",
                "category_id": 2,
                "description": "This magical story of Santiago a Shepherd boy who dreams of travelling the world to seek the most wonderful treasure known to man",
                "image": "uploads/product/Alchemist.jpeg",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 9,
                "name": "Make It Stick",
                "price": "300.00",
                "category_id": 2,
                "description": "A novel",
                "image": "uploads/product/Make_it_stick.png",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 10,
                "name": "Atomic habits",
                "price": "400.00",
                "category_id": 2,
                "description": None,
                "image": "uploads/product/Atomic_habits.jpeg",
                "on_sale": True,
                "sale_price": "350.00",
            },
            {
                "id": 11,
                "name": "Elon Musk by Walter",
                "price": "500.55",
                "category_id": 2,
                "description": None,
                "image": "uploads/product/Elon_Musk.jpeg",
                "on_sale": False,
                "sale_price": "0.00",
            },
            {
                "id": 12,
                "name": "How to know a person",
                "price": "150.00",
                "category_id": 2,
                "description": None,
                "image": "uploads/product/How_to_know_a_person.jpeg",
                "on_sale": False,
                "sale_price": "0.00",
            },
        ]

        for product in products:
            product_id = product.pop("id")

            Product.objects.update_or_create(
                id=product_id,
                defaults=product,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Ecommerce categories and products loaded successfully."
            )
        )