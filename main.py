from pathlib import Path
import shutil

# Daftar akhiran nama file foto yang diterima program.
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}


def upload_photo(source_path, upload_directory):
    # Path membantu Python membaca dan mengolah lokasi file di komputer.
    source = Path(source_path).expanduser()

    # Pastikan file benar-benar ada dan jenis filenya termasuk format foto.
    if not source.is_file():
        raise FileNotFoundError(f"File tidak ditemukan: {source}")
    if source.suffix.lower() not in IMAGE_EXTENSIONS:
        raise ValueError("Format foto harus JPG, JPEG, PNG, GIF, WEBP, atau BMP.")

    destination_directory = Path(upload_directory)
    # Buat folder tujuan jika belum ada; folder yang sudah ada tidak dihapus.
    destination_directory.mkdir(parents=True, exist_ok=True)

    # Simpan dengan nama yang sama, kecuali nama itu sudah dipakai.
    destination = destination_directory / source.name
    if source.resolve() == destination.resolve():
        raise ValueError("Foto tersebut sudah berada di folder uploads.")

    # Jika ada nama yang sama, coba nama seperti foto_1.jpg, foto_2.jpg, dst.
    number = 1
    while destination.exists():
        destination = destination_directory / f"{source.stem}_{number}{source.suffix}"
        number += 1

    # Salin foto ke folder tujuan dan kembalikan lokasi hasil salinannya.
    shutil.copy2(source, destination)
    return destination


def main():
    print("=== Program Upload Foto ===")
    source_path = input("Masukkan lokasi file foto: ").strip()
    # Hapus tanda kutip yang kadang ikut tersalin saat menyalin lokasi file.
    if len(source_path) >= 2 and source_path[0] == source_path[-1] and source_path[0] in {"'", '"'}:
        source_path = source_path[1:-1]

    # Folder uploads dibuat di lokasi file main.py, bukan di lokasi foto asli.
    upload_directory = Path(__file__).resolve().parent / "uploads"

    # Tampilkan pesan yang mudah dipahami jika foto tidak bisa disalin.
    try:
        saved_path = upload_photo(source_path, upload_directory)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Gagal mengupload foto: {error}")
        return

    print(f"Foto berhasil disimpan di: {saved_path}")


if __name__ == "__main__":
    # Jalankan program hanya saat file ini dibuka langsung oleh Python.
    main()