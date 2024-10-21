
# Network-Scanner

Simple Network Port Scanner

A simple network port scanner written in Python. This tool scans a specified IP address for open ports within a defined range. It utilizes Python's socket library and supports concurrent scanning for improved performance.


Disclaimer

Use this tool responsibly and only on networks you own or have explicit permission to test. Scanning ports on networks without authorization may be illegal and unethical.
## Features

- Scans a specified range of ports on a target IP address.
- Reports open ports found during the scan.
- Utilizes multithreading for faster scanning.

## Requirement 
To run the **Simple Network Port Scanner**, you need the following:

- **Python**: Version 3.x is required. You can download it from [python.org](https://www.python.org/downloads/).

- **Dependencies**: This project uses Python's built-in `socket` library, which is included in the standard library, so no additional installation is necessary.

- **Operating System**: The tool is compatible with various operating systems, including:
  - Windows
  - macOS
  - Linux
## Installation
Follow these steps to install and set up the **Simple Network Port Scanner**:

1. **Clone the Repository**: Start by cloning the repository to your local machine using Git. Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/09Unknown09/network-scanner.git
   ```
   ```
   cd port-scanner

2. **Verify Python Installation**: Ensure you have Python 3.x installed. You can check your Python version by running:



```
python --version
```
If Python is not installed, you can download it from python.org and follow the installation instructions for your operating system.

3. **Run the Tool**: After installation, you can run the port scanner tool by executing:
Copy code
```
python3 network_scanner.py

```
4. **Enter the target**: IP address and the range of ports you want to scan when prompted.
Example:

```
Enter the IP address to scan: 192.168.1.1 Enter the starting port number: 1 Enter the ending port number: 1024 Scanning 192.168.1.1 from port 1 to 1024... Open ports: [22, 80, 443]
```
## Disclaimer 
Use this tool responsibly and only on networks you own or have explicit permission to test. Scanning ports on networks without authorization may be illegal and unethical.
## License

This project is licensed under the MIT License. See file for details [MIT](https://choosealicense.com/licenses/mit/)


## 🚀 About Me
I am a passionate cybersecurity student currently pursuing my Post Graduate program in Cybersecurity, where I am deepening my knowledge of network security, ethical hacking, and information protection. I am enthusiastic about understanding the complexities of cybersecurity threats and developing effective strategies to mitigate them.


In addition to my studies, I am currently doing an internship with Vault-Tec Security Company, where I am gaining hands-on experience in the field. During my internship, I have the opportunity to work alongside experienced professionals, engage in real-world security assessments, and contribute to safeguarding critical systems and data. This experience is invaluable as I apply theoretical knowledge to practical situations and learn the latest tools and techniques in the industry.

