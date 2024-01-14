#!/usr/bin/pyhton3
'''Module containing tests for the BaseModel'''

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    '''Test class for BaseModel'''
    @classmethod
    def setUpClass(self):
        '''create an instance of the BaseModel class before each test'''
        pass

    def test_id(self):
        '''test BaseModel id'''
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertIsInstance(self.obj1.id, str)
        self.assertNotEqual(self.obj1, self.obj2)

    def test_created_at(self):
        '''test created_at property'''
        self.bm_created_at = BaseModel()
        self.assertIsInstance(self.bm_created_at, BaseModel)
        self.assertTrue(hasattr(self.bm_created_at, "created_at"))
        self.assertIsInstance(self.bm_created_at.created_at, datetime)

    def test_updated_at(self):
        '''test updated_at property'''
        self.bm_updated_at = BaseModel()
        self.assertIsInstance(self.bm_updated_at, BaseModel)
        self.assertTrue(hasattr(self.bm_updated_at, "updated_at"))
        self.assertIsInstance(self.bm_updated_at.updated_at, datetime)

    def test_kwargs(self):
        ''' Test case for objects instanciated from **kwargs '''
        exp_kwargs = {
                "id": 'eb78b0b0-e3e4-6bbc-a5e1-60002edc3c7e',
                "created_at": '2005-01-17T12:30:34.884906',
                "updated_at": '2020-07-20T06:25:58.906884'
        }
        self.base_kwargs = BaseModel(**exp_kwargs)
        self.assertIsInstance(self.base_kwargs, BaseModel)
        self.assertEqual(self.base_kwargs.__class__.__name__, "BaseModel")
        self.assertEqual(self.base_kwargs.id, exp_kwargs['id'])
        self.assertIsInstance(self.base_kwargs.created_at, datetime)
        self.assertIsInstance(self.base_kwargs.updated_at, datetime)
        self.assertEqual(self.base_kwargs.created_at,
                datetime.fromisoformat(exp_kwargs['created_at']))
        self.assertEqual(self.base_kwargs.updated_at,
                datetime.fromisoformat(exp_kwargs['updated_at']))

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_str(self):
        '''test __str__ function'''
        self.bm_str = BaseModel()
        self.assertIsInstance(self.bm_str, BaseModel)
        self.assertTrue(hasattr(BaseModel.__dict__, "__str__"))
        self.assertEqual(self.bm_str.__str__(),
                "[{}] ({}) {}".format(
                    self.bm_str.__class__.__name__,
                    self.bm_str.id,
                    self.bm_str.__dict__
                ))

    def test_to_dict(self):
        '''test to_dict method'''
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue("to_dict" in dir(BaseModel))
        self.bm_dict = BaseModel().to_dict()
        self.assertIsInstance(self.bm_dict, dict)
        self.assertTrue("id" in self.bm_dict)
        self.assertTrue("created_at" in self.bm_dict)
        self.assertTrue("updated_at" in self.bm_dict)
        self.assertTrue("__class__" in self.bm_dict)
        self.assertEqual(self.bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(self.bm_dict["created_at"], str)
        self.assertIsInstance(self.bm_dict["updated_at"], str)

    def test_save(self):
        '''test save() method'''
        save_obj = BaseModel()
        updated_time = save_obj.updated_at
        save_obj.save()
        self.assertLess(updated_time, save_obj.updated_at)
