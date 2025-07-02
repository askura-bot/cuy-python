import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_massage():
    star = "*" * (len(PC_NAME) + 6)
    print(star)
    print(f"** SELAMAT DATANG {PC_NAME} **")
    print(star)
    
def welcome_massage_warung_mini():
    star = "*" * (len("WARUNG MINI") + 6)
    print(star)
    print(f"** WARUNG MINI **")
    print(star)

def welcome_massage_game():
    star = "*" * (len("MONSTER GAME") + 6)
    print(star)
    print(f"** MONSTER GAME **")
    print(star)

def exit_programn():
    print("Program akan dihentikan dalam")
    sleep(1)
    print("3....")
    sleep(1)
    print("2....")
    sleep(1)
    print("1....")
    print("Program telah dihentikan")
    exit()
        
if __name__ == "__main__":
    welcome_massage()
    exit_programn()