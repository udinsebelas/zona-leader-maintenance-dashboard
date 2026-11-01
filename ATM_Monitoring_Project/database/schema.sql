-- 1. Tabel Master Mesin
CREATE TABLE master_mesin (
    sn_mesin VARCHAR(50) PRIMARY KEY,
    customer VARCHAR(100),
    cabang VARCHAR(100),
    kota VARCHAR(50),
    tipe_mesin VARCHAR(50),
    teknisi_pic VARCHAR(100),
    status_garansi VARCHAR(50)
);

-- 2. Tabel Kunjungan (Terhubung ke Master Mesin)
CREATE TABLE kunjungan (
    id SERIAL PRIMARY KEY,
    sn_mesin_id VARCHAR(50) REFERENCES master_mesin(sn_mesin),
    tanggal DATE,
    jenis VARCHAR(10),
    teknisi VARCHAR(100),
    catatan TEXT,
    status VARCHAR(50)
);
