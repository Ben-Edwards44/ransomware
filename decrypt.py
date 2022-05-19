#Author: Ben-Edwards44
#Use to decrypt encrypted files


import os
from cryptography.fernet import Fernet


NO_DECRYPT = ["main.py", "key.key", "decrypt.py"]


def get_key(filename):
  with open(filename, "rb") as file:
    key = file.read()

    return key


def decrypt_files(files, key):
  for i in files:
    with open(i, "rb") as file:
      contents = file.read()

    decrypted = Fernet(key).decrypt(contents)

    with open(i, "wb") as file:
      file.write(decrypted)


def main():
  files = [i for i in os.listdir() if os.path.isfile(i) and i not in NO_DECRYPT]
  key = get_key("key.key")
  
  decrypt_files(files, key)
  
  
main()
