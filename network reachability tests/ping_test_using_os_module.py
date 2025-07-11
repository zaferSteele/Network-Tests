# This script pings a list of hostnames using the system's ping command via os.system().
# Benefit: It provides a quick and simple way to test network connectivity to multiple servers.
# Note: Unlike subprocess, os.system() directly executes the command and prints output to the console without capturing it.

import os  # Import the os module to execute system-level commands

# List of hostnames to ping
host_list = ['www.cisco.com', 'www.google.com']

# Loop through each host in the list
for host in host_list:
    # Run the ping command using os.system and print the result to the terminal
    os.system('ping -c 1 ' + host)
