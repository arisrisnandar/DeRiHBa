# DeRiHBa: Perangkat Lunak Detektor Kematangan Pisang Tanduk
DeRiHBa ialah perangkat lunak detektor kematangan pisang tanduk segar dalam 7 kategori kematangan, di antaranya: hijau penuh (kategori 1/mentah), hijau agak kekuningan (kategori 2/mentah), hijau mendominasi kuning (kategori 3/mentah), kuning mendominasi hijau (kategori 4/matang), kuning penuh (kategori 6/matang), dan kuning penuh berbintik coklat (kategori 7/matang). DeRiHBa menggunakan model R-CNN yang sudah disesuaikan dengan kategori kematangan pisang tanduk.

**Fitur dan Keunggulan**

Fitur-fitur yang dikembangkan dan/atau dimodifikasi:
1.	Perangkat lunak DeRiHBa dirancang dan diaplikasikan dengan menggunakan algoritma berbasis pembelajaran-transfer yang menggabungkan 3 level model ResNet50 pada saat pra-pelatihan dengan resolusi yang berbeda untuk setiap pelatihan pada klasifikasi kematangan pisang tanduk.
2.	Pembelajaran mesin dengan model Faster R-CNN yang sudah disesuaikan dengan kategori kematangan pisang tanduk dengan algoritma pembelajaran-transfer pada dataset pisang tanduk yang berisi 7 (tujuh) kategori kematangan, di antaranya: banyak hijau (kategori 1/mentah), hijau agak kekuningan (kategori 2/mentah), hijau mendominasi kuning (kategori 3/mentah), banyak kuning (kategori 4/matang), kuning penuh (kategori 6/matang), dan kuning berbintik coklat (kategori 7/matang).
3.	DeRiHBa memiliki hasil yang lebih unggul dalam perhitungan kompleksitas komputasi dibandingkan dengan metodologi lainnya.
