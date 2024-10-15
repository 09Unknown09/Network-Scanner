# network-scanner
# Simple Network Port Scanner

A simple network port scanner written in Python. This tool scans a specified IP address for open ports within a defined range. It utilizes Python's `socket` library and supports concurrent scanning for improved performance.

## Features

- Scans a specified range of ports on a target IP address.
- Reports open ports found during the scan.
- Utilizes multithreading for faster scanning.

## Requirements

- Python 3.x
- `socket` (included in the standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/09Unknown09/network-scanner.git
   cd port-scanner


No additional libraries are needed beyond Python's standard library.


Usage



1) Run the script:

bash
Copy code
python networkscanner.py

2) Enter the target IP address and the range of ports you want to scan when prompted.

Example

```bash
Copy code

Enter the IP address to scan: 192.168.1.1
Enter the starting port number: 1
Enter the ending port number: 1024
Scanning 192.168.1.1 from port 1 to 1024...
Open ports: [22, 80, 443]

Disclaimer

Use this tool responsibly and only on networks you own or have explicit permission to test. Scanning ports on networks without authorization may be illegal and unethical.
