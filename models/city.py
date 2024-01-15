#!/usr/bin/python3
''' City class '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' Represents a City

    Attributes:
        state_id (str): State id
        name (str): Name of the city
    '''
    state_id = ""
    name = ""
