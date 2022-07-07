from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, Boolean
from sqlalchemy.orm import relationship

from models import Model

class Restaurant(Model):

      __tablename__ = 'restaurants'

      id = Column(Integer, primary_key=True, nullable=False)
      photo = Column(Text)
      address = Column(String(255), nullable=False)
      weekday_time = relationship("WeekdayTimeRestaurant")
      weekend_time = relationship("WeekendTimeRestaurant")


class WeekdayTimeRestaurant(Model):
      __tablename__ = 'weekday_time_restaurant'

      id = Column(Integer, primary_key=True, nullable=False)
      hour_open = Column(String(5), nullable=False)
      hour_close = Column(String(5), nullable=False)
      restaurant_id = Column(Integer, ForeignKey('restaurants.id'))


class WeekendTimeRestaurant(Model):
      __tablename__ = 'weekend_time_restaurant'

      id = Column(Integer, primary_key=True, nullable=False)
      hour_open = Column(String(5), nullable=False)
      hour_close = Column(String(5), nullable=False)
      restaurant_id = Column(Integer, ForeignKey('restaurants.id'))


class RestaurantProductCategory(Model):
    __tablename__ = 'product_category_restaurant'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)


class RestaurantProducts(Model):
    __tablename__ = 'products_restaurant'
    
    id = Column(Integer, primary_key=True)
    photo = Column(Text)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(Integer, ForeignKey("product_category_restaurant.id"))
    is_promo = Column(Boolean, default=False)
    description_promo = Column(String(255), nullable=False)
    price_promo = Column(Float, nullable=False)


tables = [Restaurant, WeekendTimeRestaurant, WeekdayTimeRestaurant, RestaurantProductCategory, RestaurantProducts]