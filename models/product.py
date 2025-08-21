from datetime import date
import re
class Product:
    'python oops applied'
    def __init__(self, productid=None, productName=None, unitprice=None, categoryid=None, manufacturedate=None, is_active='y'):
        self.__productid = productid
        self.__productName = productName
        self.__unitprice = unitprice
        self.__categoryid = categoryid
        self.__manufacturedate = manufacturedate 
        self.__is_active=is_active

#getters and setters

    def get_productid(self):
        return self.__productid
    def set_productid(self,productid):
        self.__productid = productid

    def get_productName(self):
        return self.__productName
    def set_productName(self,productName):
        'validate product name before setting (2-30 alphabets/underscore)'
        pattern = re.compile(r"^[A-Za-z_]{2,30}$")

        while True:
            if pattern.match(productName):
                self.__productName = productName
                break
            else:
                print("\t\t invalid product name must have only alphabets !!!..")
                productName = input("\t\tenter product name again: ")

    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice=unitprice

    def get_categoryid(self):
        return self.__categoryid
    def set_categoryid(self,categoryid):
        self.__categoryid=categoryid

    def get_manfacture_date(self):
        return self.__manufacturedate
    def set_manufacture_date(self,manufacturedate):
        if isinstance(manufacturedate,date):

            self.__manufacturedate=manufacturedate
        else:
            raise ValueError("manufacture dae must be date object")
    
    def get_is_active(self):
        return self.__is_active
    
    def set_is_active(self,is_active):
        self.__is_active=is_active

        # override __str__

    def __str__(self):
        return f'productid: {self.__productid:<10},productname:{self.__productName:<20},catgoryid:{self.__categoryid:<10},unitprice:{self.__unitprice:<15},manufacturedate:{self.__manufacturedate:<15},is_active:{self.__is_active}'


