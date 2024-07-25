# import shutil
# import os
# import datetime

# def backup_data(source_dir, backup_dir):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")
#     shutil.copytree(source_dir, backup_folder)

# # Example usage:

# source_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\important_data"
# backup_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\backup_storage"

# backup_data(source_dir, backup_dir)
# print("Data backed up successfully!")

import shutil
import os
import datetime

def backup_data(source_dir, backup_dir):
    # Define the backup folder path
    backup_folder = os.path.join(backup_dir, "backup")
    
    # Remove the existing backup folder if it exists
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)
    
    # Copy the source directory to the backup folder
    shutil.copytree(source_dir, backup_folder)

# Example usage:
source_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\important_data"
backup_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\backup_storage"

backup_data(source_dir, backup_dir)
print("Data backed up successfully!")
