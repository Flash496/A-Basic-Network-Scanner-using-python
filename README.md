# The Basic Network Scanner 

This project is a simple and basic implementation of a network scanner. It is intended for educational purposes and can be beneficial for anyone interested in basic networking or who is looking for a project for their CSE course.

## Description

This is a Python project that consists of two files: `netscan.py` and `netscan_gui.py`. The `netscan.py` file provides the basic network scanning functionality using the `socket` module and the `concurrent.futures` module for concurrent port scanning. The `netscan_gui.py` file provides a basic graphical user interface (GUI) for the network scanner using the `tkinter` module. 

## Getting Started


The **`netscan.py`** file contains the following functions:

- `scan_port(target_ip, port)`: This function scans a specific port on the target IP address and checks if it is open. It uses the `socket` module to establish a connection to the target IP address and port. If the connection is successful, it prints a message indicating that the port is open.
- `scan_ports(target_ip, start_port, end_port)`: This function scans a range of ports specified by the `start_port` and `end_port` parameters. It uses the `concurrent.futures` module to concurrently scan multiple ports. The `scan_port` function is called for each port in the specified range.
- `main()`: This function prompts the user to enter the target IP address, start port, and end port. It then calls the `scan_ports` function to scan the specified range of ports.

The **`netscan_gui.py`** file contains the following functions:

- `scan_port(target_ip, port)`: This function is similar to the `scan_port` function in the `netscan.py` file. It scans a specific port on the target IP address and checks if it is open.
- `scan_ports(target_ip, start_port, end_port)`: This function is similar to the `scan_ports` function in the `netscan.py` file. It scans a range of ports specified by the `start_port` and `end_port` parameters. It uses the `concurrent.futures` module to concurrently scan multiple ports. The `scan_port` function is called for each port in the specified range.
- `scan_network()`: This function is called when the "Scan" button is clicked in the GUI. It retrieves the target IP address, start port, and end port from the GUI entry fields. It then calls the `scan_ports` function to scan the specified range of ports.
- `main()`: This function creates the GUI window, sets up the labels and entry fields, and defines the "Scan" button command. It runs the GUI main loop to display the interface.

### Executing the program
To use this project, simply run the `netscan_gui.py` file. The GUI interface will appear, and you can enter the target IP address, start port, and end port. Click the "Scan" button to initiate the network scan. The results will be displayed in a message box.

## Authors
Flash496
https://github.com/Flash496
