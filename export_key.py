import oci
config = oci.config.from_file()

key_management_client = oci.key_management.KmsCryptoClient(
    config, "https://ejtcsslqaahyi-crypto.kms.us-ashburn-1.oraclecloud.com")


# Send the request to service, some parameters are not required, see API
# doc for more info
export_key_response = key_management_client.export_key(
    export_key_details=oci.key_management.models.ExportKeyDetails(
        key_id="ocid1.key.oc1.iad.ejtcsslqaahyi.abuwcljryb2c6huwsi4xejtvbnwydtkz732yde75wwrq5coe3dqj2l4izeaa",
        algorithm="RSA_OAEP_SHA256",
        public_key="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlyniaIQVRhpiy/pp1DTtFxteeZEpem+Lsvf1C25G9WflWX0nCLLuOlUFNGtjGg+REhGx+YhQeDNTQaFts+HHHCn8+cWpdyi+LYXpO786Flcf9clUoYQA8y3tNuu7gxdT+uRMcd1op2FOT85oYKwbA4ofIWNhM5HHnHsNS75UZb+A8ho8cp8LLJHdnHSp/rKAKAp68xH5r3v/w81o/3rMt+MNRb36HV8wDm1L5yTnCE3h21t2gMEOVsEDdwyrwr078PjZrAxd4sjub8jyFnO56H1sxpqWbBPoTTq2p7mThGDU2JYPN5n6hS6Ue13fFW7MZTIhM3HcBTQwPBUmULYnZwIDAQAB",
        logging_context={
            'EXAMPLE_KEY_Org57': 'EXAMPLE_VALUE_aDhCTq2ObrMBLELILR4p'}))

# Get the data from response
print(export_key_response.data)