# This script pings a list of hostnames using the system's ping command and prints the output.
# Benefit: It helps check network connectivity to multiple servers automatically, useful for diagnostics or monitoring.

import subprocess  # Import the subprocess module to run external system commands

# List of hostnames to ping
host_list = ['www.arista.com', 'www.google.com']

# Loop through each host in the list
for host in host_list:
    print('host:' + host)  # Print the current host being pinged

    # Use subprocess to run the 'ping' command with 1 packet (-c 1)
    # Capture the command's output using stdout=PIPE
    p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE)

    # Run the command and get the output (and errors, if any)
    print(p.communicate())  # Print the result of the ping command