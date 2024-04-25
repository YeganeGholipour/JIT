import hashlib

hash_object = hashlib.sha1(b'HelWorld')

pbHash = hash_object.hexdigest()

print(pbHash)


# length = len(pbHash.decode("hex"))
