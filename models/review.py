#!/usr/bin/python3
'''review module'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''review moduule'''

    place_id: str = ""
    user_id: str = ""
    text: str = ""
