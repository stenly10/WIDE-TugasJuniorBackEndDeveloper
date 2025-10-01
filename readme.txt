# Tugas Junior Back-End Developer PT Wide Technologies Indonesia

1. Bahasa pemrograman yang digunakan: Python

2. Algoritma bubble-sort dapat dilihat pada file bubble_sort.py method bubble_sort(arr). Proses bubble-sort dilakukan secara terbalik sehingga proses dimulai dengan memindahkan elemen terkecil ke indeks pertama dari list atau array.

3. Algoritma bubble-sort yang sudah dimodifikasi dapat dilihat pada file modified_bubble_sort.py pada method modified_bubble_sort(arr). Perbedaan dari algoritma bubble-sort sebelumnya adalah terdapat batasan pada inner loop di mana batas dari loop tersebut adalah i-1 dengan nilai i merupakan indeks iterasi outer loop. Hal ini dilakukan untuk membatasi proses perbandingan dan swap pada inner loop hanya pada range array yang belum terurut, sedangkan elemen-elemen terurut (elemen-elemen terkecil terurut setelah melalui proses pass sebelumnya) tidak akan dibandingkan kembali.

4. Modifikasi kode dengan pengecekan adanya proses swap dapat dilihat pada file with_break_bubble_sort.py pada method with_break_bubble_sort(arr) di mana terdapat suatu flag dengan variabel swap. Setiap terjadi proses swap, variabel swap akan diisi dengan nilai True sebagai penanda adanya proses swap pada pass tersebut. Setiap itu, dilakukan pengecekan nilai pada variabel swap pada setiap pass. Apabila variabel tersebut bernilai True, maka proses sorting akan dihentikan dengan melakukan break loop. Apabila bernilai False, proses akan dilanjutkan.

5. Berdasarkan kode versi nomor 4, perhitungan kompleksitas algoritma bubble-sort dapat dijabarkan sebagai berikut.
    - Worst case dari outer loop akan dijalankan dengan i bernilai 0 hingga n-1 dengan i adalah indeks dari outer loop dan n adalah banyak elemen pada array.
    - Worst case dari inner loop akan dijalankan sebanyak (n-2) - i + 1 = n-i-1.
    - Karena inner loop dijalankan berdasarkan indeks dari outer loop, maka total kompleksitasnya = (n-1) + (n-2) + ... + 0.
    - Total kompleksitas ini dapat disederhanakan menjadi n*(0 + (n-1))/2 = (n^2 - n)/2. Karena faktor paling besar dari kompleksitas ini adalah n^2/2, maka dapat disimpulkan kompleksitas dari algoritma ini adalah O(n^2).
