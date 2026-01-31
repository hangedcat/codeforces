rep: int = int(input())

for _ in range(rep):
    #variabel s = waktu yg dibutuhkan oleh hourglass agar semua pasirnya turun ke sisi satunya
    #variabel k = waktu yg lewat setiap kali flip dilakukan
    #variabel m = waktu sebelum mc pergi
    s, k, m = map(int, input().split(' '))
    #variabel f = flip yang dapat dilakukan mc sebelum dia pergi.
    f = (m // k)

    #disini kita lihat dlu kalau pasir hourglassnya itu udah habis sebelum dibalik dimana k lebih besar atau sama dengan s
    #maka logikanya f * k itu merepresentasikan berapa waktu yang berlalu setelah hourglassnya dibolka balik
    #lalu pada akhirnya ditambah oleh s karena setelah flip terakhir dan mcnya pergi, pasirnya akan turun tanpa gangguan.
    #maka akhirnya akan dapatlah di menit berapa pasir itu berhenti
    if (k >= s):
        end_time = (f * k + s)

    #nah kalau k lebih kecil dari s, dimana sebelum jam pasirnya habis mcnya udah flip.
    #kita harus cari tau dlu apakah flip terakhir itu ganjil atau genap?
    #karena ini menentukan flip terakhir sebelum mcnya pergi, antara pasirnya akan jatuh dalam waktu s atau k
    #kalau flip terakhir itu ganjil maka f(jumlah flip yg dilakukan mc) + 1 flip terakhir sebelum mc pergi, lalu dikalikan dengan k(menit pasir yg tersisa)
    #kalau flip terakhir itu genap maka f harus dikalikan dengan k terlebih dahulu baru akhirnya ditambah dengan s(waktu original yang dibutuhkan jam pasir)
    else:
        if f % 2 == 1:
            end_time = (f + 1) * k
        else:
            end_time = (f * k) + s
    
    #lalu pada akhirnya waktu dimana jam pasir berakhir yg direpresentasikan dengan variabel end_time
    #dikurang dengan m(waktu dimana mc pergi) untuk mencari berapa lama pasir masih akan turun setelah mc pergi
    #kalau minus, artinya sebelum mc pergi, pasirnya udah habis dimana kita gunakan max untuk memilih 0. 
    print(max(0, end_time - m))
