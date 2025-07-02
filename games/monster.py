import random
import main4
from libs import welcome_massage_game

def start():
    welcome_massage_game()
    while True:
        monster_posisi = random.randint(1,5)
        gua_kosong = ["(  )"] * 5
        gua_monster = gua_kosong.copy()
        gua_monster[monster_posisi - 1] = "(0_0)"
        gua_kosong = '--'.join(gua_kosong)
        gua_monster = '--'.join(gua_monster)
        
        print(f"Halo, Perhatikan gua di bawah ini dan tebak monster berada di gua mana")
        print(gua_kosong)
        jawaban_user = int(input("Tebak monster berada di gua mana? (1/2/3/4/5): "))
        while jawaban_user < 1 or jawaban_user > 5:
            jawaban_user = int(input("Input jawaban antara 1 sampai 5 boyyy!!!: "))
        if monster_posisi == jawaban_user:
            print(f"\nSelamat kamu benar, monster berada di gua no {monster_posisi} dan tebakanmu di no {jawaban_user} \n {gua_monster}")
        else :
            print(f"\nMaaf kamu salah, monster berada di gua no {monster_posisi} dan tebakanmu di no {jawaban_user} \n {gua_monster}")
        
        ulang = input("\nApakah kamu ingin mencoba lagi? (y/n): ")
        if ulang == "n":
            main4.options()

if __name__ == "__main__":
    start()