import oci
config = oci.config.from_file()


# Initialize service client with default config file
key_management_client = oci.key_management.KmsCryptoClient(
    config, "https://ejtcsslqaahyi-crypto.kms.us-ashburn-1.oraclecloud.com")


# Send the request to service, some parameters are not required, see API
# doc for more info
decrypt_response = key_management_client.decrypt(
    decrypt_data_details=oci.key_management.models.DecryptDataDetails(
        ciphertext="QclhwVOw9M/bBQhSWzTU9bXzCW//KNwnIelSM47ePQ56nPr/PKF6JMEjGtpxu8pV7PncVo+HgNgwr7mg6h0dWkU=",
        key_id="ocid1.key.oc1.iad.ejtcsslqaahyi.abuwcljt5j23jrhqjtqmmtrappyo7vsifdielhmxaeslqgifs2as67opxb7q"))

# Get the data from response
print(decrypt_response.data)