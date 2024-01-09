import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def random_prime():
    while True:
        num = random.randrange(2**8, 2**16)  
        if is_prime(num):
            return num

def random_coprime(phi):
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            return e

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1



def generate_keypair():
    # Generate two large prime numbers
    p = random_prime()
    q = random_prime()

    n = p * q

    # Compute the totient of n, phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and e is coprime to phi
    e = random_coprime(phi)

    # Compute d, the modular multiplicative inverse of e (mod phi)
    d = mod_inverse(e, phi)

    # Public key is (n, e), private key is (n, d)
    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

def main():
    public_key, private_key = generate_keypair()

    message = "Hello, RSA Encryption!"

    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()

