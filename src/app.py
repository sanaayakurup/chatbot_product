from flask import Flask, request, jsonify
import logging
from common.logger import *
from common.connections import *
import json
import configparser
from common.db_config import *
from common.doa import UserData
import numpy as np
from random import randint

#OTP Generator
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

 

#import src.doa_crud #CRUD DOA
application = Flask(__name__)

 

#SET Config file 
myConfig=DatabaseConfig.create_config_instance('../config/config_dev.ini','chatbot_rmg_1') #creating an instance of the config file with db name 

 

#set logger file
logger_instance=Logger.create_logger_instance('../config/config_dev.ini') #instance creation
logger=logger_instance.initiate_logging()
logger.info("Begin logging. . .") #use this line of code to log in specific errors at each step 
 

#attributes for userdata class
class UI_UserData():
    def __init__(self, user_name, user_number):
        self.user_name=user_name
        self.user_number=user_number 
        
#register-user api 
@application.route("/user-registration/<user_name>/<user_number>", methods=["POST"])
def run_insert_doa(user_name, user_number):
    userdata_obj=UI_UserData(user_name,user_number) #create an instance of the class with the vars coming from the UI
    #making a connection to the db 
    conn = Connection.create_conn_instance(myConfig)
    cursor = conn.cursor
    #gen otp
    user_otp=random_with_N_digits(3) #user_otp generated
    #calls gagans code which inserts in the table 
    UserData.CreateData('user_data', userdata_obj.user_name, userdata_obj.user_number, user_otp, "0", conn, cursor)
   # UserData.ReadData('user_data',conn,  cursor)
    logger.info("User Details inserted into database")
    return json.dumps({"response_code":"200","message":"successfuly entered data in db"})
    
if __name__ == '__main__':
    application.run( port = 5000, host='127.0.0.1')
    