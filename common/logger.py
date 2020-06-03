# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:02:58 2019

@author: sanaayak
"""
import configparser
import logging 


class Logger():
    __slots__ = ['__handler','__formatter','__loglevel']
    
    def __init__(self,handler,formatter,loglevel):
        self.__handler=handler
        self.__formatter=formatter
        self.__loglevel=loglevel
    
    @property    
    def handler(self):
         return self.__handler
    
    @property      
    def formatter(self):
         return self.__formatter

    @property     
    def loglevel(self):
         return self.__loglevel
           
    def get_logger(self,handler):
        return logging.getLogger(handler)
        
    def split_logger(self,handler):
        a,b,wrapper_log,logfile_name=handler.split('/')
        return logfile_name        
    
    def logging_filehandler(self,handler):
        return logging.FileHandler(handler) #converting the type of the obj to log type

    def logging_formatter(self,formatter):
        return logging.Formatter(formatter) #converting the type of the obj to log type
    
    def set_formatter(self,handler,formatter):
        return handler.setFormatter(formatter)

        
    def add_handler(self,logger,handler):
        return logger.addHandler(handler)
    
    def set_logger_level(self,logger,loglevel):
        return logger.setLevel(loglevel)
    
    def start_logging(self,logger):
        return logger.info('{} begin logging...'.format(logger))

    @classmethod #creates an instance for mids db  
    def create_logger_instance(cls,path):
        config = configparser.ConfigParser()
        config.read(path)
        return cls(config['loginfo']['LOG_FILE'],config['loginfo']['LOG_FORMAT'],config['loginfo']['LOG_LEVEL'])

#create a method to start logging
    def initiate_logging(self):
        logger=self.get_logger(self.handler) #create logger
        logger=self.split_logger(self.handler) #setting the logger name 
        handler=self.logging_filehandler(self.handler)
        formatter=self.logging_formatter(self.formatter)
        logger=self.get_logger(logger)  #converting it back into a log type file  
        self.set_formatter(handler,formatter) #SETTING FORMAT OF THE HANDLER 
        self.add_handler(logger,handler) 
        #add handler 
        loglevel=self.loglevel
        self.set_logger_level(logger,loglevel) #setting the level for log to debug 
        self.start_logging(logger)
        return logger

 
    
        
# =============================================================================
#                    How to use it in code is documented below 
# =============================================================================

"""
test=Logger.create_logger_instance('wrapper_config/wrapper_config.ini') #instance creation
a=test.initiate_logging() #run this to initiate the logging for your batch file. logger is stored in variable 'a'
a.info("error in obtaining the wf id") #use this line of code to log in specific errors at each step 

"""
