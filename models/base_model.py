#!/usr/bin/python3
'''
project BaseModel
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:

    '''initin Basemodel class'''
    def __init__(self):
        '''ana la gaya olak irga3'''

        self.id = str(uuid4())
        self.created_at = datetime.now
        self.updated_at = self.created_at

    def __str__(self) -> str:
        '''returns class readable represnetation'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates public instance attribut with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns class dict representation'''
        result: dict = {}
        result.update(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
