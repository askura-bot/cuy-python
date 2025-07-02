from libs import welcome_massage, exit_programn
from games import monster
from tools import warung_mini
 
def options():
    welcome_massage()
    user_option = int(input("\nPilih menu: \n1. Monster Game \n2. Warung Mini \n3. Keluar Program \n\nSilakan dipilih: ")) 
    if user_option == 1:
        monster.start()
    elif user_option == 2:
        warung_mini.start()
    elif user_option == 3:
        exit_programn()
    else:
        print("\nSilakan pilih yang tersedia di menu\n")
        options()
    
def main():
    options()    
      
if __name__ == "__main__":
    main()  