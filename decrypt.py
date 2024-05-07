import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

def decrypt_string(str):
    if str is None or str == "":
        return None

    try:
        # Assuming the key is "123!@#za"
        key = b"123!@#za"  # Using a fixed key

        cipher = DES.new(key, DES.MODE_ECB)

        # Decode the base64 encoded string
        decoded_bytes = base64.b64decode(str)
        
        decoded_bytes = base64.b64decode(decoded_bytes)

        # Decrypt the bytes
        decrypted_bytes = cipher.decrypt(decoded_bytes)

        # Unpad the decrypted data
        unpadded_data = unpad(decrypted_bytes, DES.block_size)

        # Convert bytes to string
        decrypted_string = unpadded_data.decode("utf-8")

        return decrypted_string
    except Exception as ex:
        print("Error:", ex)
        return None

# Example usage
encrypted_string = "YjVvTVMxbW1KUEhnQkp2UDhiV2VUdz09"
decrypted_string = decrypt_string(encrypted_string)
print("Decrypted string:", decrypted_string)
encrypted_string = "M2U3NS9YbjA1MUxWVlgvZUh1NEExdz09"
decrypt_string = decrypt_string(encrypted_string)
print("Decrypted string:", decrypted_string)

