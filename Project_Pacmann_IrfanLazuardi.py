"""
Original file is located at
    https://colab.research.google.com/drive/14VsHCb-ccYaK5xnJjF1DMv03Z-vud0ef
"""

import sys

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name, address, id_customer):
        self.name = name
        self.address = address
        self.id_customer = id_customer
        self.cart = {}


class IndoaprilApp:
    def __init__(self):
        self.customers = {}
        self.items = {}

    def add_item(self, name, price):
        item = Item(name, price)
        self.items[name] = item

    def generate_id_customer(self, name):
        return f'{name.lower().replace(" ","")}{len(self.customers) + 1}'

    def main_menu(self):
        while True:
            print("Indoapril Self-Service App")
            print("1. Log In ID Indoapril App")
            print("2. Daftar Member Baru")
            print("3. Exit")
            choice = input("Masukkan Pilihan (1-3): ")

            if choice == "1":
                id_customer = input("Ketik ID Indoapril App: ")
                if id_customer in self.customers:
                    self.select_item(id_customer)
                else:
                    print("Maaf, ID yang Anda masukkan salah atau tidak terdaftar, coba lagi.")
            elif choice == "2":
                self.register_customer()
            elif choice == "3":
                print("Terima kasih telah berbelanja di IndoApril Apps, silahkan datang kembali!")
                sys.exit() 
                """
                Link Referensi untuk code terkait
                https://superfastpython.com/thread-close/#Approach_3_Close_Thread_By_Exception
                """
            else:
                print("Tidak ada pilihan, coba lagi.")

    def register_customer(self):
        print("Daftar Member Baru")
        name_customer = input("Nama Anda: ")
        address_customer = input("Alamat Anda: ")
        id_customer = self.generate_id_customer(name_customer)
        customer = Customer(name_customer, address_customer, id_customer)
        self.customers[id_customer] = customer
        print("Registration successful!")
        print(f"Unique ID: {id_customer}")
        print("Silahkan login menggunakan ID Anda.")

    def select_item(self, id_customer):
        customer = self.customers[id_customer]
        print(f"Selamat datang, {customer.name}. Selamat Berbelanja!")
        self.available_items()

        while True:
            search_item = input("Silahkan ketik nama item yang Anda akan beli (atau 'lanjut' untuk melihat kantong belanjaan Anda): ")

            if search_item == "lanjut":
                self.view_cart(id_customer)
                continue

            item = self.items.get(search_item)
            if item:
                self.add_to_cart(customer, item)
            else:
                print("Maaf, item tidak tersedia.")

    def available_items(self):
        print("Daftar Item Tersedia:")
        for item in self.items.values():
            print(f"Item: {item.name}, Harga: Rp{item.price}")

    def add_to_cart(self, customer, item):
        quantity = int(input("Jumlah Barang: "))
        total_price = item.price * quantity

        customer.cart[item.name] = {
            'Kuantitas': quantity,
            'Harga': item.price,
            'Total': total_price
        }
        print(f"{item.name} sudah ditambahkan di kantong belanjaan Anda.")

    def view_cart(self, id_customer):
        customer = self.customers[id_customer]
        cart = customer.cart

        if not cart:
            print("Kantong Belanjaan Anda kosong :(.")
            return

        print("Kantong Belanjaan Anda")
        for name, item_info in cart.items():
            quantity = item_info['Kuantitas']
            price = item_info['Harga']
            total_price = item_info['Total']
            print(f"Item: {name}, Kuantitas: {quantity}, Harga: Rp{price}, Total: Rp{total_price}")

        while True:
            print("1. Lanjut Berbelanja")
            print("2. Edit Belanjaan Anda")
            print("3. Lanjut ke Pembayaran")
            choice = input("Masukkan Pilihan (1-3): ")

            if choice == "1":
                self.select_item(id_customer)
                break
            elif choice == "2":
                self.edit_cart(id_customer)
                break
            elif choice == "3":
                self.continue_to_payments(id_customer)
                return
            else:
                print("Tidak ada pilihan, coba lagi.")

    def edit_cart(self, id_customer):
        customer = self.customers[id_customer]
        cart = customer.cart

        if not cart:
            print("Belanjaan Anda kosong :(.")
            return

        print("Edit Belanjaan Anda")
        print("Ketik nama item yang ingin Anda ubah:")
        for name in cart.keys():
            print(name)

        item_to_edit = input("Ketik nama item yang ingin Anda ubah: ")

        if item_to_edit in cart:
            new_quantity = int(input("Masukkan jumlah baru (ketik '0' untuk menghapus item): "))
            if new_quantity > 0:
                item_info = cart[item_to_edit]
                item_info['Kuantitas'] = new_quantity
                item_info['Total'] = item_info['Harga'] * new_quantity
                print(f"Jumlah {item_to_edit} telah diubah menjadi {new_quantity}.")
            else:
                del cart[item_to_edit]
                print(f"{item_to_edit} telah dihapus.")
        else:
            print("Item tidak ditemukan di kantong belanjaan Anda.")

    def continue_to_payments(self, id_customer):
        print("Lanjut ke pembayaran:")
        final_price = self.calculate_total_price(id_customer)
        print(f'Total Belanjaan Anda: Rp{final_price}')

        if final_price >= 500_000:
            discount = 10
        elif final_price >= 300_000:
            discount = 8
        elif final_price >= 200_000:
            discount = 3
        else:
            discount = 0

        if discount > 0:
            discount_amount = (discount / 100) * final_price
            discounted_price = final_price - discount_amount
            print(f'Selamat, Anda mendapatkan diskon sebesar {discount}%.')
            print(f'Total Belanjaan Anda setelah diskon: Rp{discounted_price}')
        else:
            print(f'Belanjaan Anda kurang Rp{200_000 - final_price} untuk mendapatkan diskon.')

        while True:
            print("1. Opsi pembayaran")
            print("2. Batalkan Pembelian")
            choice = input("Masukkan Pilihan (1-2): ")

            if choice == "1":
                self.select_payment(id_customer)
                break
            elif choice == "2":
                self.cancel_order(id_customer)
                break
            else:
                print("Tidak ada pilihan, coba lagi.")

    def select_payment(self, id_customer):
        customer = self.customers[id_customer]
        print("Pilih metode pembayaran:")
        print("1. Debit")
        print("2. Credit Card")
        print("3. Pinjol")
        choice = input("Masukkan Pilihan (1-3): ")


        if choice in ["1", "2", "3"]:
            self.confirm_order(customer)
        else:
            print("Metode pembayaran tidak valid. Silakan coba lagi.")

    def confirm_order(self, customer):
        print(f"Hi {customer.name}, Orderan Anda telah dikirimkan ke {customer.address}.")
        print("Silahkan menunggu pengiriman. Terima kasih telah berbelanja di Indoapril App!")

        self.clear_cart(customer)

        while True:
            print("1. Belanja Kembali")
            print("2. Log off")
            end_choice = input("Masukkan Pilihan (1-2): ")

            if end_choice == "1":
                self.select_item(customer.id_customer) #kembali ke pilih item (tidak pelu login lagi)
                break
            elif end_choice == "2": #Kembali ke menu awal
                print("Logged off.")
                self.main_menu()
                break
            else:
                print("Tidak ada pilihan, coba lagi.")

    def cancel_order(self, id_customer):
        customer = self.customers[id_customer]
        self.clear_cart(customer)
        print("Pembelian Anda telah dibatalkan.")
        print("Terima kasih sudah menggunakan Indoapril App, silakan datang kembali.")

    def clear_cart(self, customer):
        customer.cart = {} #bersihin kantong belanjaan

    def calculate_total_price(self, id_customer):
        customer = self.customers[id_customer]
        total_price = sum(
            item_info['Total']
            for item_info in customer.cart.values()
        )
        return total_price


app = IndoaprilApp()
app.add_item("Mobil", 100000)
app.add_item("Mie", 5000)
app.add_item("Tempe", 3000)
app.main_menu()
