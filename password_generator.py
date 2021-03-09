# -*- coding: utf-8 -*-

import random
import string


def generate_password(number: int) -> str:
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    full_string = []
    full_string.extend(list(lowercase))
    full_string.extend(list(uppercase))
    full_string.extend(list(digits))
    full_string.extend(list(punctuation))
    
    acceptable_length = 16
      
    if  number < acceptable_length:
        print("Your password must be at least 16 characters long. ")
        number = int(input("Type your password length: "))
        return generate_password(number)
    else:
        password = "".join(random.sample(full_string, number))
        if any(chr.isdigit() for chr in password):
            return password
        else:
            return generate_password(number)
        
    
    
