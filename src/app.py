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
    def __init__(self, user_name, user_number, otp):
        self.user_name=user_name
        self.user_number=user_number 
        self.otp=otp
        
#register-user api 
@application.route("/user-registration/<user_name>/<user_number>", methods=["POST"])
def run_insert_doa(user_name, user_number):
    #making a connection to the db 
    conn = Connection.create_conn_instance(myConfig)
    cursor = conn.cursor
    #gen otp
    user_otp=random_with_N_digits(3) #user_otp generated
    userdata_obj=UI_UserData(user_name,user_number,user_otp)
    #calls gagans code which inserts in the table
    UserData.CreateData('user_data', userdata_obj.user_name, userdata_obj.user_number, user_otp, "0", conn, cursor)
    logger.info("User Details inserted into database")
    return json.dumps({"response_code":"200","message":"successfuly entered data in db"})

@application.route("/verify-user/<otp>", methods=["GET"])
def verify_user(otp):
    #making a connection to the db 
    conn = Connection.create_conn_instance(myConfig)
    cursor = conn.cursor
    user_provided_otp=otp #save users supplied otp in otp var #UserData.ReadData('user_data',conn,  cursor)
    generated_otp=3652 #change this to a select sql where user_number==, fetch this val from a table 
    if generated_otp==user_provided_otp:
        print("your account is verified, you can carry on")
        logger.info("Account was verifed")

        #run update in table where user_number==something
    else:
        print("please provide the correct otp")
        logger.info("Account was not verifed")
   
    

if __name__ == '__main__':
    application.run( port = 5000, host='127.0.0.1')
    