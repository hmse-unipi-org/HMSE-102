# HMSE 102: Building Logic with Python

Selamat datang di pertemuan kedua pelatihan **Himpunan Mahasiswa Software Engineering (HMSE)**! Di pertemuan pertama kalian sudah mengenal dasar-dasar Python seperti variabel, tipe data, dan input/output. Sekarang saatnya kita membangun sesuatu yang lebih menarik: **logika program**.

Logika adalah inti dari pemrograman. Dengan logika, program bisa **mengambil keputusan** dan **melakukan perulangan** tanpa harus menulis kode yang berulang-ulang.

---

## Tujuan Pembelajaran

Setelah pertemuan ini, peserta diharapkan mampu:
- Memahami dan menggunakan **percabangan** (`if`, `elif`, `else`) untuk membuat keputusan dalam program
- Memahami dan menggunakan **operator logika** (`and`, `or`, `not`) serta **operator perbandingan** (`>`, `<`, `==`, `>=`, `<=`)
- Menggunakan **operator modulo** (`%`) untuk menentukan kelipatan
- Menulis **conditional expression** (ternary operator) untuk kode yang lebih ringkas
- Memahami dan menggunakan **perulangan** (`for`, `while`)
- Menggunakan **list** dan mengiterasinya dengan `for`
- Membuat program sederhana yang menggabungkan konsep-konsep di atas

---

## Materi yang Dibahas

### 1. Percabangan (Conditional Statements)

Percabangan memungkinkan program memilih jalur eksekusi berdasarkan kondisi tertentu. Python menggunakan kata kunci `if`, `elif` (else if), dan `else`.

**Contoh file `kondisi.py`:**

```python
telur = False
apel = False

if (telur and apel):
    print("Beli 5")
elif(telur):  # else if (telur)
    print("Beli 3")
elif(apel):
    print("Beli 2")
else:
    print("Beli 1")
```

Kode di atas memeriksa kondisi:
1. Jika **telur dan apel** keduanya `True`, maka output adalah `"Beli 5"`
2. Jika hanya **telur** `True`, maka output adalah `"Beli 3"`
3. Jika hanya **apel** `True`, maka output adalah `"Beli 2"`
4. Jika **tidak ada** yang `True`, maka output adalah `"Beli 1"`

**Contoh file `nilai.py`:**

```python
nilai = int(input("Masukkan nilai :"))
if(nilai > 80 and nilai < 100):
    print("A")
elif(nilai >= 60):
    print("B")
elif(nilai > 40 and nilai < 59):
    print("C")
elif(nilai >= 20):
    print("D")
else:
    print("E")
```

Program ini meminta input nilai dari pengguna, lalu menentukan grade berdasarkan rentang nilai yang ditentukan.

### 2. Conditional Expression (Ternary Operator)

Untuk kode yang lebih ringkas, Python menyediakan **conditional expression** dengan format:

```python
nilai_hasil = "Lulus" if nilai >= 80 else "gagal"
```

Ini setara dengan:

```python
if nilai >= 80:
    nilai_hasil = "Lulus"
else:
    nilai_hasil = "gagal"
```

### 3. Perulangan (Loops)

Perulangan memungkankan kita menjalankan blok kode berulang kali tanpa menulis kode yang sama berkali-kali.

#### a. `for` Loop dengan `range()`

Digunakan untuk mengulang sebanyak tertentu:

```python
for i in range(1, 10):
    print(i)
```

Fungsi `range(1, 10)` menghasilkan angka dari 1 sampai 9 (10 tidak termasuk).

#### b. `for` Loop dengan List

Kita bisa mengiterasi setiap elemen dalam list:

```python
buah = ["Mangga", "Apel", "Jeruk"]
for i in buah:
    print("Saya suka makan", i)
```

Output:
```
Saya suka makan Mangga
Saya suka makan Apel
Saya suka makan Jeruk
```

#### c. `while` Loop

Digunakan ketika jumlah perulangan tidak diketahui pasti, melainkan bergantung pada kondisi:

```python
i = 1
while i < 100:
    if i % 2 == 1:
        print(i)
    i += 1
```

### 4. FizzBuzz

**Contoh file `fizzbuzz.py`:**

```python
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**Aturan permainan:**
- Cetak angka dari 1 sampai 100
- Jika angka **kelipatan 3 dan 5**, cetak `"FizzBuzz"`
- Jika angka **kelipatan 3**, cetak `"Fizz"`
- Jika angka **kelipatan 5**, cetak `"Buzz"`
- Jika tidak memenuhi kondisi di atas, cetak angkanya sendiri

---

## Struktur File

| File | Deskripsi |
|------|-----------|
| `kondisi.py` | Contoh percabangan dengan operator logika dan conditional expression |
| `nilai.py` | Program penilaian siswa dengan percabangan bertingkat |
| `loop.py` | Contoh perulangan `for` dan `while`, serta iterasi list |
| `fizzbuzz.py` | Implementasi permainan FizzBuzz dengan perulangan dan percabangan |

---

## Cara Menjalankan

Pastikan Python sudah terinstal di komputer kalian. Lalu jalankan terminal di folder ini dan eksekusi:

```bash
python kondisi.py
python nilai.py
python loop.py
python fizzbuzz.py
```

Atau gunakan Python versi 3 secara eksplisit:

```bash
python3 kondisi.py
```

---

## Latihan

Setelah memahami materi di atas, coba kerjakan latihan berikut untuk menguji logika kalian:

1. **Latihan 1:** Ubah program `nilai.py` sehingga nilai `80` mendapat grade `"A"`. Hint: perhatikan operator perbandingan yang digunakan.

2. **Latihan 2:** Buat program yang meminta input suhu dalam Celsius, lalu:
   - Jika suhu > 35, cetak `"Panas sekali!"`
   - Jika suhu antara 20 sampai 35, cerak `"Cuaca sedang"`
   - Jika suhu < 20, cerak `"Dingin"`

3. **Latihan 3:** Buat program yang mencetak **bilangan genap** dari 1 sampai 20 menggunakan `while` loop dan operator modulo.

4. **Latihan 4:** Buat program FizzBuzz versi kalian sendiri dengan aturan:
   - Kelipatan 3 → `"Foo"`
   - Kelipatan 5 → `"Bar"`
   - Kelipatan 3 dan 5 → `"FooBar"`
   - Jika tidak, cetak angka seperti biasa

---

## Kesimpulan

Pada pertemuan ini, kalian telah mempelajari konsep fundamental dalam pemrograman:
- **Percabangan** → program bisa mengambil keputusan
- **Perulangan** → program bisa mengulang kode secara efisien
- **Logika** → menggabungkan keduanya untuk membuat program yang cerdas

Di pertemuan berikutnya, kita akan membahas fungsi dan modularisasi agar program kalian lebih terorganisir.

Selamat belajar dan jangan ragu untuk bereksperimen! 🚀

---

*Himpunan Mahasiswa Software Engineering — Pelatihan Mingguan*
