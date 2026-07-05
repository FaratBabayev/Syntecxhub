import socket
from concurrent.futures import ThreadPoolExecutor
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("Port " + str(port) + " is open")
        with open("scan_results.txt", "a") as file:
            file.write("Port " + str(port) + " is open\n")
    elif result == 10060:
        print("Port " + str(port) + " timed out")
        with open("scan_results.txt","a") as file:
            file.write("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")
        with open("scan_results.txt", "a") as file:
            file.write("Port " + str(port) + " is closed\n")
    sock.close()
try:
    host = input("Enter IP address or hostname: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    if start_port > end_port:
        print("Error: Starting port must be less than or equal to ending port.")
    else:
        ip = socket.gethostbyname(host)
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, port)
except ValueError:
    print("Error: Please enter valid port numbers.")
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
except KeyboardInterrupt:
    print("Scan cancelled by user.")