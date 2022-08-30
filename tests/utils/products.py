from faker import Faker
from sqlalchemy.orm import Session

from app import models, services
from app.schemas.product import ProductCreate

fake = Faker()


def create_random_product(db: Session) -> models.Product:
    name = fake.first_name()
    price = fake.random_int()
    product_in = ProductCreate(name=name, price=price)
    return services.product.create(db, obj_in=product_in)
