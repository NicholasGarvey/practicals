def main():
    min_length = 10

    password = get_password(min_length)
    password_asterisks(password)


def password_asterisks(password):
    print('*' * len(password))


def get_password(min_length):
    password = input("Please enter a password with {} characters".format(min_length))
    while len(password) < min_length:
        password = input("Enter password of at least {} characters: ".format(min_length))
    return password


main()
