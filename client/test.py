import linecache
import json

# Make sure that requests is installed in your WSL
import requests 

#set starting id and ending id
start = 1
end = 200

# Loop over the JSON file
i = start

while i <= end and i <= linecache.getline('./output.txt', last=True):
    
    # read a specific line
    line = linecache.getline('./output.txt', i)
    
    # write the line to the API
    myjson = json.loads(line)
    
    print(myjson)
    
    response = requests.post('http://localhost:80/invoiceitem', json=myjson)

    # Use this for dedbugging
    #print("Status code: ", response.status_code)
    #print("Printing Entire Post Request")
    print(response.json())

    # increase i
    i += 1
