class Bahan:
    def bumbu(self, bumbu, harga):
        self.bumbu = bumbu
        self.harga = harga
nmax = int(input())
data = []
for i in range(nmax):
    bumbu = str(input())
    harga = float(input())
    b = Bahan()
    b.bumbu(bumbu, harga)
    data.append(b)

for i in range(nmax):
    idx = i
    for j in range(i+1 ,nmax):
        if data[j].harga > data[idx].harga:
            idx = j
    data[i], data[idx] = data[idx], data[i]

for i in data:
    print(i.bumbu, i.harga)