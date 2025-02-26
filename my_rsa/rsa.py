import random

def gcd(a, b):
    """Compute the Greatest Common Divisor (GCD) using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def is_prime(n, k=5):
    """Check if a number is prime using Miller-Rabin test."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    def miller_rabin(d, n):
        """Perform one iteration of the Miller-Rabin test."""
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        if not miller_rabin(d, n):
            return False
    return True

def generate_prime(bits=16):
    """Generate a random prime number with given bit length."""
    while True:
        num = random.getrandbits(bits) | (1 << bits - 1) | 1
        if is_prime(num):
            return num

def mod_inverse(e, phi):
    """Compute modular inverse using Extended Euclidean Algorithm."""
    a, b = e, phi
    x0, x1 = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
    return x0 % phi

def generate_keys(bits=16):
    """Generate RSA public and private keys."""
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Commonly used public exponent
    if gcd(e, phi) != 1:
        e = 3  # Fallback if 65537 is not coprime

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # Public and Private Key

def encrypt(message, public_key):
    """Encrypt a message using RSA."""
    e, n = public_key
    message_int = [ord(char) for char in message]
    cipher = [pow(m, e, n) for m in message_int]
    return cipher

def decrypt(ciphertext, private_key):
    """Decrypts the ciphertext using the private key."""
    try:
        d, n = private_key
        message_int = [pow(c, d, n) for c in ciphertext]

        # Validate Unicode range
        if any(m >= 0x110000 for m in message_int):
            raise ValueError("Error: Decryption failed. Invalid Unicode values detected.")

        message = ''.join(chr(m) for m in message_int)
        return message

    except TypeError:
        raise TypeError("Error: Invalid private key format.")
    except ValueError:
        raise ValueError("Error: Decryption failed. Possibly incorrect private key or corrupted ciphertext.")
