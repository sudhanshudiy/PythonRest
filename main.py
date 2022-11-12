
import requests
import json
import src.base.Batsman

def check():
     resp  = requests.get("https://api.publicapis.org/entries")
     print(resp.json)


batsman = Batsman("ssas", 10 , 10)
print(batsman)