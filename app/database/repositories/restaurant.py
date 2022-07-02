from models.domain.restaurant import RestaurantInterface


def init_app(app):
    app.repositories.restaurant = RestaurantRepository(app)


class RestaurantRepository(RestaurantInterface):

    def __init__(self, app):
        self.app = app

    def create_product(self):
        ...

    def update_product(self):
        ...

    def delete_product(self):
        ...
