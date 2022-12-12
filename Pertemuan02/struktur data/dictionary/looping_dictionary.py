mahasiswa = {
  "Nama" : "Muhammad Hilmy",
  "Mata Kuliah" : "Dasar Dasar Pemrograman",
  "Nilai" : 95
}

# looping nilai (values)
for i in mahasiswa.values():
  print(i)

# looping kata kunci (keys)
for j in mahasiswa.keys():
  print(j)

for keys, values in mahasiswa.items():
  print(keys, ":", values)