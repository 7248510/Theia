#First two modules.
#Scraping from an array & list
#The goal of harvesting is to extract all relevant links and put them in a list and back them in a MySQL.
#Controlling your urls is an vital step into web scraping.
#In this example module the examples will include ranges, lists(text files) and an array.
from bs4 import BeautifulSoup
import time
import requests
from config import headers,cookies, urlList
controller = range(1,11) #I'm using the tests from the data repository, I'll include the pages in Theia 1-11 == 1-10
#An Example of ranges
def collect():
    def rangeExample():
        print("Looping through a range")
        for x in controller:
            url = "http://10.0.1.4/{0}".format(x) + ".html" #The IP is meant for testing purposes, if you're going to scrape a live url change it!
            page = requests.get(url,headers=headers,cookies=cookies)
            try:
                time.sleep(1)
                html = page.content
                print(url)
            except Exception:
                print("An error occured in the request. Is your network adapter enabled?")
                print("Is the url schema correct?")
            except AttributeError:
                print("Are you scraping what's loaded in JavaScript?")
            #Declarations/BS 
            bs = BeautifulSoup(html, 'html.parser')
            #Below are an example of using find & findAll, same outputs 
            for paragraph in bs.find("p"):
                print(paragraph)
            for paragraph in bs.findAll("p"):  
                z = paragraph.get_text() 
                print(z + " Used findAll")                                            
    rangeExample()

    #Looping from a .txt file
    def loopExample():
        print("Looping through a list")
        for url in urlList:
            print(url)
            page = requests.get(url,headers=headers,cookies=cookies)
            try:
                time.sleep(5)
                html = page.content
            except Exception:
                print("An error occured in the request. Is your network adapter enabled?")
                print("Is the url schema correct?")
            except AttributeError:
                print("Are you scraping what's loaded in JavaScript?")
            #Declarations/BS 
            bs = BeautifulSoup(html, 'html.parser') 
            for titles in bs.find("title"):
                print(titles)
    loopExample()

    def loopArray():
        print("Loop through an array")
        urlArray = ["http://10.0.1.4", "https://facebook.com", "https://youtube.com"]
        for url in urlArray:
            print(url)
            page = requests.get(url,headers=headers,cookies=cookies)
            try:
                time.sleep(3)
                html = page.content
            except Exception:
                print("An error occured in the request. Is your network adapter enabled?")
                print("Is the url schema correct?")
            except AttributeError:
                print("Are you scraping what's loaded in JavaScript?")
            #Declarations/BS 
            bs = BeautifulSoup(html, 'html.parser') 
            for titles in bs.find("title"):
                print(titles)
    loopArray()
'''
NOTES:
If you find multiple elements li's a's etc. Use a find_all statement or find. I use find or select to loop make it an array.
#I don't use find_all unless I'm dealing with tags, without classes or ID'S. It helps in the beginnig(Displaying all tags regardless of ID's | Classes)-
but I had some trouble with dictionaries with find_all(multiple str_class not an array)
for links in bs.find("attribute|a"):
for links in bs.select(".CLASS_NAME"):
for links in bs.select("#ID_NAME"):
To find an elements
for links in bs.find("a"):
To find a complete list of elements
print(bs.findAll("element"))
'''