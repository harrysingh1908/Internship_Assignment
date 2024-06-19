import subprocess
import platform
import re

def get_default_gateway():
    system = platform.system()
    
    if system == "Windows":
        result = subprocess.run(["ipconfig"], capture_output=True, text=True).stdout
        # Find the default gateway using a regex pattern
        match = re.search(r"Default Gateway . . . . . . . . . : ([\d.]+)", result)
    else:  # Assuming Unix-like system
        result = subprocess.run(["netstat", "-rn"], capture_output=True, text=True).stdout
        match = re.search(r"0\.0\.0\.0\s+([\d.]+)", result)
        
    if match:
        return match.group(1)
    else:
        return "Default gateway not found"


# Example usage
gateway = get_default_gateway()
print(f"Default Gateway: {gateway}")
