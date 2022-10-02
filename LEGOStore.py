from mysql.connector import MySQLConnection, Error
import pandas as pd


class LEGOStore:

    conn = None
    
    # method instance constructor
    def __init__(self):
        "Instance Constructor"
        self.connect()


    # connect db
    def connect(self):
        
        db_config = {
            'host': 'localhost',
            'database': 'legostore',
            'user':'root',
            'password': '1234'
        }
        
        conn = None
        
        try:
            conn = MySQLConnection(**db_config)
            if conn.is_connected() == False:
                raise Error
        
        except Error as error:
            print("Error connect db!" )
            
        self.conn = conn

    
    # show list lego
    def show(self):
        query = "SELECT * FROM LEGOStore"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            df = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Product_Name', 'Price', 'Brand', '_Sku', 'Image', 'Description', 'Store_Address'])
            print("=======================================================================================================================")
            print(df)
            print("=======================================================================================================================\n\n")
                
        except Error as e:
            print(e)
        finally:
            cursor.close()
            
            
            
    # insert data
    def insert(self, name_product, price, brand, sku, description, store_address):
        query = """INSERT INTO LEGOStore(name_product, price, brand, sku, description, store_address) 
                                VALUES (%s, %s, %s, %s, %s, %s)"""
        
        
        value = (name_product, price, brand, sku, description, store_address)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, value)
            
            if cursor.lastrowid:
                print('\nInsert success')
            else:
                print('\nError!!! Insert fail')
                
            self.conn.commit()
            print("\n=======================================================================================================================")
            self.show()
            print("=======================================================================================================================\n\n")
        
        except Error as error:
            print(error)
            
        finally:
            cursor.close()
            
            
    # update data
    def update(self, id, name_product, price, brand, sku, description):
        query = """UPDATE LEGOStore 
                    SET name_product = %s, price = %s, brand = %s, sku = %s, description = %s
                    WHERE _id = %s
                """
        
        data = (name_product, price, brand, sku, description, id)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, data)
            
            self.conn.commit()
            print("\n=======================================================================================================================")
            self.show()
            print("=======================================================================================================================\n\n")
            
        except Error as error:
            print(error)
            
        finally:
            cursor.close()
            
    
            
    # delele data
    def delete(self, id):
        query = "DELETE FROM LEGOStore WHERE _id = %s"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (id,))
            print("Bạn có thật sự muốn xóa id = {0} không? !!!".format(id))
            confirm = input("Nhấn 'y' để đồng ý !!! 'n' để hủy lệnh")
            flag = True
            while flag:
                if confirm == "y":
                    self.conn.commit()
                    print("\n=======================================================================================================================")
                    self.show()
                    print("=======================================================================================================================\n\n")      
                elif (confirm == "n"):
                    print("Đã hủy lệnh!!!!!")
                    print("\n=======================================================================================================================")
                    self.show()
                    print("=======================================================================================================================\n\n")      
                else:
                    break
        except Error as error:
            print(error)
            
        finally:
            cursor.close()
            
    
    
    # sum total price
    def sum(self):
        query = "SELECT SUM(`PRICE`) FROM `legostore` WHERE 1"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            pf = pd.DataFrame(cursor, columns=['TOTAL_PRICE'])
            print(pf)
        
        except Error as error:
            print(error)
        finally:
            cursor.close()
    
    
    
    # find product by id
    def findById(self, id):
        try:
            cursor = self.conn.cursor()

            query = """SELECT * FROM `LEGOStore` WHERE _id = %s"""
            cursor.execute(query, (id,))
            
            df = pd.DataFrame(cursor, columns=['ID', 'Product_Name', 'Price', 'Brand', '_Sku', 'Image', 'Description', 'Store_Address'])
            
            print("\n=======================================================================================================================")
            print(df)
            print("=======================================================================================================================\n\n")
        except Error as error:
            print(error)
        
        finally:
            cursor.close()
    
    
    # find product by name
    def findByName(self, name):
        query = "SELECT * FROM LEGOStore WHERE `NAME_PRODUCT` LIKE '%{0}%'".format(name)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            df = pd.DataFrame(cursor , columns=['ID', 'Product_Name', 'Price', 'Brand', '_Sku', 'Image', 'Description', 'Store_Address'])
            
            print("\n=======================================================================================================================")
            print(df)
            print("=======================================================================================================================\n\n")
        except Error as e:
            print(e)
        finally:
            cursor.close()
            
        
            
    # ORDER by PRICE tăng dần
    def orderByPriceASC(self):
        query = "SELECT * FROM `LEGOStore` ORDER BY PRICE ASC"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            df =  pd.DataFrame(cursor , columns=['ID', 'Product_Name', 'Price', 'Brand', '_Sku', 'Image', 'Description', 'Store_Address'])
            
            print("\n=======================================================================================================================")
            print(df)
            print("=======================================================================================================================\n\n")
        except Error as error:
            print(error)
            
        finally:
            cursor.close()
            
            
    # ORDER by PRICE giảm dần
    def orderByPriceDESC(self):
        query = "SELECT * FROM `LEGOStore` ORDER BY PRICE DESC"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            df =  pd.DataFrame(cursor , columns=['ID', 'Product_Name', 'Price', 'Brand', '_Sku', 'Image', 'Description', 'Store_Address'])
            
            print("\n=======================================================================================================================")
            print(df)
            print("=======================================================================================================================\n\n")
        except Error as error:
            print(error)
            
        finally:
            cursor.close()