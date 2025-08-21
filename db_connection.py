import configparser
import pymysql
from pymysql.err import MySQLError
class DBConnection:
    '''establish a singleton connection with db
    this class will create only one instance'''

    __instance=None  #to store singleton instance

    def __new__(cls):
        '''override to implement singleton
        ensures only one instance of dbconnection is ever created'''

        if cls.__instance is None:
            cls.__instance=super(DBConnection,cls).__new__(cls)
            cls.__instance.__initialize()
        return cls.__instance
    
    def __initialize(self):
        '''initialize the database connection using proprties from the db_config.ini
        '''
        try:
            # load the configuration file
            config=configparser.ConfigParser()
            config.read('db_config.ini')
            # establish mysql connection
            self.connection=pymysql.connect(
                host=config.get("mysql","host"),
                user=config.get('mysql',"user"),
                password=config.get("mysql","password"),
                database=config.get("mysql","database"))
           
            print('connected to mysql database')
        except MySQLError as e:
            print(f'error while connecting to mysql :{e}')
            self.connection=None

    def get_connection(self):
        return self.connection            
