# Program Upload Foto

Program ini berjalan di terminal (jendela untuk mengetik perintah). Program
menyalin foto dari komputer ke folder `uploads` yang berada di sebelah file
`main.py`.

> **Catatan:** "Upload" di program sederhana ini berarti menyalin foto ke folder
> di komputer Anda. Foto tidak dikirim ke internet atau ke situs web.

## Yang perlu disiapkan

- Python 3 sudah terpasang di komputer.
- File foto yang ingin disalin. Format yang diterima: JPG, JPEG, PNG, GIF,
  WEBP, atau BMP.

Program ini hanya menggunakan fitur bawaan Python, jadi tidak perlu memasang
library tambahan.

## Cara menjalankan

1. Buka folder proyek ini.
2. Buka terminal di folder tersebut. Di Windows, Anda bisa membuka folder di
   File Explorer, klik bilah alamat, ketik `powershell`, lalu tekan Enter.
3. Ketik perintah ini dan tekan Enter:

   ```text
   python main.py
   ```

   Jika perintah `python` tidak dikenali, coba:

   ```text
   py main.py
   ```

4. Saat muncul pesan `Masukkan lokasi file foto:`, ketik atau tempel lokasi
   file foto, lalu tekan Enter. Contoh:

   ```text
   C:\Users\Nama\Pictures\liburan.jpg
   ```

   Jika lokasi memiliki spasi, Anda boleh menambahkan tanda kutip:

   ```text
   "C:\Users\Nama\My Pictures\foto liburan.jpg"
   ```

5. Setelah berhasil, program menunjukkan lokasi salinan foto. Foto tersimpan
   di folder `uploads` di dalam folder proyek. Buka folder proyek di File
   Explorer, lalu buka `uploads` untuk melihatnya.

## Contoh hasil

Jika foto bernama `liburan.jpg` berhasil disalin, hasilnya seperti ini:

```text
Foto berhasil disimpan di: ...\uploads\liburan.jpg
```

Foto asli tidak dihapus atau dipindahkan. Jika `liburan.jpg` sudah ada di folder
`uploads`, salinan baru diberi nama seperti `liburan_1.jpg` supaya file lama
tidak tertimpa.

## Jika terjadi kesalahan

- **File tidak ditemukan:** periksa kembali lokasi dan nama file. Pastikan
  lokasi tersebut menunjuk ke file foto, bukan hanya ke folder.
- **Format foto harus ...:** gunakan file dengan akhiran `.jpg`, `.jpeg`,
  `.png`, `.gif`, `.webp`, atau `.bmp`.
- **`python` tidak dikenali:** pastikan Python 3 terpasang, lalu coba perintah
  `py main.py`.
- **Gagal mengupload foto:** baca pesan setelah tulisan tersebut. Pesan itu
  menjelaskan penyebab yang dilaporkan komputer, misalnya akses ke folder
  ditolak.

## Penjelasan singkat kode

- `IMAGE_EXTENSIONS` berisi jenis file foto yang diterima.
- `upload_photo(...)` memeriksa file, membuat folder `uploads` bila perlu,
  lalu menyalin foto tanpa menimpa file bernama sama.
- `main()` meminta lokasi foto, menjalankan proses penyalinan, dan menampilkan
  hasilnya.
- Baris paling bawah memastikan `main()` dijalankan saat `main.py` dibuka
  langsung dengan Python.