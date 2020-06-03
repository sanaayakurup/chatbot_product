# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:57:34 2019

@author: sanaayak
"""
from common.db_config import *
import pymysql

"""
#creating the instance for orchestration 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','ORCHESTRATION_database') 


#creating the instance for sads 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','MIDS_database') 

#creating the instance for mids 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','SADS_database') 

"""


class Connection():
    
    def __init__(self,conn,cursor):
        self.conn=conn
        self.cursor=cursor

#    @property
    def conn(self):
        return self.conn
    
#    @property
        #CHECK IF CURSOR IS OPEN, IS OPEN CLOSE IT IN THIS METHOD 
    def close_connection(self):
        return self.conn.close
        if self.cursor!= None:
            print(" cursor closed")
            return self.cursor.close()
#            print(" cursor closed")
    
#    @property
    def cursor(self):
        return self.cursor

##    @property
##        REMOVE CLOSE CURSOR
#    def close_cursor(self):
#        return self.cursor.close() 
#    @property
    def commit(self):
        self.conn.commit()
        
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
            
    @classmethod #creates an instance of the class 
    def create_conn_instance(cls,config_details):
        conn = pymysql.connect(host=config_details.db_host, port=config_details.db_port, user=config_details.db_user, password=config_details.db_pwd, database=config_details.db)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return cls(conn,cursor)
                   
                   
# =============================================================================
                            # how to use the code
# =============================================================================

"""
 #creating the instance for orchestration 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','ORCHESTRATION_database') 


#creating the instance for sads 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','MIDS_database') 

#creating the instance for mids 
config_details=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','SADS_database') 

test=Connection.create_conn_instance(config_details) #creating an instance of the class
test.conn #checking conn 
test.cursor #checking cursor
connetion=test.conn #new conn is created 
test.close_connection() #closing conn and cursor 

"""
