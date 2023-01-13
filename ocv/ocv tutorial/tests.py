import matplotlib.pyplot as plt

class Mobil:

    def __init__(self):
        self.daftar_kendaraan = {'Nomor Polisi Mobil' : ['AB 1273 JWZ', 'AB 3256 GIL','1'], 'Nomor Polisi Motor' : ['AB 7863 WER']}
        self.daftar_member = {'Nomor Polisi Mobil' : ['AB 1273 JWZ', 'AB 3256 GIL'], 'Nomor Polisi Motor' : ['AB 7863 WER']}
        self.limitParkirMobil = 10
        self.limitParkirMotor = 20
        self.tag = 0
        self.login()

    def visualKey(self):
        data = {'Parkiran kosong\nuntuk Motor': self.limitParkirMotor - len(self.daftar_kendaraan['Nomor Polisi Motor']), 'Jumlah Motor\nyang ada': len(self.daftar_kendaraan['Nomor Polisi Motor']),
                'Parkiran kosong\nuntuk Mobil': self.limitParkirMobil - len(self.daftar_kendaraan['Nomor Polisi Motor']), 'Jumlah Mobil\nyang ada': len(self.daftar_kendaraan['Nomor Polisi Mobil'])}
        jenis = list(data.keys())
        jumlah = list(data.values())
        fig = plt.figure(figsize=(10, 6))
        plt.locator_params(axis="both", integer=True, tight=True)
        plt.barh(jenis, jumlah, color='blue')

        plt.xlabel(f"Jumlah Kendaraan")
        plt.title("Parkiran")
        plt.grid()
        plt.show(block=False)
        plt.pause(5) # 5 detik
        plt.close("all")

    def login(self):
        print('=' * 20)
        print('selamat datang di aplikasi pemesanan parkir')
        username = input('apakah anda ingin melakukan pemesanan ? : 1. yes | 2. no : ')
        if username == '1':
            print('Selamat datang')
            self.main_menu()
        else:
            print('terima kasih telah berkunjung')

    def main_menu(self):
        if self.tag == 0:
            pass
        else:
            self.visualKey()
            self.tag = 0

        print('=' * 10, 'MAIN MENU pemesanan PARKIR', '=' * 10)
        print('selamat datang di aplikasi pemesanan parkir')
        print('=' * 20, 'masukan input aplikasi', '=' * 20)
        print('1. pemesanan')
        print('2. Pendaftaran Member')
        print('3. exit application')
        pilihan = input('pilih menu: ')
        if pilihan == '1' :
          self.transaksi()
        # fix one
        elif pilihan == '2' :
          self.member()
        elif pilihan == '3' :
          self.exit_menu()
        else:
            print("Pilihan tidak tersedia, kembali ke main menu.")
            self.main_menu()

    def exit_menu(self):
        print('Terima kasih telah berkunjung')
        exit()


    def transaksi(self):
        print('Masukkan jenis kendaraan')
        print('1. Mobil| 2. Motor')
        pilihan = input('Masukkan jenis kendaraan: ')
        if pilihan == '1' :
          print("mengecek ketersediaan slot parkir")
          if len(self.daftar_kendaraan['Nomor Polisi Mobil']) >= self.limitParkirMobil:
              print("slot parkir tidak tersedia")
              print('kembali ke menu utama')
              self.main_menu()
          else:
              print('slot parkir tersedia')
              print('silahkan masukan data kendaraan')
              nopolisi = str(input('Masukkan Nomor Polisi: '))
              masuk = float(input('Masukan jam masuk(0 - 24): '))
              keluar = float(input('Masukkan jam keluar(0 - 24): '))
              if nopolisi in self.daftar_kendaraan['Nomor Polisi Mobil']:
                    print('kendaraan anda telah terdaftar')
                    self.main_menu()
              else :
                    self.tag += 1
                    self.daftar_kendaraan['Nomor Polisi Mobil'].append(pilihan)
                    lama_parkir = keluar - masuk
                    tagihan = 4000 + (lama_parkir - 1) * 2000
                    print('mengecek membership')
                    if nopolisi in self.daftar_member['Nomor Polisi Mobil']:
                        diskon = tagihan * 10/100
                        bayar = tagihan-diskon
                        print('anda terdaftar sebagai member')
                        print('='*15)
                        print('Jogja City Mall Parking System')
                        print('Waktu Parkir: ', lama_parkir, 'hours')
                        print('Biaya Parkir: ','Rp', bayar)
                        print('Anda mendapat diskon member sebesar 10%')
                        print('Terimakasih')
                        print('='*15)
                        self.main_menu()
                    else :
                        print('anda tidak terdaftar sebagai member')
                        print('='*15)
                        print('Jogja City Mall Parking System')
                        print('Waktu Parkir: ', lama_parkir, 'hours')
                        print('Biaya Parkir: ','Rp', tagihan)
                        print('Terimakasih')
                        print('='*15)
                        self.main_menu()
        if pilihan == '2' :
          print("mengecek ketersediaan slot parkir")
          if len(self.daftar_kendaraan['Nomor Polisi Motor']) >= self.limitParkirMotor:
              print("slot parkir tidak tersedia")
              print('kembali ke menu utama')
              self.main_menu()
          else:
              self.tag += 1
              nopolisi = str(input('Masukkan Nomor Polisi: '))
              masuk = float(input('Masukan jam masuk(0 - 24): '))
              keluar = float(input('Masukkan jam keluar(0 - 24): '))
              if nopolisi == self.daftar_kendaraan['Nomor Polisi Motor']:
                    print('kendaraan anda telah terdaftar')
                    self.main_menu()
              else :
                    self.daftar_kendaraan['Nomor Polisi Motor'].append(nopolisi)
                    lama_parkir = keluar - masuk
                    tagihan = 4000 + (lama_parkir - 1) * 2000
                    print('member check...')
                    if nopolisi in self.daftar_member['Nomor Polisi Motor']:
                        diskon = tagihan * 10/100
                        bayar = tagihan-diskon
                        print('anda terdaftar sebagai member')
                        print('='*15)
                        print('Jogja City Mall Parking System')
                        print('Waktu Parkir: ', lama_parkir, 'hours')
                        print('Biaya Parkir: ','Rp', bayar)
                        print('Anda mendapat diskon member sebesar 10%')
                        print('Terimakasih')
                        print('='*15)
                        self.main_menu()
                    else :
                        print('anda tidak terdaftar sebagai member')
                        print('='*15)
                        print('Jogja City Mall Parking System')
                        print('Waktu Parkir: ', lama_parkir, 'hours')
                        print('Biaya Parkir: ','Rp', tagihan)
                        print('Terimakasih')
                        print('='*15)
                        self.main_menu()
        else :
          print('input yang anda masukkan salah')
          self.transaksi()

    def member(self):
        print('Silahkan masukan data kendaraan')
        kendaraan = input('Masukkan Jenis Kendaraan: 1. Mobil|2. Motor: ')
        nopolisi = input('Masukkan Nomor Polisi: ')
        if kendaraan == 1:
          self.daftar_member['Nomor Polisi Mobil'].append(nopolisi)
        if kendaraan == 2:
          self.daftar_member['Nomor Polisi Motor'].append(nopolisi)
        else:
          self.daftar_member['Nomor Polisi Mobil'].append(nopolisi)
        print('pendaftaran member selesai')
        kembali = input('kembali ke menu..? 1. Yes|2. No|3. Exit app : ')
        if kembali == '1':
            self.main_menu()
        elif kembali == '2':
            self.member()
        elif kembali == '3':
            self.exit_menu()
        else:
          print('Pilihan tidak tersedia, kembali ke menu utama')
          self.main_menu()

mobil = Mobil()

