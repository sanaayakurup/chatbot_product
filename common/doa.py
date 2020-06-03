
class UserData():
    def __init__(self,table, user_name, user_number, user_otp, is_verified, conn, cursor):
        self.table = table
        self.user_name = user_name
        self.user_number = user_number
        self. user_otp = user_otp
        self.is_verified = is_verified
        self.conn = conn
        self.cursor = cursor
        
        
    
    def CreateData(table, user_name, user_number, user_otp, is_verified, conn, cursor):
        
        # try:
            
            insertSql = "INSERT INTO "+table+" (user_name, user_number, user_otp, is_verified) VALUES (%s,%s, %s,%s )  "
            print(insertSql, (user_name, user_number, user_otp, is_verified))
            print(cursor)
            cursor.execute(insertSql, (user_name, user_number, user_otp, is_verified))
            conn.commit()
        # except Exception as e:
        #         print(e)
                    
        # finally:
        #     conn.close_connection()
            
    def ReadData(table, conn, cursor):
        cursor.execute('Select * from '+table)
        # Print the data
        for row in cursor:
            print('row = %r' % (row,))
        conn.close_connection()
      
    def DeleteData(self,table, conn, cursor):
        # Get the SQL connection
          
    
         try:
           deleteQuery = "Delete From "+table+" Where id = ?"
           cursor.execute(deleteQuery,[id])
           conn.commit()
           print('Data deleted successfully!')
           
         except:
           print('Something wrong, please check')
         finally:
           conn.close_connection()

   


            

















# def getConnection():
#     conn = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_pwd, database=db_name)
#     return conn

# def closeConnection(conn):
#     conn.close()
    
# def getEngine(): 
#     engine = create_engine('mysql+pymysql://', creator=getConnection)
#     logger.info("Engine created")
#     engineCon=engine.connect()
#     logger.info("Engine connected")
#     return engineCon,engine

# def closeEngine(engineCon,engine):
#     engineCon.detach()
#     engineCon.close()
#     logger.info("Engine closed")
#     engine.dispose()
#     logger.info("Engine disposed")
    
# def getCursor(conn):
#     cur = conn.cursor(pymysql.cursors.DictCursor)
#     return cur            
            

# class Update:
#     def func_UpdateData(self):
#         # Get the SQL connection
#         connection = dbConn.getConnection()

        
#         try:
#            # Fetch the data which needs to be updated
#            sql = "Select * From "+table+ "Where Id = ?" 
#            cursor = connection.cursor()
#            cursor.execute(sql, [id])
#            item = cursor.fetchone()
#            print('Data Fetched for Id = ', id)
#            print('ID\t\t Name\t\t\t Age')
#            print('-------------------------------------------')       
#            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
#            print('-------------------------------------------')


#            name = input('Enter New Name = ')
#            age = input('Enter New Age = ')
#            query = "Update Employee Set Name = ?, Age =? Where Id =?" 
       
#            # Execute the update query
#            cursor.execute(query, [name, age, id])
#            connection.commit()
#            print('Data Updated Successfully')

#         except:
#              print('Something wrong, please check')

#         finally:
#            # Close the connection
#            connection.close()
           
