from google.cloud import storage
import os

BUCKET_NAME = "sukhino-chroma-db"
GCS_PERSIST_PATH = "chroma/"
LOCAL_PERSIST_PATH = "./persisent_db/"

storage_client = storage.Client()

def upload():
    bucket = storage_client.bucket(BUCKET_NAME)

    for root, _, files in os.walk(LOCAL_PERSIST_PATH):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, LOCAL_PERSIST_PATH)
            blob = bucket.blob(os.path.join(GCS_PERSIST_PATH, relative_path))

            try:
                blob.upload_from_filename(file_path)
                print("uploaded")

            except Exception as e:
                print(f"Error {file_name}: {e}")

