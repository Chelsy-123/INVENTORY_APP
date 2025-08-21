from dao.abstarctproductdao import Productdaoservice
from db_connection import DBConnection
from models.product import Product
from pymysql.cursors import DictCursor
class Productdaoimplemtation(Productdaoservice):
    'implementation for abstract class productdaoservice'
    # sql queries
    DISPLAY_ALL='select * from products'
    INSERT_PRODUCT='insert into products(productname,unitprice,categoryid,manufacturedate,isActive)VALUES(%s,%s,%s,%s,%s)'
    FIND_BY_ID='select * from products where productid=%s'
    UPDATE_PRODUCT='UPDATE products set productname=%s, unitprice=%s where productid=%s'
    DISABLE_PRODUCT="update products set isActive='n' where productid=%s"
    APPLY_GST='call apply_gst_to_product(%s,%s)'
    def __init__(self):
        self.conn=DBConnection().get_connection()
    def insert_products(self,product:Product)->bool:
        try:
            cursor=self.conn.cursor() #create a cursor object
            cursor.execute(self.INSERT_PRODUCT,(product.get_productName(),
                                                product.get_unitprice(),
                                                product.get_categoryid(),
                                                product.get_manfacture_date(),
                                                product.get_is_active()))
            self.conn.commit()
            return cursor.rowcount==1
        except Exception as e:
            print('error inserting product:',e)
            return False
        finally:
            cursor.close()
    def display_all_prdcts(self):
        products=[]
        cursor=None
        try:
            cursor=self.conn.cursor(DictCursor) #return data in dictionary
            cursor.execute(self.DISPLAY_ALL)# fire the query
            rows=cursor.fetchall()
            for row in rows:
                products.append(Product(productid=row['productid'],productName=row['productname'],unitprice=row['unitprice'],categoryid=row['categoryid'],manufacturedate=row['manufacturedate'],is_active=row['isActive']))

        except Exception as e:
            print('error fetching products:',e)
        finally:
            cursor.close()
        return products
    
    def find_by_product_id(self,product_id:int):
        product=None
        try:
            cursor=self.conn.cursor(DictCursor)
            cursor.execute(self.FIND_BY_ID,(product_id,))
            row=cursor.fetchone()
            if row:
                product=Product(productid=row['productid'],
                                productName=row['productname'],
                                unitprice=row['unitprice'],
                                categoryid=row['categoryid'],
                                manufacturedate=row['manufacturedate'],
                                is_active=row['isActive'])

        except Exception as e:
            print('error finding product: ',e)
        finally:
            cursor.close()
        return product
    

    def update_product(self, product, product_id):
        try:
            cursor=self.conn.cursor(DictCursor)
            cursor.execute(self.UPDATE_PRODUCT,(product.get_productName(),
                                                product.get_unitprice(),
                                                product_id))
            self.conn.commit()
            return cursor.rowcount==1
        except Exception as e :
            print('error updating product: ',e)
            return False
        finally:
            cursor.close()

    def disable_product(self, product, product_id):
        try:
            cursor=self.conn.cursor(DictCursor)
            cursor.execute(self.DISABLE_PRODUCT,(product_id,))
            self.conn.commit()
            return cursor.rowcount==1
        except Exception as e:
            print('error disablng product: ',e)
            return False
        finally:
            cursor.close()

    def apply_gst(self, product_id:int, gst_percentage:float):
        cursor=None
        try:
            cursor=self.conn.cursor()
            cursor.execute(self.APPLY_GST,(product_id,gst_percentage))
            self.conn.commit()
            return cursor.rowcount>=0  #since sp returns 0 if already applied
        except Exception as e:
            print('error applying gst:',e)
            return False
        finally:
            if cursor:
                cursor.close()
        
