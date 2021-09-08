import sqlite3
from backend import hashing 
from functools import wraps

connection_to_database = sqlite3.connect('passwords.db')
database_cursor = connection_to_database.cursor()


def database_creation(func):
    """
    Creates the database and tables if it dose not exist
    
    Tables:
        username (text):
        password (text):
        salt (text):
    """
    @wraps(func)
    def wrapper(*args, **kwargs)->None:

        database_cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
            username TEXT,
            password TEXT,
            salt TEXT)
            """)
        connection_to_database.commit()
        func(*args, **kwargs)
    return wrapper


def table_check(func):
    """Adds a try and excpet block for table functions"""
    @wraps(func)
    def wrapper(*args, **kwargs)->None:
        try:
            func(*args, **kwargs)
        except sqlite3.OperationalError:
            return "No table found"
        else:
            return func(*args, **kwargs)
    return wrapper
    

@database_creation
def database_add_user_salt_and_pepper(username:str, password:str)->None:
    """
    Adds a user to the database

    Parameter:
        username (str): username selected by the user  
        password (str): plain text password, will be salted and hashed before storage
    
    Example:
        >>> username = 'andrew'
        >>> password = 'Hello'
        >>> database_add_user_pass(username, password)
        >>> database_list_all()
        ('andrew', '0e9862684b93ab22744fa77f907256ad', '0fYst66bDGTBi97El1rOzdbP0su8NOoAqNyYuekUb4Rav9WyYw6zOtjTqzhTHcn')

    """
    if username_check(username):
        salt = hashing.salt_generator()
        password = hashing.pepper(password)
        password = password + salt
        password = hashing.hash_password(password)
        with connection_to_database:
            database_cursor.execute(
                'INSERT INTO passwords VALUES (:username, :password, :salt)', 
                {'username': username, 'password': password, "salt": salt})


@table_check
def database_find_user(username:str)->list:
    """
    Finds a user in the database

    Parameter:
        username (str): username selected by the user
    
    Returns:
        users (list): A list of all users in the database matching username
    
    Example:
        >>> username = 'andrew'
        >>> database_find_user(username)
        [('andrew', '0e9862684b93ab22744fa77f907256ad', '0fYst66bDGTBi97El1rOzdbP0su8NOoAqNyYuekUb4Rav9WyYw6zOtjTqzhTHcn')]
    """
    database_cursor.execute(
        "SELECT * FROM passwords WHERE username=:username", 
        {"username": username})
    return database_cursor.fetchall()


@table_check
def database_find_user_password(username:str)->str:
    """
    Finds a users password from there username

    Parameter:
        username (str): username selected by the user
    
    Returns:
        password (str): The users hashed password from the database
    
    Example:
        >>> username = 'andrew'
        >>> database_find_user_password(username)
        '0e9862684b93ab22744fa77f907256ad'

    """
    database_cursor.execute(
        "SELECT password FROM passwords WHERE username=:username", 
        {"username": username})
    return database_cursor.fetchone()[0]


@table_check
def database_find_user_salt(username:str)->str:
    """
    Finds a users salt from there username

    Parameter:
        username (str): username selected by the user
    
    Returns:
        salt (str): The users salt from the database
    
    Example:
        >>> username = 'andrew'
        >>> database_find_user_salt(username)
        '0fYst66bDGTBi97El1rOzdbP0su8NOoAqNyYuekUb4Rav9WyYw6zOtjTqzhTHcn'

    """
    database_cursor.execute(
        "SELECT salt FROM passwords WHERE username=:username", 
        {"username": username})
    return database_cursor.fetchone()[0]


@table_check
def database_list_all()->str:
    """returns all users in the database"""
    database_cursor.execute("SELECT * FROM passwords")
    output = ""
    for row in database_cursor.fetchall():
        output+= str(row)+'\n'
    return output.strip()


def database_delete_all()->None:
    """Deleles everything in the table"""
    with connection_to_database:
        database_cursor.execute('DELETE FROM passwords')

def username_check(username:str)->bool:
    """Check if username is taken"""
    try:
        database_cursor.execute(
            "SELECT username FROM passwords WHERE username=:username", 
            {"username": username})
        if database_cursor.fetchone()[0]:
            return False
    except TypeError:
        return True


