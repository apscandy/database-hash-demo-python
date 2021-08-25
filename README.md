# **Salt and pepper demo**
This is a demo of how salt and pepper work in a theoretical aspect, and is intended for educational purposes. PLEASE DO NOT USE IN PRODUCTION

---
## **Why**

The question everyone will ask at some point, salt and pepper is indented to address the short comings of storing hashed passwords in a database. Ok so what are the aforementioned short comings, lets say two uses have the same passwords and we are using authentication model without salt or pepper in place, in the event a hacker gets access to the database the hacker can see who has the same password making it more effective for a hacker to crack one hash and get access to anyone with the same password.

## **Avalanche effect**

The avalanche effect is one of the most desirable effect in cryptography, So what is the avalanche effect, simply put if you change one single bit in the plain-text it snowballs and changes the output of the hash entirely. Cool right?, that means if I change the "A" in Andrew to "a" I get a different hash. Remember this as the concept will get taken to the extreme with salts.

## **Salt**

The process of salting a password is fairly simple it's just adding a random sequence of bits to the plain-text which subsequently triggers the avalanche effect from earlier. One down side is the salt typically gets stored in the database with the hash, so in the event a hacker gets access to the database they will have the salt to attempt a rainbow table attack. The next concept we will cover will help prevent this.

```python
def salt_generator()->str:
    salt = ''
    for _ in range(0, 64):
        salt += random.choice(string.ascii_letters+string.digits)
    return str(salt)
```

Here is an example of how you would generate a salt for a user, this one makes a salt of 64 character's making for a possible 
```
96 1963041904 1620901435 3125244491 2446413079 5720328478 1904170638 1939592816 6869436184 4273110973 8401260761 8805661696
``` 
combinations or 9.6196304190416 x 10^111.


## **Pepper**

## **Python code examples**