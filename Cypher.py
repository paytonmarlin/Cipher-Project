#Create a function to encrypt a given string, uses the alphabet and encrypted lists
def encrypt(not_encrypted):

    message = []
    message_encrypt = ""
    
    for char in not_encrypted:
        index = alphabet.index(char)
        message_char = encrypted[index]
        message.append(message_char)

    for index in message:
        message_encrypt += index

    return message_encrypt

#Create a function to decrypt a given string, uses the alphabet and encrypted lists
def decrypt(encrypt):
    e_message = []
    message_decrypt = ""
    
    for char in encrypt:
        index = encrypted.index(char)
        message_char = alphabet[index]
        e_message.append(message_char)

    for index in e_message:
        message_decrypt += index

    return message_decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
encrypted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '<', '>', '?', '=', ' ']
test = encrypt("hello")
print(test)

test_1 = decrypt("74@@%")
print(test_1)

print("Welcome to the Secrety Message Encoder/Decoder")
print("-----------------------------------------------------")
again = True
while(again):
    print('''Options
    1. Encode a message
    2. Decode a message
    3. Exit''')
 
    user_input = input("\nWhat would you like to do? ")
    if user_input == "1":
        not_encrypted = input("\nEnter a message to Encode: ")
        string_encrypted = encrypt(not_encrypted)
        print("Encoded message: ", string_encrypted)
    elif user_input == "2":
        yes_encrypted = input("\nEnter a message to decode: ")
        string_decrypted = decrypt(yes_encrypted)
        print("Encoded message: ", string_decrypted)
    elif user_input == "3":
        again = False
    elif user_input in alphabet :
        print("Plese enter a number between 1 and 3\n")
    else:
        print(user_input, "is not a valid choice\n")
