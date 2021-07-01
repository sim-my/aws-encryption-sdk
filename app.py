import os
import base64
import aws_encryption_sdk
from decouple import config

from s3 import upload_file, get_file_content

client = aws_encryption_sdk.EncryptionSDKClient()

kms_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(
    key_ids=[config('ENCRYPTION_KEY_ID')])


def get_file_name_and_extension(file):
    basename = os.path.basename(file)
    filename, file_extension = os.path.splitext(basename)

    return {"filename": filename, "file_extension": file_extension}


def encrypt_file_and_upload(file):
    file_to_encrypt = get_file_name_and_extension(file)
    file_name = file_to_encrypt["filename"]+file_to_encrypt["file_extension"]

    with open(file, "rb") as plaintext:
        file_64_encode = base64.encodebytes(plaintext.read())
        ciphertext, encryptor_header = client.encrypt(
            source=file_64_encode, key_provider=kms_key_provider
        )

        upload_file(ciphertext, file_name)


def get_file_content_and_decrypt(file):
    textfile = get_file_content(file)
    file_to_decrypt = get_file_name_and_extension(file)
    decrypted_file = 'files-after-decryption/decrypted_' + \
        file_to_decrypt["filename"]+file_to_decrypt["file_extension"]

    with open(decrypted_file, "wb") as plaintext:
        decrypted_plaintext, decrypt_header = client.decrypt(
            source=textfile, key_provider=kms_key_provider
        )
        plaintext.write(base64.decodebytes(decrypted_plaintext))
