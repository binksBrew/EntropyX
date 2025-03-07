import string
import getpass
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def check_pwd():
    password = getpass.getpass(Fore.YELLOW + "\n🔑 Enter Password: ")
    strength = 0
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    # Strength Criteria
    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if special_count >=1:
        strength +=1
    if len(password) >= 12:
        strength += 1  # Bonus point for length

    # Strength Messages
    messages = {
        1: (Fore.RED + "⚠️ Very Bad Password! It's like a welcome mat for hackers. CHANGE IT NOW!"),
        2: (Fore.RED + "❌ Weak Password! This won't hold up against brute force attacks."),
        3: (Fore.YELLOW + "⚡ Not Bad! But still, I wouldn't trust it with my Netflix account."),
        4: (Fore.GREEN + "🔒 Strong Password! You're on the right track."),
        5: (Fore.GREEN + "🔥 Ultra Secure! This is the kind of password that laughs at hackers! 😎")
    }
    
    print(Fore.CYAN + "\n🔍 Password Analysis:")
    print(Fore.LIGHTWHITE_EX + f"✔️ {lower_count} lowercase letters")
    print(Fore.LIGHTWHITE_EX + f"✔️ {upper_count} uppercase letters")
    print(Fore.LIGHTWHITE_EX + f"✔️ {num_count} numeric characters")
    print(Fore.LIGHTWHITE_EX + f"✔️ {special_count} special characters")
    print(Fore.LIGHTWHITE_EX + f"✔️ Length: {len(password)} characters")
    
    print(Fore.MAGENTA + f"\n🛡️ Password Strength: {strength}/5")
    print(messages.get(strength, Fore.RED + "Something went wrong!"))

def ask_pwd(another_pwd=False):
    while True:
        prompt = 'Do you want to test another password? (y/n): ' if another_pwd else 'Do you want to check a password? (y/n): '
        choice = input(Fore.BLUE + prompt).strip().lower()
        
        if choice == 'y':
            return True
        elif choice == 'n':
            print(Fore.GREEN + "\n🎉 Thanks for using the Password Analyzer! Stay secure! 🔐")
            return False
        else:
            print(Fore.RED + "Invalid input! Try again.")

if __name__ == '__main__':
    print(Fore.CYAN + '+++ Welcome to the Ultimate Password Strength Checker +++')
    
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(True)
