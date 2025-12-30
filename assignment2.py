import numpy as np

def stat():
    # 1. populations.txt dosyasini yukle
    # (Dosyadaki # ile baslayan satiri ve e3 gibi formatlari otomatik okur)
    data = np.loadtxt('populations.txt')

    # 2. Hare sutununu al (Sutun indeksi 1)
    hare = data[:, 1]

    # 3. Hare populasyonunun en dusuk oldugu yili bul
    # En kucuk degerin indeksini bulup, o indeksteki yili (Sutun 0) aliyoruz
    min_index = np.argmin(hare)
    min_year_hare = data[min_index, 0]

    # 4. Lynx ortalamasini hesapla (Sutun indeksi 2)
    lynx_avg = np.mean(data[:, 2])

    # 5. new_data olustur ve sonuna turlerin toplamini ekle
    # Sadece turleri topluyoruz (Yil sutununu haric tutmak icin 1'den basliyoruz)
    # axis=1 diyerek satirdaki degerleri topluyoruz
    species_sum = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, species_sum))

    # 6. Carrot populasyonu 40000 alti olanlari 0 yap (Sutun indeksi 3)
    new_data[new_data[:, 3] < 40000, 3] = 0

    # 7. Istenen degiskenleri dondur
    return data, hare, min_year_hare, lynx_avg, new_data