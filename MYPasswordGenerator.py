import random

# Initialize everything needed - All possible results for the characters entered by user, the password, and the temporary password.

c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
p = [".", "?", "!", "@", "$", "%", "&"]

password = ""
temp_pass = []

while True:                 # The loop used for getting the desired length of the password from the user.
    try:
        pass_slot = int(input("How many characters long do you want your password?: "))                 # Asks user how long the password should be and sets desired length to a variable.
    except ValueError:                  # Just to make sure the user enters the right character type.
        print("Please enter an integer.")
        continue
    else:
        break

for i in range(0, pass_slot, 1):                    # The loop used for gathering the user's inputs.
    char = input("What character type would you like for this slot?  Select c for a capital letter, l for a lower case letter, n for a number, or p for punctuation: ")                 # Line to find out what the user wants each character to be in the password.
    char = char.lower()                 # Just in case the user enters a capital letter.

    # Code block that takes the character the user entered and randomly selects a character from the corresponding list of characters, then adds the randomly selected character to the temporary password.

    if char == "c":
        temp_pass.append(random.choice(c))
        continue
    elif char == "l":
        temp_pass.append(random.choice(l))
        continue
    elif char == "n":
        temp_pass.append(random.choice(n))
        continue
    elif char == "p":
        temp_pass.append(random.choice(p))
        continue
    else:
        print("Invalid input.  Enter either c, l, n or p.")                 # Just in case an unused character is accidently entered by the user.
        break

password = "".join(temp_pass)                   # The list of characters stored in temp_pass is joined together to make the user's password.

if len(password) != pass_slot:                  # Checks to make sure the length of the password that's been created matches the desired length the user entered.
    print("Please try again.")
else:
    print(password)                 # If everything worked correctly, this returns the newly created password.
