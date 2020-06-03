# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:25:02 2019

@author: sanaayak
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:37:45 2019

@author: sanaayak
"""

import configparser


#creating the method for reading in the config file i.e. db details 
class DatabaseConfig():
#    __slots__ = ['__db_host','__db_port','__db_user','__db_pwd','__db_name']

    def __init__(self,db_host,db_port,db_user,db_pwd,db_name):
        self.__db_host=db_host
        self.__db_port=db_port
        self.__db_user=db_user
        self.__db_pwd=db_pwd
        self.__db_name=db_name
        
        
    #defining a setter and getter for each variable 
    #REMOVE NAME 
    @property     
    def db_host(self):
         return self.__db_host #the getter
     
    @property     
    def db_port(self):
         return self.__db_port #the getter
     
    @property    
    def db_user(self):
         return self.__db_user #the getter
     
    @property                
    def db_pwd(self):
         return self.__db_pwd #the getter
     
    @property     
    def db(self):
         return self.__db_name #the getter

    @property     
    def directory(self):
         return self.__directory #the getter

     
#    @property     
    def config(self,path):
        config = configparser.ConfigParser()
        config.read(path)        
        return config 
    
    @classmethod #creates an instance for orchestration db
    def create_config_instance(cls, path,db_name):
        config = configparser.ConfigParser()
        config.read(path)
        return cls(config[db_name]['HOST'],int(config[db_name]['PORT']),config[db_name]['USERNAME'],config[db_name]['PASSWORD'],config[db_name]['DATABASE'])


# =============================================================================
#                   #how to use these objects in code
# =============================================================================
"""
#to create an instance of the config file, put in the path +the databse that you want to access. The name of the database should be of the same format as used in the config file.       
from db_config import *
myConfig=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','MIDS_database')
# names of dbs used in config=SADS_database, MIDS_database,ORCHESTRATION_database

#creating the instance for orchestration 
myConfig=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','ORCHESTRATION_database') 


#creating the instance for sads 
myConfig=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','MIDS_database') 

#creating the instance for mids 
myConfig=DatabaseConfig.create_config_instance('wrapper_config/wrapper_config.ini','SADS_database') 



#accessing the host, port, etc ie.e. the attributes from the instance created
myConfig.db_host
myConfig.db
myConfig.db_port
myConfig.db_pwd
myConfig.db_user
myConfig.directory
myConfig.config('wrapper_config/wrapper_config.ini') 
"""



