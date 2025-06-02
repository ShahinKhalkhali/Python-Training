alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift numebr: "))

# TODO-1: Create function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs
# TODO-2: In encrypt() shift each letter forwards by a shift amount and print
# TODO-3: Call encrypt() and pass in the user inputs. You should be able to test the code and encrypt message
# TODO-4: What happens if you try to shift z by 9? Can you shift the code?