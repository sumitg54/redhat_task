############################################################################################################################
#       Name        : task_one.py
#       Description : This code is develope to read comics? Please provide a number/Title and read on the web
#
#       Author      : Sumit Gupta
#       
#       Change Log  :
#       ------------------------------------------------------------------------------------------
#       Date                    Developer                Description
#       ------------------------------------------------------------------------------------------
#       23-SEP-2021             Sumit Gupta              Code Devlopment
#
############################################################################################################################
#import required Library
import random
import requests
import mysql.connector
import json
import webbrowser

#MySql - Making Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass@123"
)

#create cursor object
mycursor = mydb.cursor()

INPUT = input("Would you like to read comics? ")
if INPUT.lower() == ("yes"):
    INPUT1 = input("Please provide a number/Title ")
    if INPUT1.isdigit():
        where_clasue="where number={0}".format(INPUT1);
    else:
        where_clasue="where comic_name='{0}'".format(INPUT1);

    #select data using query
    sql="SELECT imageLink FROM comic_db.comic {0}".format(where_clasue)
    mycursor.execute(sql)
    output = mycursor.fetchone()    
    if(mycursor.rowcount != 0):
        print("Check the Browser")
        webbrowser.open(output[0])    
    else:
        print("Invalid Input")
        
elif INPUT.lower() == ("no"):
    #print ("try again")
    exit
else: 
    print("Please enter yes or no.")

#terminate connection
mycursor.close()
