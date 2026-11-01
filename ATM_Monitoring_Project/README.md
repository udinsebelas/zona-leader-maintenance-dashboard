# Panduan Memulai Proyek Monitoring ATM (Django + PostgreSQL)

Selamat! Ini adalah starter kit untuk proyek aplikasi Data Analyst Anda.

## Struktur File:
1. `frontend/dashboard_operasional.html`: Ini adalah tampilan web interaktif (UI) yang bisa langsung dibuka di browser.
2. `database/schema.sql`: Script untuk membuat tabel di PostgreSQL.
3. `backend_django/models.py`: Rancangan tabel versi Python/Django.
4. `backend_django/views.py`: Contoh API untuk menghubungkan Frontend dan Database.

## Cara Menggunakan (Tahap Awal):

### 1. Melihat Hasil Frontend
Cukup buka folder `frontend/` dan klik dua kali (double-click) pada file `dashboard_operasional.html`. File ini akan terbuka di Chrome/Edge dan Anda bisa mencoba fitur "Catat Kunjungan" serta notifikasi Anti-Double Ticket.

### 2. Memulai Backend di VS Code
1. Buka aplikasi **Visual Studio Code (VS Code)**.
2. Pilih menu **File > Open Folder**, dan pilih folder tempat Anda mengekstrak ZIP ini.
3. Buka Terminal di VS Code (`Ctrl + \``).
4. Buat virtual environment: `python -m venv venv`
5. Aktifkan virtual environment:
   - Windows: `venv\Scripts\activate`
6. Install library yang dibutuhkan: `pip install -r requirements.txt`

### 3. Mengatur PostgreSQL
1. Buka aplikasi **pgAdmin** di laptop Anda.
2. Buat database baru bernama `db_operasional_atm`.
3. Buka Query Tool, lalu copy-paste isi file `database/schema.sql` dan klik **Run (Execute)**.
