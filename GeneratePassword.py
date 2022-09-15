import secrets
import string


def gen_pswd(length, lwr_case=True, upr_case=True, num=True, special_char=True):

    alphabet = ''

    if lwr_case:
        alphabet += string.ascii_lowercase

    if upr_case:
        alphabet += string.ascii_uppercase

    if num:
        alphabet += string.digits

    if special_char:
        alphabet += string.punctuation


    while True:
        password = ''

        contains_lwr = not lwr_case
        contains_upr = not upr_case
        contains_num = not num
        contains_spc = not special_char

        for _ in range(length):
            password += secrets.choice(alphabet)

        for char in password:

            if char in string.ascii_lowercase:
                contains_lwr = True

            elif char in string.ascii_uppercase:
                contains_upr = True

            elif char in string.digits:
                contains_num = True

            elif char in string.punctuation:
                contains_spc = True

        if contains_upr and contains_lwr and contains_num and contains_spc:
            break

    return password
