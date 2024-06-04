import socket
import concurrent.futures

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
            # Perform service detection and output the identified service
    except (socket.error, socket.timeout) as e:
        print(f"Error occurred while scanning port {port}: {e}")

def scan_ports(target_ip, start_port, end_port):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        port_range = range(start_port, end_port + 1)
        futures = [executor.submit(scan_port, target_ip, port) for port in port_range]
        for future in concurrent.futures.as_completed(futures):
            future.result()

def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scan_ports(target_ip, start_port, end_port)

if __name__ == "__main__":
    main()
