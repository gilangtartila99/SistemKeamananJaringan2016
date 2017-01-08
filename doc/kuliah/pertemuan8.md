**Rangkuman Pertemuan 8 Sistem Keamanan Jaringan**

<p align="center">
  <img src="../../img/snort.gif" width="400px">
</p>

Latar Belakang Masalah
1. Snort
2. Cara Instalasi Snort Pada CentOS

Snort
Snort adalah sebuah sistem open source untuk pencegahan penyusupan jaringan yang mampu melakukan analisis lalu lintas jaringan secara real-time dan packet logger pada jaringan IP. Snort juga dapat melakukan analisis protocol, konten pencarian atau pencocokan dan dapat digunakan untuk mendeteksi berbagai serangan.

Cara Instalasi Snort Pada CentOS
Sebelum menginstall snort, install dulu beberapa paket yang dibutuhkan snort untuk berjalan.

- # yum install libdnet libdnet-devel pcre pcre-devel gcc make flex byacc bison kernel-devel libxml2-devel wget -y

Selanjutnya membuat direktori atau folder untuk digunakan sebagai tempat instalasi.

- # mkdir /usr/local/src/snort

- # cd /usr/local/src/snort

Instalasi Libpcap.

- # wget http://www.tcpdump.org/release/libpcap-1.3.0.tar.gz -O libpcap.tar.gz

- # tar zxvf libpcap.tar.gz

- # cd libpcap-\*

- # ./configure &amp;&amp; make &amp;&amp; make install

- # echo &quot;/usr/local/lib&quot; &gt;&gt; /etc/ld.so.conf

- # ldconfig -v

Instalasi DAQ.

- # wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz -O daq.tar.gz

- # tar zxvf daq.tar.gz

- # cd daq-\*

- # ./configure &amp;&amp; make &amp;&amp; make install

- # ldconfig -v

Buat user dan group untuk snort.

- # groupadd snort

- # useradd -g snort snort
- Masuk ke folder snort dan instalasi snort.
- # cd /usr/local/src/snort

- # wget https://www.snort.org/downloads/snort/snort-2.9.9.0.tar.gz -O snort.tar.gz

- # tar zxvf snort.tar.gz

- # cd snort-2\*

- # ./configure –prefix /usr/local/snort –enable-sourcefire &amp;&amp; make &amp;&amp; make install

Kesimpulan
Jadi, snort adalah sebuah sistem open source untuk pencegahan penyusupan jaringan yang mampu melakukan analisis lalu lintas jaringan secara real-time dan packet logger pada jaringan IP.

Saran
Diharapkan memahami materi dan praktikumnya secara mendetail dan perhatikan setiap langkah proses instalasi Snort dengan baik dan benar.

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Keamanan Jaringan

Link Github : https://github.com/gilangtartila99/SistemKeamananJaringan2016

Referensi : 

1. https://www.snort.org/
2. https://rozzada.wordpress.com/2013/04/11/install-snort-centos-6-2-64bit/

Scan Plagiarisme

1. smallseotools - Link https://drive.google.com/open?id=0B5FSMUsdCMU4MWMyNDRtZ25CTU0
2. searchenginereport - Link   https://drive.google.com/open?id=0B5FSMUsdCMU4LVZReG9NSjhYaVE