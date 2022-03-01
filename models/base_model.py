#!/usr/bin/python3
import uuid
from datetime import datetime
import models


"""
Base class for all models that will contain id, created_at
and updated_at attributes. Save() and to_json() methods
"""


class BaseModel:
    """
    Instantiation of the class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """ Initializing the variables"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = (uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Method to return string representation"""
        return ("[{}] ({}) {}".formart(str(type(self).__name__),
                                       self.id, str(self.__dict__)))

    def __repr__(self):
        """Method that returns the official representations of string"""
        cls = self.__class__.__name__
        string = ("[{}] [()] {}".format(cls, self.id, self.__dict__))
        return (string)

    def save(self):
        """ Method to updaate attrb updated_at"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method to return a dict containing all key/value of
        __dict__ instance"""
        dic = dict(**self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
