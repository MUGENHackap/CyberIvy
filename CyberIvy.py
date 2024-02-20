#!/bin/python3

import requests

proxies = {'http': '127.0.0.1:7657'}

ip = input("Enter IP address: ")
port = int(input("Enter port number: "))

class Scrape_websites_for_Data:
    def __init__(self, ip, port, timeout):
        self.target_url = ip
        self.port = port
        self.timeout = timeout
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.url = "http://" + ip + ":" + str(port) + "/login.php"
        self.login_data = {"username": "admin", "password": "admin"}
        self.credentialed_url = "http://" + ip + ":" + str(port) + "/admin.php"
        self.credentialed_data = {"username": "admin", "password": "admin"}
    def make_request(self):
      try:
          print(f"Checking availability of: {self.url}")
          response = requests.get(self.url, headers=self.headers, timeout=self.timeout, proxies=proxies)
          if response.status_code == 200:
              print("Website is up and running.")
              return True
          else:
              print("Website may be down (status code: {})".format(response.status_code))
              return False
      except requests.exceptions.RequestException as e:
          print("An error occurred while making the request:", e)
          return False

    def login(self):
      if self.make_request():
          try:
              print("Attempting to login to: {}".format(self.url))
              response = requests.post(self.url, data=self.login_data, headers=self.headers, timeout=self.timeout, proxies=proxies)
              if response.url == self.credentialed_url:
                  print("Login successful")
              else:
                  print("Login failed")
          except requests.exceptions.RequestException as e:
              print("An error occurred during login:", e)
if __name__ == "__main__":
    scraper = Scrape_websites_for_Data(ip, port, 10)
    
    scraper.login()
        
