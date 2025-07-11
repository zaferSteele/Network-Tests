"""
This script pings a list of hostnames (e.g., websites) once each to check their reachability 
and measure round-trip time. It determines the correct ping command flag based on the OS 
(-n for Windows, -c for Unix/Linux/macOS), executes the ping command, parses the output 
to extract the ping time using regex, and prints a summary list showing whether each host 
was reachable and how long the ping took (in milliseconds).
"""
import subprocess  # Used to run system commands like ping
import re  # Used for extracting patterns like ping time using regular expressions
import platform  # Used to detect the operating system

# List of hostnames to ping
host_list = ['www.juniper.com', 'www.google.com']
ping_times = []  # List to store (host, time) results

# Determine the correct ping command option based on the operating system
# Windows uses '-n' for count; Unix-based systems use '-c'
count_flag = '-n' if platform.system().lower() == 'windows' else '-c'

# Loop through each host in the list
for host in host_list:
    try:
        # Run the ping command with one packet
        result = subprocess.run(
            ['ping', count_flag, '1', host],  # Command to execute
            capture_output=True,  # Capture the output instead of printing it
            text=True,  # Return output as string instead of bytes
            timeout=5  # Timeout after 5 seconds if ping hangs
        )

        # Check if ping was successful (returncode 0 means success)
        if result.returncode == 0:
            # Try to find the ping time using a regular expression
            # This works for both Windows and Unix-style outputs
            match = re.search(r'time[=<]?(\d+(\.\d+)?) ?ms', result.stdout)
            time = match.group(0) if match else 'time not found'
        else:
            time = 'unreachable'  # Host did not respond

    except Exception as e:
        time = f'error: {e}'  # Catch any exception (e.g., timeout)

    # Save the result as a tuple (hostname, ping time)
    ping_times.append((host, time))

# Print the list of results
print(ping_times)
