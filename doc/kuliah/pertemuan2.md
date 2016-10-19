**Rangkuman Pertemuan 2 Sistem Keamanan Jaringan**

<p align="center">
  <img src="../../img/network.jpg" width="400px">
</p>

Latar Belakang Masalah

Setelah kita mempelajari Sistem Keamanan Jaringan kita akan mengerti betapa pentingnya Network Security dalam pembangunan aplikasi maupun aplikasi yang telah jadi agar data yang ada dalam aplikasi tersebut aman dan tidak mudah untuk diretas

1. Apa itu Vulnerabilities?
2. Apa yang ada pada layer TCP/IP?
3. Apa fungsi MAC Address?
4. Apa fungsi ARP Table?
5. Apa kelemahan DNS?
6. Bagaimana cara mengecek MAC Address pada IP Address?
7. Bagaimana cara mengetahui IP Address suatu Domain Web?
8. Bagaimana cara melalukan Vulnerabilities menggunakan Python?

Vurnerabilities adalah suatu sistem yang dimana terdapat kelemahan sehingga bisa di explore penyerang atau musuh yang mengakibatkan sistem tidak bekerja dengan baik

Pada TCP/IP semua berbasis port, untuk Application Layer sendiri terdapat HTTP : port 80, FTP : port 21 dan SSH : port 22, untuk Transport Layer terdapat TCP/IP, untuk Internet Layer terdapat IP Address, dan untuk Network Access Layer terdapat MAC Address

MAC Address pada jaringan computer berfungsi untuk komunikasi jaringan local seperti user atau PC dengan Router yang digunakan

ARP Table pada jaringan komputer berfungsi untuk mentransformasikan IP Address yang ada menjadi MAC Address

Untuk Kelemahan DNS dalam jaringan komputer adalah alamat domain yang digunakan dapat dipalsukan menggunakan IP Address yang berbeda

Cara mengecek MAC Address pada IP Address yang digunakan cukup mudah, kita hanya memerlukan Command Prompt atau Terminal dan memasukkan coding/code &quot; **arp –a**&quot; kemudian Enter, nanti akan muncul IP Address beserta MAC Address yang digunakan

Kemudian untuk mengetahui IP Address pada suatu domain seperti Web, kita juga hanya memerlukan Command Prompt atau Terminal untuk mengeceknya. Caranya cukup dengan memasukkan coding/code pada Command Prompt atau Terminal &quot; **nslookup namaweb**&quot; kemudian Enter, nanti akan muncul nama domain beserta IP Address yang digunakan

Untuk melakukan vulnerabilities pada Python pertama kita harus menginstall Python dan parameter – parameter lain yang diperlukan seperti Scapy dan lain – lain. Kemudian cek apakah Python sudah terinstall atau belum dengan coding &quot; **python**&quot; dan Enter, apabila muncul versi python maka python berhasil diinstal. Apabila kita menggunakan Linux atau Mac, kita tidak perlu lagi menginstall Python karena sudah terinstall secara default. Setelah selesai kita membuat script Python, kemudian jika selesai membuat scriptnya makan kita running atau jalankan dengan Command Prompt atau Terminal dengan cara &quot; **python namafilepython** (contoh gilang.py) **ipaddressyangdiserang ipaddress**** tujuan**&quot;. Jika semua langkah tersebut berhasil maka proses Vulnerabilities telah berhasil dilakukan

Penutup

Kesimpulan
Dari pernyataan diatas dapat disimpulkan bahwa vulnerabilities ini merupakan suatu cara meretas dengan menggunakan ip address yang dituju sehingga sistem/ip address yang diretas tidak dapat berjalan dengan baik

Saran
Saran saya sebaiknya pelajari vulnerabilities dengan baik agar dapat memahami cara menggunakannya, akan tetapi kita harus menggunakannya dengan benar agar tidak menyebabkan masalah yang besar dan merugikan orang lain

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Keamanan Jaringan

Link Github : https://github.com/gilangtartila99/SistemKeamananJaringan2016

Referensi : http://gankersmekti.blogspot.co.id/2014/03/makalah-vulnerability.html

Scan Plagiarisme

1. smallseotools - Link https://drive.google.com/open?id=0B5gySyqZ4GGoUGE2TDhoaWU1ZXM
2. serachenginereport - Link https://drive.google.com/open?id=0B5gySyqZ4GGoX2Z3NUlkV2xnZHc