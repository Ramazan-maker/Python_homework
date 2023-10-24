import hashlib

#username = "Vitaly"
passw = "1235"
salt = "ltvfunpabsnhy nl;rskruthg;osaihv lervyubatve4tlw8tybosei8tyeso54p8"

# hash = hashlib.md5()
# hash = hashlib.sha1()
hash = hashlib.sha512()

hash.update(passw.encode('utf-8'))
hash.update(salt.encode('utf-8'))

hash_string = hash.hexdigest()
print(hash_string)
