from models.domain.restaurant import RestaurantInterface
from database.repositories.base import BaseRepository


class RestaurantRepository(RestaurantInterface, BaseRepository):

    def create_product(self):
        ...

    def update_product(self):
        ...

    def delete_product(self):
        ...
