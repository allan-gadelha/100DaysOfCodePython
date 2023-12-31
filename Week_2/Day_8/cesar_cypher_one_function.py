#Alphabet Len = 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#My function that englobs both encrypt and decrypt
def caesar(plain_text, shift_amount, code_type):
    #Transforming text in a list, so it get easier to work with also getting the len of this list so we can use a loop
    list_text = list(plain_text)
    len_list_text = len(list_text)

    #For to iterate each letter in the list!
    for i in range(0, len_list_text):

        #Getting the specific letter for the iteration
        letter = list_text[i]
        
        #If theres a space in the user input this part serve to get the space into the answers without having a problem
        #since we're checking the alphabet list and theres no space there
        if letter == " ":
            list_text[i] = " "
            continue

        #In case the user types anything that's not in the alphabet list
        if letter not in alphabet:
            list_text[i] = letter
            continue

        #Getting the index where the specific letter is in the alphabet list
        index = alphabet.index(letter)


        # Everytime you have a list and if it need to keep circling like here for exemple, you just need to use the % operator, in this case % (size of the list)
        if code_type == "encode":
            #Calculate the new index
            new_index = (index + shift_amount) % len(alphabet)
            list_text[i] = alphabet[new_index]

        #Elif cause they're mutually exclusive
        elif code_type == "decode":
            #Calculate the new index
            new_index = (index - shift_amount) % len(alphabet)
            list_text[i] = alphabet[new_index]

    #Transforming it back into a string!
    print("".join(list_text))
    #Debugging
    #print(list_text)

while True:
    #User action, if he wants to encrypt or decrypt
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    #User Message
    text = input("Type your message:\n").lower()

    #The increases
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    continue_program = input("Do you want to continue? Type 'yes' to continue, or anything else to quit:\n").lower()
    if continue_program != 'yes':
        break