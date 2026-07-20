# SQL Injection Scanner

## Overview

The SQL Injection Scanner is a Python-based security tool that scans web forms for potential SQL Injection vulnerabilities. It automatically discovers HTML forms on a webpage, injects predefined SQL payloads into input fields, analyzes server responses for common SQL error messages, and reports potential vulnerabilities.

This project was developed for educational purposes to demonstrate the basic concepts of automated web vulnerability scanning. It should only be used against systems that you own or have explicit permission to test.

---

## Features

- Automatically crawls webpages and discovers HTML forms
- Supports both **GET** and **POST** forms
- Injects SQL Injection payloads into form inputs
- Detects common SQL database error messages
- Records vulnerable endpoints and payloads
- Generates a scan summary
- Logs scan results to a file
- Uses basic concurrency with `ThreadPoolExecutor`
- Includes rate limiting between requests
- Includes a local Flask test server for safe testing

---

## Technologies Used

- Python 3
- requests
- BeautifulSoup4
- Flask (testing server)
- logging
- concurrent.futures

---

## Project Structure

```
SQL_Injection_Scanner/
│
├── scannerpr.py              # Main SQL Injection scanner
├── test_server.py          # Local vulnerable Flask server
├── payloads.txt            # SQL Injection payloads
├── logs/
│   └── scan_results.txt    # Scan results
└── README.md
```

---

## Installation

Clone the repository or download the project.

Install the required libraries:

```bash
pip install requests beautifulsoup4 flask
```

---

## Running the Project

### Step 1 – Start the Test Server

Run the local Flask application:

```bash
python test_server.py
```

The server will start on:

```
http://127.0.0.1:5000
```

---





### Step 2 – Run the Scanner

Open another terminal and run:

```bash
python scannerpr.py
```

Enter the target URL:

```
Target URL:
http://127.0.0.1:5000
```

The scanner will:

1. Download the webpage
2. Discover all HTML forms
3. Inject SQL payloads
4. Analyze server responses
5. Report potential SQL Injection vulnerabilities

---

## Example Payloads

Example contents of `payloads.txt`:

```
'
''
' OR '1'='1
admin'--
UNION SELECT NULL--
```

---

## Example Output

```
Found 1 form(s).

Scanning: http://127.0.0.1:5000

[!] Potential SQL error detected with payload: '

' -> Status: 500 | Length: 191 bytes

========== Scan Summary ==========

Target: http://127.0.0.1:5000
Forms Found: 1
Payloads Tested: 5
Requests Sent: 5
Potential Findings: 4
```
![SQL Injection Scanner Results](screenshots/SQL_Injection_Scanner%20results.png)

---

## How It Works

1. Downloads the target webpage.
2. Extracts all HTML forms using BeautifulSoup.
3. Reads each form's action, method, and input fields.
4. Loads SQL payloads from `payloads.txt`.
5. Submits each payload to every discovered form.
6. Analyzes the server response for common SQL error messages.
7. Logs potential vulnerabilities.
8. Generates a summary report.

---

## Logging

All scan activity is saved to:

```
logs/scan_results.txt
```

The log contains:

- Target URL
- Payload used
- HTTP status code
- Response length
- Response time
- Potential findings

---

## Testing

A local Flask application (`test_server.py`) is included with the project.

The test server intentionally returns SQL-like error messages when SQL Injection payloads are submitted. This allows the scanner to be tested safely without attacking real websites.

Example test URL:

```
http://127.0.0.1:5000
```

---

## Limitations

This scanner performs basic **error-based SQL Injection detection**.

It currently does not support:

- Boolean-based SQL Injection
- Time-based SQL Injection
- URL parameter scanning
- Cookie injection
- Authentication handling
- JavaScript-rendered forms

---

## Legal and Ethical Notice

This project is intended for educational purposes only.

Only scan web applications that you own or have explicit permission to test.

Suitable testing environments include:

- Local Flask test server
- DVWA (Damn Vulnerable Web Application)
- Other intentionally vulnerable web applications

Unauthorized scanning of third-party systems may violate laws or organizational policies.

---

## Author

**Farat Babayev**

Internship Project – SQL Injection Scanner