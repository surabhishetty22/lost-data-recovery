import shutil
import os

def recover_data(backup_dir, target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)  # Delete existing directory
    shutil.copytree(backup_dir, target_dir)

backup_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\backup_storage\\backup"
target_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\important_data"

recover_data(backup_dir, target_dir)
print("Data recovered successfully!")
