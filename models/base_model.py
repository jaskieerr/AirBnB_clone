#!/usr/bin/python3
'''
project BaseModel
'''
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    '''initin Basemodel class'''
    def __init__(self, *args, **kwargs):
        '''ana la gaya olak irga3'''

        if kwargs is not None and len(kwargs) != 0:
            for kw in kwargs:
                if kw == '__class__':
                    continue
                elif kw in ['created_at', 'updated_at']:
                    setattr(self, kw, datetime.fromisoformat(kwargs[kw]))
                else:
                    setattr(self, kw, kwargs[kw])

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage.new(self)

    def __str__(self) -> str:
        '''returns class readable represnetation'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates public instance attribut with current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns class dict representation'''
        dic_rep: dict = {}
        dic_rep.update(self.__dict__)
        dic_rep['__class__'] = self.__class__.__name__
        dic_rep['created_at'] = self.created_at.isoformat()
        dic_rep['updated_at'] = self.updated_at.isoformat()
        return dic_rep
