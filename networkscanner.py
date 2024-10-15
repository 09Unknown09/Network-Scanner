import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout for connection
            result = sock.connect_ex((ip, port))  # Returns 0 if the port is open
            if result == 0:
                return port
    except Exception:
        pass
    return None

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports

def main():
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
