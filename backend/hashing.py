import hashlib
import random
import string

def hash_password(password:str)->str:
    """
    Hashes the password for database storage
    
    Parameter:
        password (str): password intended to be hashed 

    Returns:
        hash (str): password hashed in md5

    Example:
        >>> password = 'Hello'
        >>> hash_password(password)
        '8b1a9953c4611296a827abf8c47804d7'
    """
    return hashlib.md5(str.encode(password)).hexdigest()

def salt_generator()->str:
    """
    Used to generate a salt for password processing

    Returns:
        salt (str): A random string of 64 character of [a-z A-Z 0-9]
    
    Why:
        In cryptography, the avalanche effect is the desirable property of cryptographic algorithms, 
        typically block ciphers and cryptographic hash functions, wherein if an input is changed slightly, 
        the output changes significantly.

    Combinations:
        5.164973859965254e114

    Example:
        >>> salt_generator()
        '0fYst66bDGTBi97El1rOzdbP0su8NOoAqNyYuekUb4Rav9WyYw6zOtjTqzhTHcn'
    """
    salt = ''
    for _ in range(0, 64):
        salt += random.choice(string.ascii_letters+string.digits)
    return str(salt)

def pepper(password:str)->str:
    """
    Reverses the given string
    
    Parameter:
        password (str): password intended to be peppered

    Returns:
        pepper (str): reversed sting

    Example:
        >>> password = 'Hello'
        >>> pepper(password)
        'olleH'

    """
    password = password[::-1]
    return password

def salt_hash_check(password:str, database_hash:str, database_salt:str)->bool:
    """
    Checking if the password + salt matchs the hash
    
    Parameter:
        password (str): plain text password
        database_hash (str): hash stored in the database
        database_salt (str): salt stored in the database

    Returns:
        True or False (bool):
    
    Example:
        >>> password = 'Hello'
        >>> hashed = '0e9862684b93ab22744fa77f907256ad'
        >>> salt = '0fYst66bDGTBi97El1rOzdbP0su8NOoAqNyYuekUb4Rav9WyYw6zOtjTqzhTHcn'
        >>> salt_hash_check(password, hashed, salt)
        True
    """
    password = pepper(password)
    password = hash_password(password + database_salt)
    if password == database_hash:
        return True
    else:
        return False

