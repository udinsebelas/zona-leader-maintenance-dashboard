from django.http import JsonResponse
from .models import MasterMesin, Kunjungan


# 1. API untuk Filter SN Berdasarkan Lokasi (Cascading Dropdown)
def get_sn_by_lokasi(request, id_unit):
    mesin_list = MasterMesin.objects.filter(cabang=id_unit).values(
        "sn_mesin", "tipe_mesin", "status_garansi"
    )
    return JsonResponse(list(mesin_list), safe=False)


# 2. API untuk Cek Jadwal Ganda (Double Ticket Validation)
def cek_jadwal_ganda(request, sn_mesin, tanggal):
    is_exists = Kunjungan.objects.filter(sn_mesin_id=sn_mesin, tanggal=tanggal).exists()
    return JsonResponse({"is_double": is_exists})
