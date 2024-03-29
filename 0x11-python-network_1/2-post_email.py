#!/usr/bin/python3
"""
sends a POST request to the passed URL with email as a parameter and
display the body of the response
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    reqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqst) as response:
        body = response.read()
    print(body.decode('utf-8'))
