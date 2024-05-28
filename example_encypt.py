import oci
config = oci.config.from_file()


# Initialize service client with default config file
key_management_client = oci.key_management.KmsCryptoClient(
    config, "https://ejtcsslqaahyi-crypto.kms.us-ashburn-1.oraclecloud.com")


encrypt_response = key_management_client.encrypt(
    encrypt_data_details=oci.key_management.models.EncryptDataDetails(
        key_id="ocid1.key.oc1.iad.ejtcsslqaahyi.abuwcljt5j23jrhqjtqmmtrappyo7vsifdielhmxaeslqgifs2as67opxb7q",
        plaintext="VGhpcyBpcyBhIHN1cGVyIHJhbW1pIHNlY3JldA==",
        key_version_id="ocid1.keyversion.oc1.iad.ejtcsslqaahyi.a4u7mzla4qqaa.abuwcljt7rbgwjyyb76rmgqzbj67wmpcuzghbelx35ibrcex5ng4oqder6jq"))

# Get the data from response
print(encrypt_response.data)