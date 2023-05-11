#Author: Aurem01
#DateL 5/11/2023
#python sqli_trunner.py --urls "url1" "url2" --payloads "payload1" "payload2"

import argparse
import requests
import time
import threading
from urllib.parse import urljoin

def test_sqli(target_url, payload):
    start_time = time.time()
    headers = {
        "User-Agent": f"{payload}"
    }
    try:
        response = requests.get(target_url, headers=headers, timeout=30)
    except requests.exceptions.RequestException as e:
        print(f"Error testing {target_url} with payload {payload}: {e}")
        return False

    end_time = time.time()
    return (end_time - start_time) > 20

def test_url(url, payloads, results):
    for payload in payloads:
        if test_sqli(url, payload):
            print(f"Possible time-based SQLi vulnerability found at {url} with payload {payload}")
            results.append((url, payload))
            break

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", nargs="+", help="List of URLs to test")
    parser.add_argument("--payloads", nargs="+", help="List of payloads to test")
    parser.add_argument("--output", default="results.txt", help="Output file for results")
    args = parser.parse_args()

    urls = args.urls
    payloads = args.payloads
    results = []

    threads = []
    for url in urls:
        t = threading.Thread(target=test_url, args=(url, payloads, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open(args.output, "w") as f:
        for url, payload in results:
            f.write(f"{url}\t{payload}\n")

if __name__ == "__main__":
    main()

