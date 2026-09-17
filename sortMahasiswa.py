import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    #kerjakan disini
    isi = maps[index]
    print(isi)
    n = len(data)
    for i in range(n):
        for j in range(n - 1):
            var_j      = data[j][isi]
            var_j_next = data[j + 1][isi]

            if rev == False:

                if var_j > var_j_next:
                    data[j], data[j + 1] = data[j + 1], data[j]

            elif rev == True:
                if var_j < var_j_next:
                    data[j], data[j + 1] = data[j + 1], data[j]
    # Jangan Dihapus
    show_data(data)

#sort_by(data)

sort_by(data, "presensi")       
#sort_by(data, "nim", rev=False)  
#sort_by(data, "nama")  
    
