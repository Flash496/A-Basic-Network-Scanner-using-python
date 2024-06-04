import socket
import concurrent.futures
import tkinter as tk
from tkinter import messagebox
from tkinter import font


def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
    except (socket.error, socket.timeout) as e:
        print(f"Error occurred while scanning port {port}: {e}")


def scan_ports(target_ip, start_port, end_port):
    open_ports.clear()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        port_range = range(start_port, end_port + 1)
        futures = [executor.submit(scan_port, target_ip, port) for port in port_range]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    if not open_ports:
        messagebox.showinfo("Scan Complete", "No open ports found.")
    else:
        open_ports_str = ', '.join(map(str, open_ports))
        messagebox.showinfo("Scan Complete", f"Open ports found: {open_ports_str}")


def scan_network():
    target_ip = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    scan_ports(target_ip, start_port, end_port)


# Create the main window
window = tk.Tk()
window.title("Network Scanner")

# Set font size
font_size = font.Font(size=20)

# Create labels
label_ip = tk.Label(window, text="Target IP:", font=font_size)
label_ip.grid(row=0, column=0, sticky=tk.W, padx=30, pady=30)

label_start_port = tk.Label(window, text="Start Port:", font=font_size)
label_start_port.grid(row=1, column=0, sticky=tk.W, padx=30, pady=30)

label_end_port = tk.Label(window, text="End Port:", font=font_size)
label_end_port.grid(row=2, column=0, sticky=tk.W, padx=30, pady=30)

# Create entry fields
entry_ip = tk.Entry(window, font=font_size)
entry_ip.grid(row=0, column=1, padx=30, pady=30)

entry_start_port = tk.Entry(window, font=font_size)
entry_start_port.grid(row=1, column=1, padx=30, pady=30)

entry_end_port = tk.Entry(window, font=font_size)
entry_end_port.grid(row=2, column=1, padx=30, pady=30)

# Create scan button
button_scan = tk.Button(window, text="Scan", command=scan_network, font=font_size)
button_scan.grid(row=3, column=0, columnspan=2, padx=30, pady=30)

# Initialize open ports list
open_ports = []

# Configure grid weights to expand the interface
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

# Run the GUI main loop
window.mainloop()
