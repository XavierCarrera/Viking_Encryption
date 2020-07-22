import random
import csv

VIKING_SCRIPT = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚺ", "ᚾ", "ᛁ", "ᛃ", "ᛇ", "ᛈ", "ᛉ", 
"ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛜ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]

class Encryption():

    def __init__(self, user_input):
        self.user_input = user_input
    
    
    def viking_encryption(self):

        runic = random.sample(VIKING_SCRIPT, 10)
        runic_string = ""

        for i in runic:
            runic_string += i

        print(f"Your encrypted message is {runic_string}")
        
        return runic_string
        

if __name__ == "__main__":
    
    user_message = input("What message you wish to encrypt? ")
    unencrypted = Encryption(user_message)
    unencrypted.viking_encryption()

    with open("Viking_Record.txt", mode='w') as csv_file:
        fieldnames = ["Priest message", "Puritan message"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({"Priest message": user_message , "Puritan message": unencrypted })

    