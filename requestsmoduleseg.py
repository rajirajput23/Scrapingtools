import requests
url="https://site.financialmodelingprep.com/developer/docs/"
r=requests.get(url)
# To check if the connection was successful
if r:
    print("Success")
else:
    print("An error has occured")

# To print the text
print(r.text)
# To print the directory 
print(dir(r))
# To print the status code
print(r.status_code)
# It is the same as r.text but it will give raw data
print(r.content)
# To access the header values
print(r.headers)
