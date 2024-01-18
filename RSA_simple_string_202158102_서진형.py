def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def genRSAKeys(n, e, d):
    publicKey = (n, e)
    privateKey = (n, d)
    return publicKey, privateKey

def modinv(a, n):
    temp = n
    b, c = 1, 0
    while n:
        q, r = divmod(a, n)
        a, n, b, c = n, r, c, b - q * c
    if a == 1:
        return (temp + b) % temp
    raise ValueError("Not invertible")

def find_d(e, phi_n):
    d = modinv(e, phi_n)
    return d
def calculate_phi(n):
    phi = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            phi -= phi // p  

        p += 1

    if n > 1:
        phi -= phi // n

    return phi

def RSADecrypt(ciphertext, privateKey):
    output = []
    n, d = privateKey
    for val in ciphertext:
        decrypted_val = pow(val, d, n)
        if 0 <= decrypted_val <= 0x10FFFF:
            output.append(chr(decrypted_val))
        else:
            print(f"Decrypted value {decrypted_val} is not a valid Unicode code point.")
    return "".join(output)

e = 3789479
n = 16695347

phi_n = calculate_phi(n)
d = find_d(e, phi_n)

print("개인 키 d:", d)
print(f"Φ(n) = {phi_n}")
bobPublicKey, bobPrivateKey = genRSAKeys(n,e,d)
print("bob's Public Key (n,e): ", bobPublicKey)
print("bob's Private Key (n,d): ", bobPrivateKey)

ciphertext = [1221847, 4795448, 11929767, 5886852, 2157475, 15309133, 12762586, 16082646, 3766899, 5637406, 2157475,
                  3983004, 7526959, 2157475, 8992392, 7362759, 7362759, 15309133, 5856642, 7526959, 3766899, 15087685,
                  15309133, 12762586, 14627653, 3766899, 5637406, 16082646, 12762586, 14627653, 3983004, 5856642,
                  8366708, 8366708, 3766899, 6004314, 4795448, 10888581, 10888581, 3983004, 3766899, 5136555, 3983004,
                  2157475, 10888581, 15741778, 8366708, 8366708]

decrypt = RSADecrypt(ciphertext, bobPrivateKey)
print("plaintext: ", decrypt)