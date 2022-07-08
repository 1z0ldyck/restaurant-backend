from typing import Optional, Union
from pydantic import BaseModel
from loguru import logger
from models.domain.restaurant import RestaurantInterface
from database.app import database
from utils.decorators import generic_repr


class ICreateProduct(BaseModel):
    name: str
    photo: Optional[str]
    price: float
    category: int
    is_promo: bool = False
    description_promo: Optional[Union[str, None]] = None
    price_promo: Optional[Union[float, None]] = None

class IUpdateProduct(ICreateProduct):
    name: Optional[str]
    price: Optional[float]
    category: Optional[int]

class RestaurantRepository(RestaurantInterface):

    session = database.session()

    @generic_repr(phrase='Creating new product')
    def create_product(self, product: ICreateProduct) -> None:
        try:
            with self.session() as session:
                session.add(product)
                session.commit()
                
        except Exception as e:
            logger.error(f'Could not create a product: {str(e)}')

    @generic_repr(phrase='Updating product')
    def update_product(self, product: IUpdateProduct, id_product: int) -> None:
        ...
            
    @generic_repr(phrase='Deleting product')
    def delete_product(self):
        ...
