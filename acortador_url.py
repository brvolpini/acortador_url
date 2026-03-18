import requests,sys,json

long_url = sys.argv[1]


url = "https://api-ssl.bitly.com/v4/shorten"

payload = "{{\r\n    \"long_url\": \"{}\"\r\n}}\r\n".format(long_url)


headers = {
    'Authorization': 'Bearer ' + "0638eea2129b64f83bfd6ed0029cd0894465bef0" ,
    'Content-Type': 'application/json'
}


response = json.loads(requests.request("POST", url, headers=headers, data = payload).text.encode('utf8'))

print(response['link'])
