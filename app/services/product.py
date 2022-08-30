from app.core import repository
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductServices(repository.Base[Product, ProductCreate, ProductUpdate]):
    # Declare model specific CRUD operation methods.
    pass


product = ProductServices(Product)
