# 🐍 CUY-PYTHON

**CUY-PYTHON** adalah proyek Python sederhana namun seru yang berisi kumpulan mini-program, antara lain:
- 🎮 Permainan tebak gua monster
- 🛒 Sistem input dan pengecekan barang warung mini
- 📦 Koneksi langsung ke database MySQL untuk menyimpan data

## 🧠 Deskripsi Proyek

Proyek ini bertujuan untuk menggabungkan fitur-fitur Python interaktif yang melibatkan input pengguna, manipulasi data, dan modularisasi kode. Cocok untuk pemula yang ingin belajar tentang:
- Struktur folder Python yang rapi
- Fungsi dan import antar file
- Interaksi dengan basis data
- Penerapan permainan interaktif berbasis terminal

## 📁 Struktur Folder

```
cuy-python/
├── games/
│   └── monster.py           # Permainan tebak gua berisi monster
├── services/
│   └── db.py                # Koneksi dan fungsi MySQL
├── tools/
│   └── warung_mini.py       # Input & cek barang warung
├── libs.py                  # Fungsi utilitas seperti banner dan keluar
└── main4.py                 # Program utama dan menu
```

## ⚙️ Cara Menjalankan

1. **Clone Repository**
   ```bash
   git clone https://github.com/askura-bot/cuy-python.git
   cd cuy-python
   ```

2. **Pastikan Environment Siap**
   - Python 3.x telah terinstal
   - MySQL aktif dan memiliki database bernama `warung_mini` dengan tabel `tbl_barang`

3. **Jalankan Program Utama**
   ```bash
   python main4.py
   ```

## 🎮 Mini Game: Monster

Tebak di gua mana monster bersembunyi! Tersedia 5 gua dan visualisasi sederhana. Cocok untuk melatih intuisi dan keberuntungan 😄

## 🛍️ Warung Mini

Sistem kasir mini di terminal:
- Tambah barang (kode, nama, harga, stok)
- Lihat semua barang di database MySQL
- Navigasi menu interaktif

## 🛠️ Database MySQL

Pastikan sudah membuat:
```sql
CREATE DATABASE warung_mini;

CREATE TABLE tbl_barang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(20),
    nama_barang VARCHAR(255),
    harga_barang INT,
    stock_barang INT
);
```

## 📸 Tampilan Contoh

```
** SELAMAT DATANG CUY-PC **
Pilih menu:
1. Monster Game
2. Warung Mini
3. Keluar Program
```

## 🧩 Ide Pengembangan Selanjutnya

- Tambahkan autentikasi admin sebelum akses warung mini
- Simpan riwayat permainan monster
- Upgrade GUI menggunakan tkinter atau PyQt

## 📄 Lisensi

Proyek ini open-source dan bebas digunakan untuk pembelajaran maupun pengembangan lebih lanjut.