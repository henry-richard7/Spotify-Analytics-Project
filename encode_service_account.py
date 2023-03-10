from base64 import b64encode
cred_path = input("Path of the GCP creds JSON file: ")
creds = open(cred_path,'r').read()

encode_creds = b64encode(creds.encode())
print(encode_creds.decode())