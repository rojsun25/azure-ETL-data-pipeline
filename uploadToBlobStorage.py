from azure.storage.blob import BlobServiceClient

storage_account_key = " "
storage_account_name = " "
connection_string = " "
container_name = " "

def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   
   with open(file_path,"rb") as data:
      blob_client.upload_blob(data)
      print(f"Uploaded {file_name}.")
      
# calling a function to perform upload
uploadToBlobStorage(' ',' ')