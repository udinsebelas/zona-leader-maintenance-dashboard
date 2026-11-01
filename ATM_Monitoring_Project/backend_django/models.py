from django.db import models


class MasterMesin(models.Model):
    sn_mesin = models.CharField(max_length=50, primary_key=True)
    customer = models.CharField(max_length=100)
    cabang = models.CharField(max_length=100)
    kota = models.CharField(max_length=50)
    tipe_mesin = models.CharField(max_length=50)
    teknisi_pic = models.CharField(max_length=100)
    status_garansi = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sn_mesin} - {self.cabang}"


class Kunjungan(models.Model):
    JENIS_KUNJUNGAN = [("PM", "Preventive"), ("CM", "Corrective")]

    sn_mesin = models.ForeignKey(MasterMesin, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jenis = models.CharField(max_length=2, choices=JENIS_KUNJUNGAN)
    teknisi = models.CharField(max_length=100)
    catatan = models.TextField()
    status = models.CharField(max_length=50)
