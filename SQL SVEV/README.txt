# Time-based SQL Injection Tester

This Python script tests a list of URLs and payloads for time-based SQL injection vulnerabilities. It is intended for use by ethical bug bounty hunters who have received proper authorization to perform vulnerability testing.

### Features

- Accepts command-line arguments for URLs and payloads
- Multithreading to test multiple URLs concurrently
- Error handling for failed requests
- Saves results to a file for further analysis

### Requirements

- Python 3.6 or higher
- `requests` library

### Installation

1. Clone the repository or download the `sqli_test.py` script.
2. Install the required `requests` library:


``` pip install requests ```

### Usage

Run the script with the following command-line arguments:



``` python sqli_test.py --urls "url1" "url2" --payloads "payload1" "payload2" --output "results.txt" ```

    --urls: A list of target URLs to test.
    --payloads: A list of payloads to test for time-based SQL injection.
    --output (optional): The name of the output file where the results will be saved (default: results.txt).

The script will test each URL with the provided payloads and save any potential time-based SQL injection vulnerabilities to the specified output file.

## Disclaimer

This script is intended for ethical bug bounty hunting and vulnerability testing. Ensure that you have proper authorization before testing any websites or applications.
