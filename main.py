import string
import random

def get_the_password(upper_count=2, digits_count=2, lower_count=2, symbols_count=2, ):
    upper = ''.join((random.choice(string.ascii_uppercase) for i in range(upper_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    lower = ''.join((random.choice(string.ascii_lowercase) for i in range(lower_count)))
    symbols = ''.join((random.choice(string.punctuation) for i in range(symbols_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(upper + digits + lower + symbols)
    random.shuffle(sample_list)

    # convert list to string
    final_password = ''.join(sample_list)
    print(final_password)
get_the_password()