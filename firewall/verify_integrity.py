import hashlib
import os
import shutil

def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

def verify_integrity(original_hash, recovered_file_path):
    """
    Verify the integrity of data by comparing the hash values.
    """
    recovered_hash = calculate_hash(recovered_file_path)
    if original_hash == recovered_hash:
        print("Integrity verified: Data remains unchanged.")
    else:
        print("Integrity compromised: Data may have been altered or corrupted.")

def backup_file(source_file, backup_dir):
    """
    Backup a specific file to a backup directory.
    """
    shutil.copy2(source_file, backup_dir)  # Use copy2 to preserve metadata

# File path of the original data file
original_file_path = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\important_data\\1.txt"

# Backup directory
backup_dir = "C:\\Users\\shett\\OneDrive\\Desktop\\firewall\\backup_storage"

# Backup the original file
backup_file(original_file_path, backup_dir)

# Calculate the hash of the original data
original_hash = calculate_hash(original_file_path)

# File path of the recovered data file (after backup)
recovered_file_path = os.path.join(backup_dir, "1.txt")

# Verify integrity after recovery
verify_integrity(original_hash, recovered_file_path)
