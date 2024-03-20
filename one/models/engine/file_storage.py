#!/usr/bin/python3
"""defines a class to storage file for hbnb clone"""
import json


class FileStorage:
    """managing storage of hbnb in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of models in storage but when not specified,
	returns a dictionary
        """
        if cls is not None:
            new_obj_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    new_obj_dict[key] = value
            return new_obj_dict

        return FileStorage.__objects

    def new(self, obj):
        """Adds objects to be stored in a dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary in a file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is not None:
            # get the key for this obj class name.id
            key = obj.__class__.__name__ + '.' + obj.id
            del self.__objects[key]
