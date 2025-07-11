"""
This script pings a list of hostnames once each and captures the output.
It extracts the host and ping time from the command output and stores them
as (host, time) tuples in a list. Finally, it prints the list of results.
Note: The code assumes a specific format of the ping output and works best on Unix-like systems.
"""

import subprocess  # Allows running system commands like 'ping'

# List of websites to ping
host_list = ['www.juniper.com', 'www.google.com']

# Empty list to store ping results
ping_time = []

# Loop through each host in the list
for host in host_list:
    # Run the 'ping' command with 1 packet using subprocess
    # The output is captured using PIPE
    p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    
    # Wait for the ping command to complete and get the result
    result = p.communicate()[0]

    # Extract the host IP or name from the result
    host = result.split()[1]  # Gets second word, usually the host

    # Extract the ping time (this assumes format like 'time=XX ms')
    time = result.split()[13]  # Gets 14th word, which may be 'time=XX ms'

    # Save the host and time as a tuple in the list
    ping_time.append((host, time))

# Print the list of ping results
print(ping_time)




    
