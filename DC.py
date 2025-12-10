meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO":"untuk menjadi agresif/marah"
            }


while True:
    print ("apa yang mau kamu lakukan ?")
    print( "1. menambah kata")
    print ("2. mencari kata")
    print ("3. tampilkan semua kata")
    jawaban = int (input ())
    if jawaban == 1:
        list_baru = input  ("masukkan kata yang ingin ditambahkan :")
        meme_dict[list_baru]=input("masukkan artinya:")
    elif jawaban == 2:
        kata = input("ketik kata yang ingin kamu cari")
        if kata in meme_dict.keys():
            print(meme_dict[kata])
        else :
            print ("kata yang kamu cari tidak ada")
    elif jawaban == 3 :
        print (meme_dict)
    else :
        print ("jawabanmu error")
