from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

# Load the private key from the PEM file
with open(r"C:\Security\Blogs\kms-export-keys\private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# The RSA-encrypted key (in base64 format)
encrypted_key_base64 = "ZWusoVgUV2tALNKKAabE5nVWSwCTlYSePl++i/BbUMHqwAT/v8jWWBQFzfiJy/FIsqp7/FvYFtdxS7/8/idvs+WI2BrTsJccbnzJw01HK5sNH2sUwSbnG51a4FV0MQkUp1grQJNNgOA7/E2EpT58U/45ICOr0oyiGnCkpAhizHEHyb3VWDPyAfjIHWnwtgnV9wZuqthvKLkAaHRcRVw5ijq0venn2yWKiKBscmnrk05Ih2yYZczf9tjiyBEy+WzGeyoukncTTwtmPnK6jwJE1Z05un/V5L125JuWPZO68ZMm2Vx8LxSsZLqfsS/ju64GM/VFUMYV2/gAgnqxZnYHrw=="

# Decode the base64 encoded encrypted key
encrypted_key = base64.b64decode(encrypted_key_base64)
print(encrypted_key)
# Decrypt the encrypted key using the private key
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print the decrypted key as a byte string
print("Decrypted Key (bytes):", decrypted_key)

# If you want to display the decrypted key as a hexadecimal string
print("Decrypted Key (hex):", decrypted_key.hex())
