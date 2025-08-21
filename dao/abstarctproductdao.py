from abc import ABC,abstractmethod
from typing import List
from models.product import Product

class Productdaoservice(ABC):
    @abstractmethod
    def display_all_prdcts(self)->List[Product]:
        '''fetch all products'''
        pass

    @abstractmethod
    def insert_products(self)->bool:
        '''insert product to db'''
        pass

    @abstractmethod
    def find_by_product_id(self)->Product:
        '''find a product by id'''
        pass

    @abstractmethod
    def update_product(self,product:Product,product_id:int)->bool:
        '''update product by its id'''
        pass

    @abstractmethod
    def disable_product(self,product:Product,product_id:int)->bool:
        '''disable product '''
        pass

    @abstractmethod
    def apply_gst(self,product_id:int,gst_percentage:float)->bool:
        '''compute gst of the product'''
        pass
   