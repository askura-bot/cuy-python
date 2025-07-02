import main4
from libs import welcome_massage_warung_mini
from services import db

def add():
    kode_barang = input("\nMasukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = int(input("Masukkan harga barang: "))
    stock_barang = int(input("Masukkan stock barang: "))
    
    db.create_item(kode_barang, nama_barang, harga_barang,stock_barang)
    
    
def check():
    items = db.read_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stock_barang = item[4]
        print (f'''
Kode: {kode_barang}
{nama_barang} | Rp {harga_barang}
Stock: {stock_barang}               
''')

def start():
    welcome_massage_warung_mini()
    while True:
        menu = int(input("Pilih menu: \n1. Tambah Barang \n2. Check Barang \n3. Kembali \n\nSilakan dipilih: "))
        if menu == 1:
            add()
        elif menu == 2: 
            check()
        elif menu == 3:
            main4.options()  
        else:
            break        
            
if __name__ == "__main__":
    start()