from dao.productdaoimplementation import Productdaoimplemtation
from dao.abstarctproductdao import Productdaoservice
from models.product import Product
from datetime import datetime
class Productmanagmentlib:
    'handles CRUD logic '
    dao_service:Productdaoservice=Productdaoimplemtation()

    @staticmethod
    def display_all():
        products=Productmanagmentlib.dao_service.display_all_prdcts()
        for product in products:
            print(product)

    @staticmethod
    def add_product():
        product=Product()
        productname=input('enter pro name:')
        product.set_productName(productname)
        unitprice=float(input('enter unit price:'))
        product.set_unitprice(unitprice)
        categoryid=int(input('enter category id:'))
        product.set_categoryid(categoryid)
        m_date=input('enter manufacture date(dd/mm/yyyy):')
        util_date=datetime.strptime(m_date,"%d/%m/%Y")
        conv_m_date=util_date.date()
        product.set_manufacture_date(conv_m_date)

        if Productmanagmentlib.dao_service.insert_products(product):
            print('inserted successflly')

        else:
            print('something went wrong')

    @staticmethod
    def update_product():
        searchid=int(input('enter the product id: '))
        # create a method in dao
        product=Productmanagmentlib.dao_service.find_by_product_id(searchid)
        if not product:
            print('product not found')
            return
        print(product)
        confirm=input('do you want to edit this data?(y/n)')
        if confirm.lower()=='y':
            product.set_productName(input('enter new product name:'))
            product.set_unitprice(float(input('enter new unit price: ')))
            # pass the object to dao update
            if Productmanagmentlib.dao_service.update_product(product,searchid):
                print('updated successfully!!')
            else:
                print('something went wrong!!')
    
    @staticmethod
    def disable_product():
        prodid=int(input('enter product id to disable:  '))
        # create method in dao
        product=Productmanagmentlib.dao_service.find_by_product_id(prodid)
        if not product:
            print('product not found!!')
            return
        print(product)
        confirm=input('do you want to disable the data?(y/n)')
        if confirm.lower()=='y':
            if Productmanagmentlib.dao_service.disable_product(product,prodid):
                print('disabled successfully')
            else:
                print('something went wrong')

    @staticmethod
    def find_by_id():
        prodid=int(input('enter product id:'))
          # create method in dao
        product=Productmanagmentlib.dao_service.find_by_product_id(prodid)
        if not product:
            print('product not found!!')
            return
        print(product)

    @staticmethod
    def apply_gst_to_product():
        product_id=int(input('enter product id to apply gst:'))
        gst_percentage=float(input('enter gst percent to apply: '))
        if Productmanagmentlib.dao_service.apply_gst(product_id,gst_percentage):
            print(f'gst of {gst_percentage} applied to product id {product_id}')
        else:
            print('failed to apply gst')
