from database_utils import *
from hashing import *

username = "linus"
password = "Hello world"


if __name__ == "__main__":
    #database_add_user_salt_and_pepper(username, password)
    #print(database_find_user(username))
    #print(database_find_user_password(username))
    #print(hash_check('Hello', str(database_find_user_password(username)[0])))
    #print(salt_generator())
    print("\n"+database_list_all()+"\n")
    #print(database_user_login("andrew", "Hello"))
    #print(hash_password(password))
    #print(database_find_user_salt(username))
    #user_pass = database_find_user_password(username)
    #user_salt = database_find_user_salt(username)
    #print(salt_hash_check(password, user_pass, user_salt))
    #database_delete_all()
    #print(hash_password("passw0rd"))