#!/usr/bin/python3
'''city module'''
from models.base_model import BaseModel


class City(BaseModel):
    '''city module'''

    state_id: str = ""
    name: str = ""
