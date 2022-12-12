
def grade(nilai, nama, matkul):
  if nilai >= 85 and nilai <= 100:
    print("Nama Mahasiswa : ", nama)
    print("Mata Kuliah    : ", matkul)
    print("Nilai          : ", nilai)
    print("Nilai A")
  elif nilai >= 75 and nilai < 85:
    print("Nama Mahasiswa : ", nama)
    print("Mata Kuliah    : ", matkul)
    print("Nilai          : ", nilai)
    print("Nilai B")
  elif nilai >= 60 and nilai < 75:
    print("Nama Mahasiswa : ", nama)
    print("Mata Kuliah    : ", matkul)
    print("Nilai          : ", nilai)
    print("Nilai C")
  else:
    print("Nama Mahasiswa : ", nama)
    print("Mata Kuliah    : ", matkul)
    print("Nilai          : ", nilai)
    print("Nilai D")
  
grade(95, "Hilmy", "DDP")