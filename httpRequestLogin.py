import requests
import random
import string
import hashlib
import base64
import json
import urllib.parse

class webPentest:
    #---------------------------------------------------------------------------------#
    # Constructor
    def __init__(self, URL, Header, JsonPayload):
        self.url = URL
        self.header = Header
        self.payload = JsonPayload
        self.httpMethod = None
        print(f"Initialized with URL: {self.url}, Header: {self.header}, Payload: {self.payload}")

    #---------------------------------------------------------------------------------#
    # Get methods
    def getURL(self):
        print(f"Getting URL: {self.url}")
        return self.url

    def getHeader(self):
        print(f"Getting Header: {self.header}")
        return self.header

    def getPayload(self):
        print(f"Getting Payload: {self.payload}")
        return self.payload

    #---------------------------------------------------------------------------------#
    # Set methods
    def setURL(self, url):
        self.url = url
        print(f"URL set to: {self.url}")

    def setHeader(self, header):
        self.header = header
        print(f"Header set to: {self.header}")

    def setPayload(self, payload):
        self.payload = payload
        print(f"Payload set to: {self.payload}")

    def setCookie(self, cookie):
        self.cookie = cookie
        print(f"Cookie set to: {self.cookie}")

    #---------------------------------------------------------------------------------#
    # Generate password methods
    def genNumRandomPass(self):
        random_pass = random.randint(0, 100000000001)
        print(f"Generated numeric random password: {random_pass}")
        return random_pass

    def genRandomPass(self):
        length = random.randint(8, 64)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print(f"Generated random password: {password}")
        return password

    #---------------------------------------------------------------------------------#
    # Encrypt and Decrypt methods
    def encryptSha512(self, str):
        encrypted_str = hashlib.sha512(str.encode('utf-8')).hexdigest()
        print(f"SHA-512 encrypted string: {encrypted_str}")
        return encrypted_str

    def encryptMd5(self, str):
        encrypted_str = hashlib.md5(str.encode('utf-8')).hexdigest()
        print(f"MD5 encrypted string: {encrypted_str}")
        return encrypted_str

    def encryptBase64(self, str):
        encrypted_str = base64.b64encode(str.encode('utf-8')).decode('utf-8')
        print(f"Base64 encoded string: {encrypted_str}")
        return encrypted_str

    def decodeBase64(self, str):
        decoded_str = base64.b64decode(str).decode('utf-8')
        print(f"Base64 decoded string: {decoded_str}")
        return decoded_str

    def base64JsonCookieEncoder(self, data):
        if isinstance(data, set):
            data = list(data)

        JsonStr = json.dumps(data)
        base64Bytes = base64.b64encode(JsonStr.encode('utf-8'))
        base64Str = base64Bytes.decode('utf-8')
        UrlEncodedStr = urllib.parse.quote(base64Str)
        print(f"Base64 and URL encoded JSON cookie: {UrlEncodedStr}")
        return UrlEncodedStr

    #---------------------------------------------------------------------------------#
    # Request methods
    def requestConfig(self, type):
        if type == 1:  # GET
            self.httpMethod = 1
            print("Request method set to GET.")
        elif type == 2:  # POST
            self.httpMethod = 2
            print("Request method set to POST.")
        elif type == 3:  # PATCH
            self.httpMethod = 3
            print("Request method set to PATCH.")

    def sendRequest(self, output):
        # Add cookie to the headers if set
        if hasattr(self, 'cookie') and self.cookie:
            self.header['Cookie'] = self.cookie
            print(f"Cookie added to header: {self.cookie}")

        # Send the request based on method type
        if self.httpMethod == 1:
            print(f"Sending GET request to {self.url} with headers {self.header} and payload {self.payload}")
            r = requests.get(self.url, headers=self.header, data=self.payload)
            if output:
                print("GET Request response:")
                print(f"Status code: {r.status_code}")
                print(f"Response content: {r.content}")
        elif self.httpMethod == 2:
            print(f"Sending POST request to {self.url} with headers {self.header} and payload {self.payload}")
            r = requests.post(self.url, headers=self.header, json=self.payload)  # Use `json` instead of `data`
            if output:
                print("POST Request response:")
                print(f"Status code: {r.status_code}")
                print(f"Response content: {r.content}")
        elif self.httpMethod == 3:
            print(f"Sending PATCH request to {self.url} with headers {self.header} and payload {self.payload}")
            r = requests.patch(self.url, headers=self.header, data=self.payload)
            if output:
                print("PATCH Request response:")
                print(f"Status code: {r.status_code}")
                print(f"Response content: {r.content}")

# Example Usage
URL = "http://example.com"
Header = {"Content-Type": "application/json"}
JsonPayload = {"key": "value"}

example = webPentest(URL, Header, JsonPayload)
example.requestConfig(1)
example.sendRequest(1)
