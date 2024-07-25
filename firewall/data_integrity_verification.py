from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def calculate_hash(data):
    # Create a SHA-256 hash object
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    # Update the hash object with data
    digest.update(data)
    # Finalize the hash computation and get the digest
    hash_value = digest.finalize()
    return hash_value

def verify_data_integrity(original_data, recovered_data):
    if original_data == recovered_data:
        print("Data integrity verified: Original and recovered data match.")
    else:
        print("Data integrity check failed: Original and recovered data do not match.")
        print("Details of differences:")
        # Find and print the first differing byte
        for i, (orig_byte, recov_byte) in enumerate(zip(original_data, recovered_data)):
            if orig_byte != recov_byte:
                print(f"Byte at index {i} differs: Original = {orig_byte}, Recovered = {recov_byte}")
                break
        # If the lengths are different, report that
        if len(original_data) != len(recovered_data):
            print(f"Lengths differ: Original = {len(original_data)}, Recovered = {len(recovered_data)}")

# Example usage:
if __name__ == "__main__":
    # Original data (could be read from a file, database, etc.)
    original_data = b"Original data to be backed up and recovered."

    # Simulated recovered data (after recovery process)
    recovered_data = b"Recovered data after backup and recovery."

    # Verify data integrity
    verify_data_integrity(original_data, recovered_data)
