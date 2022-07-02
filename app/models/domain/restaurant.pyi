from abc import ABC, abstractmethod


class RestaurantInterface(ABC):

    @abstractmethod
    def create_product(self) -> None: ...

    @abstractmethod
    def update_product(self) -> None: ...

    def delete_product(self, id: int) -> None: ...
