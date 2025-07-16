# Klasifikasi Sentimen Ulasan Produk Skintific

Aplikasi web ini dibuat menggunakan Django untuk melakukan klasifikasi sentimen (positif atau negatif) pada ulasan produk Skintific. Model yang digunakan adalah Support Vector Machine (SVM) yang telah dilatih sebelumnya.

## Instalasi

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/matchateens/Klasifikasi-Ulasan-Skintific.git
    cd Klasifikasi-Ulasan-Skintific
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependensi yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi

Untuk menjalankan server pengembangan lokal, gunakan perintah berikut:

```bash
python manage.py runserver
```

Buka browser Anda dan kunjungi `http://127.0.0.1:8000/` untuk melihat aplikasi.