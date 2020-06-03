import requests
import datetime
import mysql.connector
from pymongo import MongoClient
urls = ['http://10.0.1.4:3000'] #This is url is for testing headers, I wrote an Node js application to view your browsers headers & method
cookies = dict(cookies='Paste alert(document.cookie[the value]) or console.log(document.cookie)')
#Opening the test file and stripping the \n 
session = requests.session()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','accept-language':'en-US,en;q=0.5','accept-encoding': 'gzip, deflate'}
#If you're using a remote server you have to allow other access. It won't work automatically
#Local host for testing(If your adding another ip make sure the DB allows the remote connection and has access control)
#MySQL
sqlConf = {
    'user': 'data',
    'password': '',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True
}
cnx = mysql.connector.connect(**sqlConf)
cursor = cnx.cursor()
#Mongo begins
client = MongoClient('127.0.0.1', 27017) #Default port for MongoDB!

#For the extraction operation! After the harvest operation is complete you should links you'd like to scrape. If you have some links you'd like to scrape paste them in the file.
with open('Lists\info.txt', 'r') as f:
    urlList = [line.rstrip() for line in f]