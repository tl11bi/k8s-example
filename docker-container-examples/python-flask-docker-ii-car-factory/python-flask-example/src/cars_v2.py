import json
import os
import pymongo

class CarsStore(object):
    """
    This class represents a car and provides methods for creating, reading, updating, and deleting cars.
    """

    def __init__(self):
        """
        Constructor for the cars class.
        """
        mongodb_client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
        # set client user name and password
        # mongodb_client = pymongo.MongoClient("mongodb://username:password@localhost:27017/")
        # create database if not exists
        mongodb_client.list_database_names()
        self.cars_db = mongodb_client["carsFactory"]
        # create collection if not exists
        self.cars_collection = self.cars_db["cars"]


    def create_car(self, id, make, module, year):
        """
        This method creates a new car and adds it to the cars dictionary.
        example of car:
        {
            "_id": 1,
            "make": "Toyota",
            "module": "Corolla",
            "year": 2015
        }
        """
        new_car = {
            '_id': id,
            'make': make,
            'module': module,
            'year': year
        }
        self.cars_collection.insert_one(new_car)
        return json.dumps(new_car)

    def get_car(self, id):
        """
        This method retrieves a car from the cars dictionary.
        """
        return json.dumps(self.cars_collection.find_one({'_id': id}))

    def update_car(self, id, make, module, year):
        """
        This method updates an existing car in the cars dictionary.
        """
        return self.cars_collection.update_one({'_id': id}, {'$set': {'make': make, 'module': module, 'year': year}})

    def delete_car(self, id):
        """
        This method deletes a car from the cars dictionary.
        """
        self.cars_collection.delete_one({'_id': id})
        return json.dumps({'response': 'Success'})

    def is_car_exist(self, id):
        """
        This method checks if a car exists in the cars dictionary.
        """
        # if id in self.cars_dict:
        #     return True
        # else:
        #     return False
        if self.cars_collection.find_one({'_id': id}):
            return True
        else:
            return False


    def save_cars_state(self):
        """
        This method saves the cars dictionary to a file.
        """
        #save all cars_collection to json file
        with open('cars.json', 'w') as f:
            for car in self.cars_collection.find():
                json.dump(car, f)
                f.write('\n')

    def load_cars_state(self):
        """
        This method loads the cars dictionary from a file.
        """
        # if os.path.exists('cars.json'):
        #     with open('cars.json', 'r') as f:
        #         self.cars_dict = json.load(f)
        # load all cars from json file to cars_collection
        if os.path.exists('cars.json'):
            with open('cars.json', 'r') as f:
                cars_dict = json.load(f)
                # insert all cars_dict to cars_collection multiple in the same time
                self.cars_collection.insert_many(cars_dict)

    def get_cars_state(self):
        """
        This method returns the cars dictionary.
        """
        # return all cars stored in cars_collection
        return json.dumps([car for car in self.cars_collection.find()])

    def delete_cars_state(self):
        """
        This method deletes the cars dictionary.
        """
        # delete all cars from cars_collection
        self.cars_collection.delete_many({})
        return json.dumps({'response': 'Success'})
