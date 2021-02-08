#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import requests
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    r  = requests.get(MAJORTOM)
    
    ## put fileobject into helmet
    ## decode JSON to Python data structure
    helmetson = r.json()
    print(type(helmetson))
    
    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for p in people:
        print("{} on the {}".format(p['name'], p['craft']))

                
if __name__ == "__main__":
    main()

