import requests

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: --------------------")
    print(resData.headers)
    
    print("Returned data: -----------------------")
    print(resData.text)

url = "http://httpbin.org/xml"

result = requests.get(url)
#printResults(result)

url = "http://httpbin.org/get"

datavalues = {
    "Name": "Rajesh",
    "Age" : "43"
}

result = requests.get(url, params=datavalues)
#printResults(result)

url = "http://httpbin.org/post"

datavalues = {
    "Name": "Rajesh",
    "Age" : "43"
}

result = requests.post(url, data=datavalues)
#printResults(result)

url = "http://httpbin.org/get"

headervalues = {
    "Name": "Rajesh",
    "Age" : "43"
}

result = requests.get(url, headers=datavalues)
#printResults(result)

import requests
from requests.auth import HTTPBasicAuth

url = "http://httpbin.org/basic-auth/Lalith123/Lbandaru389281!"

myCreds = HTTPBasicAuth("Lalith123", "Lbandaru389281!")

result = requests.get(url, auth=myCreds)

#printResults(result)

import json

jsonStr = '''{
    "Pizza": "Combo",
    "Baked": true,
    "Toppings": [
        "Olives",
        "Bell Peppers",
        "Mushrooms"
    ],
    "Price": 12.99
}'''

#data = json.loads(jsonStr)

#print("Pizza: " + data['Pizza'])

#if data['Baked']:
#    print("It's Baked")

#for topping in data['Toppings']:
#    print("Topping: " + topping)

import json

pythonData = {
        "Pizza" : "Combo",
        "Baked" : True,
        "Toppings" : ["Olives",
            "Bell Peppers",
            "Mushrooms"
        ],
    "Price" : 12.99
    }

jsonStr = json.dumps(pythonData, indent=4)

#print(jsonStr)

url = "http://www.mathkangaroo.us/mk/sample_questions.html"

result = requests.get(url)
#printResults(result)

b = bytes([0x41, 0x42, 0x43, 0x44])
#print(b)

s = "This is a string"
#print(s)

#print(b+s)

s2 = b.decode('utf-8')
#print(s+s2)

b2 = s.encode('utf-8')
#print(b+b2)

b3 = s.encode('utf-32')
#print(b3)

from string import Template

str1 = "You're watching {0} by {1}".format("Sarileru Neekavvaru", "Anil Ravipudi")
#print(str1)

templ = Template("You're watching ${movie} by ${director}")

str2 = templ.substitute(movie="Sarileru Neekavvaru", director="Anil Ravipudi")
#print(str2)

data = {
    "movie" : "Sarileru Neekavvaru",
    "director": "Anil Ravipudi"
}

str3 = templ.substitute(data)
#print(str3)

list1 = [1, 2, 3, 4, 5, 6]

#print(any(list1))

#print(all(list1))

#print("min :", min(list1))
#print("max: ",  max(list1))

#print("sum: ", sum(list1))

months = ["Jan", "Feb", "Mar", "Apr"]
monthsFr = ["Jan", "Fev", "Mar", "Avr"]

i = iter(months)
#print(next(i))
#print(next(i))
#print(next(i))

#for m in months:
#    print(m)

#with open("groceries.txt", "r") as fp:
    #for line in iter(fp.readline, ''):
    #    print(line)

#for m in range(len(months)):
#    print(m+1, months[m])

#for i, m in enumerate(months, start=1):
#    print(i, m)

#for m in enumerate(zip(months, monthsFr), start=1):
#   print(i, m[0], "=", m[1], "in French")

#def addition(*args):
#    result += 0
#    for arg in args:
#        result += arg
#    return result

def CelciustoFahrenheit(temp):
    return (temp - 32) * 5/9

def FahrenheittoCelcius(temp):
    return (temp * 9/5) + 32

ftemp = [25, 50, 75, 100, 90]
ctemp = [15, 20, 75, 100, 50]

#print(list(map(CelciustoFahrenheit, ftemp)))
#print(list(map(FahrenheittoCelcius, ctemp)))

#print(list(map(lambda t: (t - 32) * 5/9, ftemp)))
#print(list(map(lambda t: (t * 9/5) + 32, ctemp)))

import collections

Number = collections.namedtuple("Number", "a b")

n1 = Number(1, 2)
n2 = Number(5, 6)

#print(n1, n2)

#print(n1.a, n2.b)

n1 = n1._replace(a=25)
#print(n1)

#import collections

#Number = collections.namedtuple("Number", "a b")

#n1 = Number(1, 2)
#n2 = Number(5, 6)

#print(n1, n2)

#print(n1.a, n2.b)

#n1 = n1._replace(a=25)
#print(n1)

from collections import defaultdict

veggies = ['tomato', 'okra', 'squash', 'spinach',
            'tomato', 'tindora', 'okra', 'tomato']

veggieCounter = defaultdict(int)

for veggie in veggies:
    if veggie in veggieCounter.keys():
        veggieCounter[veggie] += 1
    else:
        veggieCounter[veggie] = 1

#for (v, k) in veggieCounter.items():
#    print(v + ":"+ str(k))

#print(veggie)

from enum import Enum, unique, auto

@unique
class Veggie(Enum):
    BEANS = 1
    TOMATO = 5
    OKRA = 3
    TINDORA = 2
    RED_TOMATO = 4
    CARROT = 10

# print(Veggie.BEANS)
# print(type(Veggie.TOMATO))
# print(repr(Veggie.TINDORA))

#print(Veggie.TOMATO.name, Veggie.BEANS.name)

#print(Veggie.CARROT.value)

myVeggies = {}

myVeggies[Veggie.CARROT] = "Vaishu did Hiah"
# print(myVeggies[Veggie.CARROT])

