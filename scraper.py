import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

'''Important Points: Lots of code is not properly optimized in this for the sake of having some sort of functional ability in 8 hours. 
For example, the "instance" argument in all of the functions is going to be replaced with a better form of selection at some point in development.
Currently, createPandas and createTableCSV have functional outputs on the test website, and createListCSV should also be functional (createList is currently 
not displaying the correct final list.
elementTraceback is not functional, it and it's accompanying lookup function will be created later in the development of this package. '''





'''elementTraceback: This creates a traceback string related to the selected element, which will be used by a lookup function to find the element at it's position
Example Use: Tracking the amount of students at UTD. I can setup the traceback string by targeting the population at the time of setup (currently 19,872 undergrad).
I could then use the traceback string to get accurate updates on UTD's population from the UTD website. Of course, an API could solve the same issue, but there are
cases where there is no API for info tracked on the web.
This function is currently NOT functional. '''

'''def elementTraceback(link = "", key = "", instance = 1):
    liList = []
    data = []
    website=requests.get(link)
    soup = BeautifulSoup(website.content, "html.parser")
    search = 0
    tag = soup.head
    for case in soup:
        if key.lower in case.string.lower():
            search+=1
            if search == instance:
                tag = case
                break
            else:
                continue
    tag =
    for (parent in tag.parents)'''

'''createList: takes an list element from the page and returns a list containing the element and it's siblings.
Currently needs testing'''

def createList(link ="", key = "", instance = 1):
    liList = []
    data = []
    tagList = []
    website = requests.get(link)
    soup = BeautifulSoup(website.content, "html.parser")
    search = 0
    cases = soup.findAll("li")
    iterator = -1
    for case in cases:
        tagList.append(case)
        weirdSoup = BeautifulSoup(str(case), "html.parser")
        text = weirdSoup.get_text()
        text = text.replace("\n", " ")
        if (text != " " and text != "\n" and text != ""):
            liList.append(text)
    for case in liList:
        iterator+=1
        if key.lower() in case.lower():
            search +=1
            if search == instance:
                break
            else:
                continue
    tag = tagList[iterator]
    parent = tag.parent
    for child in parent.children:
        weirdSoup = BeautifulSoup(str(child), "html.parser")
        text = weirdSoup.get_text()
        text = text.replace("\n", " ")
        if (text != " " and text != "\n" and text != ""):
            data.append(text)
            print(text)
    return data

#createListCSV: same as createList but outputs a CSV file instead of a list
def createListCSV(link = "", key = "", instance = 1, csvName = ""):
    data = createList(link, key, instance)
    df = pd.DataFrame({"col":data})
    df.to_csv(csvName, index=False, header=False)

'''createPandas: creates a table using a table element. 
Functional on test case 1, nonfunctional on test case 2.'''
def createPandas(link = "", key = "", instance = 1):
    liList = []
    data = []
    website = requests.get(link)
    soup = BeautifulSoup(website.content, "html.parser")
    search = 0
    cases = soup.findAll("td")
    for case in cases:
        liList.append(str(case.string))
    for case in liList:
        if key.lower() in case.lower():
            search +=1
            if search == instance:
                break
            else:
                continue
    tag = cases[search]
    table = tag.parent.parent.parent
    df = pd.DataFrame()
    col = 0
    for parent in table.find_all("tr"):
        data = []
        for child in parent.children:
            weirdSoup = BeautifulSoup(str(child), "html.parser")
            text = weirdSoup.get_text()
            text = text.replace("\n", " ")
            if (text != " " and text != "\n" and text != ""):
                data.append(text)
        newDF = pd.DataFrame(data)
        df = pd.concat([df, newDF], axis=1)
    return df

'''createTableCSV: same as createPandas but returns a CSV. 
    functional but will need testing when createPandas is tested more'''
def createTableCSV(link ="", key ="", instance = 1, csvName =""):
    df = createPandas(link, key, instance)
    df.to_csv(csvName, index=False, header=False)

