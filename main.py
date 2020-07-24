import random
import csv

# VIKING_SCRIPT = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚺ", "ᚾ", "ᛁ", "ᛃ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛜ", "ᛟ", 
# "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]

VIKING_SCRIPT = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

CHRISTIAN_SCRIPT = []

class Encryption():

    def __init__(self, user_input, runic_string = ""):
        self.user_input = user_input
        self.runic_string = runic_string

    def __str__(self):
        return "{}".format(self.runic_string)
    
    
    def viking_encryption(self):
        
        runic = random.sample(VIKING_SCRIPT, 10)

        for i in runic:
            self.runic_string += i

        print(f"Your encrypted message is {self.runic_string}")

def Viking_Memory():

    with open('Viking_Record.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(row["Priest message"], row["Puritan message"])
            

if __name__ == "__main__":
    
    user_message = input("What message you wish to encrypt? ")
    unencrypted = Encryption(user_message)
    unencrypted.viking_encryption()

    Viking_Memory()

    with open("Viking_Record.txt", mode='w') as csv_file:
        fieldnames = ["Priest message", "Puritan message"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({"Priest message": user_message, "Puritan message" : unencrypted})

    