
from cryptography.fernet import Fernet
import base64
import hashlib
import os
# Function to decrypt files
def decrypt(encrypted_file: str, password: str, output_filename: str) -> None:
    '''
    Example usage
    decrypt('locked_data.tsv.enc', 'your_secure_password', 'unlocked_data.tsv')
    
    Input file should be in the working directory (not in sub directories)
    will output file in the working directory called output_filename
    '''
    # Generate a key from the password
    key = generate_key(password)

    # Load the encrypted content
    with open(encrypted_file, 'rb') as file:
        encrypted_content = file.read()

    # Decrypt the content
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content).decode()

    # Save the decrypted content to a new file
    with open(output_filename, 'w') as file:
        file.write(decrypted_content)

    print("Unlocked file created: unlocked_data")


# Example usage
#decrypt_tsv('locked_data.tsv.enc', 'your_secure_password')

#df = pd.read_csv('unlocked_data.tsv', sep='\t')

# Print the first column
#print(df.iloc[:, 0])  # iloc[:, 0] accesses the first column


def generate_key(password: str) -> bytes:
    # Hash the password to create a key
    password = password.encode()  # Convert to bytes
    salt = b'salt_'  # A salt to help with key generation
    key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    return base64.urlsafe_b64encode(key)
