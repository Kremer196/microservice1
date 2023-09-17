import sys
import hashlib

inp = sys.stdin.readlines()
if inp:
    hash_func = inp[0].strip()
    message = '\n'.join(inp[1:]).strip()

    if hash_func in hashlib.algorithms_available:
        h = hashlib.new(hash_func)
        h.update(str.encode(message))

        print(h.hexdigest())
    else:
        print("Enter valid hash function, valid hash functions are: ", hashlib.algorithms_available)
else:
    print("Please provide a hash function and what you want to hash")