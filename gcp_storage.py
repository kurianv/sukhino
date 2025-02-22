from google.cloud import storage
import os
storage_client = storage.Client()

BUCKET_NAME = "sukhino-chroma-db"
LOCAL_P_PATH = "./persistent_db"
GCS_PATH = "chroma/"

def upload_folder(bucket_name, local, gcs):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    for root, _, files in os.walk(local):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local)
            blob_path = os.path.join(gcs, relative_path).replace("\\", "/")  # Ensure compatibility for Windows
            blob = bucket.blob(blob_path)
            blob.upload_from_filename(local_path)

            print(f"Uploaded {local_path} to gs://{bucket_name}/{blob_path}")

upload_folder(BUCKET_NAME, LOCAL_P_PATH, GCS_PATH)




    

            




