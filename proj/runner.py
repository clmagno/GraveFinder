import socket
import subprocess

def get_local_ip():
    # Create a temporary socket to retrieve the local IP address
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a public IP address (Google's DNS server) to retrieve the local IP
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
    finally:
        # Close the temporary socket
        temp_socket.close()
    
    return local_ip

# Get the current IP address
current_ip = get_local_ip()

# Build the command to run the Django server with the current IP
command = f"python manage.py runserver {current_ip}:8000"

# Run the command
subprocess.run(command, shell=True)
