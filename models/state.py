#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""


class State(BaseModel):
    @property
    def cities(self):
    """Return the list of City objects from storage linked to the current State."""
        from models import storage
        cities_list = []
        for city in list(storage.all(City).values()):
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

