import hashlib

# Open the script and create a signature hash
with open("keylogger.py", 'rb', buffering=0) as f:
        md5Hash= hashlib.file_digest(f, 'sha256').hexdigest()


# Save the hash
with open("hash.txt","w") as f:
    f.write(md5Hash)