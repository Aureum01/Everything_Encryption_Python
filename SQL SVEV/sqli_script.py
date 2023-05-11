import requests
from urllib.parse import urljoin
import time

def test_sqli(target_url, payload):
    start_time = time.time()
    headers = {
        "User-Agent": f"{payload}"
    }
    response = requests.get(target_url, headers=headers)
    end_time = time.time()

    return (end_time - start_time) > 20

def main():
    urls = [
        # Add the URLs you want to test here.
    ]

    payloads = [
        # Add the payloads you want to test here.
    ]

    for url in urls:
        for payload in payloads:
            if test_sqli(url, payload):
                print(f"Possible time-based SQLi vulnerability found at {url} with payload {payload}")
                break

if __name__ == "__main__":
    main()
