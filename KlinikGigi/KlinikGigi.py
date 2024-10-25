"""
MIT License

Copyright (c) [2024] [Abdullah Azzam Rabbani]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
class KlinikGigi:
    def __init__(self):
        self.layanan = {
            "Pembersihan Gigi": 50000,
            "Pengobatan Gigi": 100000,
            "Pengobatan Gigi Berlubang": 150000,
            "Pengobatan Gigi Patah": 200000,
            "Pengobatan Gigi Rusak": 250000
        }
        self.diskon = {
            "Pembersihan Gigi": 0.1,
            "Pengobatan Gigi Berlubang": 0.2,
            "Pengobatan Gigi Rusak": 0.5
        }

        self.pembelian = []
        self.banyakJenisLayanan = 0
        self.statusBeli = False

    def formatrupiah(self,uang):
        y = str(uang)
        if len(y) <= 3:
            return 'Rp ' + y
        else:
            p = y[-3:]
            q = y[:-3]
            return self.formatrupiah(q) + '.' + p

    def tampilkan_layanan(self):
        print("Daftar Layanan:")
        for layanan, harga in self.layanan.items():
            print(f"{layanan}: Rp {harga}")

    def pilih_layanan(self):
        print("Pilih Layanan:")
        for i, layanan in enumerate(self.layanan.keys()):
            print(f"{i + 1}. {layanan}")
        self.banyakJenisLayanan = int(input("Masukan banyak layanan : "))
        i = 0
        if self.banyakJenisLayanan <= 0:
            print("Data Tidak Ada")
        else:
            while i < self.banyakJenisLayanan:
                pilihan = int(input(f"Masukkan nomor layanan ke {i+1}: "))
                if pilihan <= len(self.layanan.keys()):
                    layanan = list(self.layanan.keys())[pilihan - 1]
                    self.pembelian.append({
                            "layanan": layanan,
                            "biaya": self.hitung_biaya(layanan),
                            "diskon": self.hitung_diskon(layanan),
                            "hargaFinal" : int(self.hitung_biaya(layanan) - self.hitung_diskon(layanan) *100),
                        })
                    self.statusBeli = True
                    i = i + 1
                else:
                    print("Masukan Pilihan Dengan Benar!!,,")
                    i = 0


    def hitung_biaya(self, layanan):
        return self.layanan[layanan]

    def hitung_diskon(self, layanan):
        if layanan in self.diskon:
            return self.diskon[layanan]
        else:
            return 0

    def struk(self):
        print("")
        print("Sedang Mencetak Struk .....")
        print("")
        print("=" * 72)
        print(" " * 14, "Klinik Gigi", " " * 20)
        print("=" * 72)
        print(" No\tNama Layanan\t\t\tHarga Layanan\t\tDiskon\t\t\tHarga")
        print("-" * 72)
        total_pembelian = []

        for i, pembelian in enumerate(self.pembelian):
            nama = pembelian["layanan"]
            harga = pembelian["biaya"]
            diskon = pembelian["diskon"] * 100
            harga_final = pembelian["hargaFinal"]
            print(f' {i+1}\t{nama}\t\t\t{harga}\t\t{diskon}%\t\t\t{harga_final}')
            total_pembelian.append(harga_final)
        print("\nTotal Bayar : ", self.formatrupiah(sum(total_pembelian)))

    def main(self):
        while True:
            print("Selamat datang di Klinik Gigi!")
            print("1. Tampilkan Daftar Layanan")
            print("2. Pilih Layanan")
            print("3. Cetak Struk")
            try:
                pilihan = int(input("Masukkan pilihan: "))
                if pilihan == 1:
                    self.tampilkan_layanan()
                elif pilihan == 2:
                    self.pilih_layanan()
                elif pilihan == 3:
                    if self.statusBeli:
                        self.struk()
                        break
                    else:
                        print("Anda Belum Melakukan Pemilihan Menu")
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print(f"Masukan Pilihan dengan benar")

if __name__ == "__main__":
    klinik = KlinikGigi()
    klinik.main()