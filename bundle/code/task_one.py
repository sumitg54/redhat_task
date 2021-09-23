############################################################################################################################
#       Name        : task_one.py
#       Description : This code is devloped for Request the library to perform API requests.
#                     Here we are using the xkcd API which allows us to fetch various XKCD comics 
#                     And their metadata. After the fetching the data we are inserting into MYSQL.
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

#create the list to Generate the 15 unique random number.
randomlist = random.sample(range(1, 87), 15)

#create class to add data in dictonary
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

#MySql - Making Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass@123"
)

#create cursor object
mycursor = mydb.cursor()

#execute DDL query (either we can call from here or we can remove it from here and run from MYSQL)
mycursor.execute("CREATE DATABASE if not exists comic_db")
mycursor.execute("CREATE TABLE if not exists comic_db.comic (comic_name VARCHAR(255), alt_text VARCHAR(255), number int, link VARCHAR(255),image VARCHAR(255), imageLink VARCHAR(255))")
mycursor.execute("TRUNCATE TABLE comic_db.comic")

recordList=[]
#get the random unique number from list
for x in randomlist:
    #get comic information from XKCD API
    getComic = requests.get("https://xkcd.com/{0}/info.0.json".format(x))
    
    #check the response code
    if (getComic.status_code == 200):
        #get response json
        comic_details=getComic.json()
        
        #fetch column details from json
        comicName=comic_details["title"]
        comicAltText=comic_details["alt"]
        comicNumber=comic_details["num"]
        comicLink=comic_details["link"]
        comicImg=comic_details["img"].split("/")[-1]
        comicImgLink=comic_details["img"]
        
        #append in list for bulk insert
        recordList.append((comicName,comicAltText,comicNumber,comicLink,comicImg,comicImgLink))
    elif (response.status_code == 404):
        print("Result not found!")
        exit

#bulk insert into MYSQL db
insert_sql = "INSERT INTO comic_db.comic (comic_name, alt_text, number, link, image, imageLink) VALUES (%s, %s, %s, %s, %s, %s)"
mycursor.executemany(insert_sql, recordList)

#commit insert data
mydb.commit()

#print(mycursor.rowcount, "record inserted.")

#select data using query
mycursor.execute("SELECT * FROM comic_db.comic")
myresult = mycursor.fetchall()

final=[]
#loop for showing the data on console
for row in myresult:
    mydict = create_dict()
    mydict.add("comic",row[0])
    mydict.add("comic_meta",({"alt_text":row[1],"number":row[2],"link":row[3],"image":row[3],"image_link":row[3]}))
    final.append(mydict)
    
stud_json = json.dumps(final, indent=2, sort_keys=True)
print(stud_json)

#terminate connection
mycursor.close()