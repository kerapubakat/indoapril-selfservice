# indoapril-selfservice
Pilot Project for Final Exam Python at Pacmann Batch 14

Aplikasi Self-service yang dapat diaplikasikan sebagai aplikasi sederhana untuk kemudahan berrbelanja, dengan fitur sederhana seperti login menggunakan **Unique-ID**, melihat dan menambahkan ke keranjang belanja, melakukan transaksi pembayaran serta pengiriman.

# Flowchart
Flowchart dari aplikasi IndoApril dapat dilihat di link berikut:
https://miro.com/app/board/uXjVMCRSFx0=/?share_link_id=80252952358

# Function dan Attribute
**Class Item**
Mempersentasikan item yang terdapat di IndoApril App

Attribute
- name: nama item
- price: harga item

**Class Customer**
Menyimpan data pelanggan

Attribute
- name: nama pelanggan
- address: alamat pelanggan
- id_customer: Unique ID pelanggan
- cart: Keranjang belanja

**Class Main menu**
Menu utama dari aplikasi
- add_item(name, price): Menambahkan item baru ke daftar item yang tersedia
- generate_id_customer(name): Menghasilkan unique id berdasarkan (nama+(len(self.customer)+1))
- main_menu(): Menampilkan menu utama dan menerima input dari pengguna.
- register_customer(): Mendaftarkan pelanggan baru
- select_item(id_customer): Memilih item yang akan dibeli oleh pelanggan
- available_items(): Menampilkan daftar item yang tersedia
- add_to_cart(customer, item): Menambahkan item ke keranjang belanja pelanggan
- view_cart(id_customer): Menampilkan isi keranjang belanja pelanggan
- edit_cart(id_customer): Mengedit isi keranjang belanja pelangga
- continue_to_payments(id_customer): Melanjutkan ke proses pembayaran
- select_payment(id_customer): Memilih metode pembayaran
- confirm_order(customer): Mengkonfirmasi pesanan dan menyelesaikan transaksi
- cancel_order(id_customer): Membatalkan pesanan
- clear_cart(customer): Mengosongkan keranjang belanja pelanggan
- calculate_total_price(id_customer): Menghitung total harga belanjaan pelanggan

Terima kasih telah berkunjung di repository saya, selamat berbelanja dan silahkan datang kembali!
