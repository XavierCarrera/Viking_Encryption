import random
import csv

VIKING_SCRIPT = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚺ", "ᚾ", "ᛁ", "ᛃ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛜ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]


class Encryption:

    def __init__(self, user_input):
        self.user_input = user_input
    
    def message(self):
        
        saved_message = []
        saved_message.append(user_message)
        print(saved_message[0])
    
    def viking_encryption(self):

        runic = random.sample(VIKING_SCRIPT, 10)
        runic_string = ""

        for i in runic:
            runic_string += i

        print(f"Your encrypted message is {runic_string}")

if __name__ == "__main__":
    
    user_message = input("What message you wish to encrypt? ")
    unencrypted = Encryption(user_message)
    unencrypted.viking_encryption()
    



























