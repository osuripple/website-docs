import os
import hashlib

def main():
    for file_name in os.listdir("en"):
        h = hashlib.md5()
        full_file_name = "/".join(("en", file_name))
        with open(full_file_name, "rb") as f:
            h.update(f.read())
        print(f"{h.hexdigest()}  {full_file_name}")


if __name__ == "__main__":
    main()
