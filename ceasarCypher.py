#########################################################
###############      CAESAR CIPHER        ###############
#########################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs
# TODO-2: In encrypt() shift each letter forwards by a shift amount and print
# TODO-3: Call encrypt() and pass in the user inputs. You should be able to test the code and encrypt message
# TODO-4: What happens if you try to shift z by 9? Can you shift the code?

# Primitive encryption function (Longer)
def encrypt_prim(original_text, shift_amount):
    for i in range(len(original_text)):
        flag = False
        for j in range(len(alphabet)):
            if original_text[i].lower() == alphabet[j]:
                flag = True
                if (j + shift_amount) > 26:
                    shift_rem = shift_amount % 26
                    original_text[i] = alphabet[(j - 27) + shift_rem]
                    break
                else:
                    original_text[i] = alphabet[j + shift_amount]
                    break
            
        if flag == False:
            i += 1

    print("The Encrypted message is: " + display(original_text))

def display(modified_list):
    modified_text = ""
    for i in range(len(modified_list)):
        modified_text += str(modified_list[i])
    return modified_text

# Advanced encryption function (Shorter)
def encrypt_adv(original_text, shift_amount):
    modified_text = ""

    for i in original_text:                                         # i indexes along each character of original_text

        if i not in alphabet:                                       # Place current letter in constructed string
            modified_text += i                                      # if letter is not in alphabet

        else:
            shifted_position = alphabet.index(i) + shift_amount # i will be equal to the indexed character and 
                                                                # alphabet.index(i) will look for the letter
                                                                # associated to i then shift by shift_amount
            
            shifted_position = shifted_position % len(alphabet) # Assures that the index is within bounds of  
                                                                # alphabet's list

            modified_text += alphabet[shifted_position]         # Constructs string

    print(f"The encrypted message is: {modified_text}")

# TODO-1: Create a function called decrypt() that takes original_text and shift_amount as 2 inputs
# TODO-2: Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text
# TODO-3:   1) Combine the encrypt() and decrypt() functions into a single function called caesar()
#           2) Use the value of the user chosen direction variable to determine which functionality to use
#           3) Call the caesar function instead of encrypt/decrypt and pass in all three variables (ie: direction/text/shift)
# TODO-4: What happens if the user enters a number/symbol/space
# TODO-5: Figure out how to restart cipher program

def decrypt(original_text, shift_amount):
    modified_text = ""

    for i in original_text:

        if i not in alphabet:
            modified_text += i
        
        else:
            shifted_position = alphabet.index(i) - shift_amount
            shifted_position = shifted_position % len(alphabet)
            modified_text += alphabet[shifted_position]

    print(f"The decrypted message is: {modified_text}")

def caesar(direction, original_text, shift_amount):
    if direction.lower() == "encrypt":
        encrypt_adv(original_text, shift_amount)
    elif direction.lower() == "decrypt":
        decrypt(original_text, shift_amount)

def main():

    restart = True

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = input("Type the shift number: ")

    if shift.isdigit():
        shift_input = int(shift)
        caesar(direction, text, shift_input)
    else:
        print("Invalid shift amount, please choose a number\n")
        main()

    while restart == True:
        restart = input(f"Would you like to go again (y/n): ")
        if restart.lower() == "n":
            exit
        elif restart.lower() == "y":
            main()
        else:
            print("Invalid input, please choose 'y' or 'n'\n")
            restart = True

# # Primitive method
# chars_text = list(text)
# encrypt_prim(chars_text, shift)

main()