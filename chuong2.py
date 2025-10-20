n = int(input("nhập số n:"))
ket_qua = 1
for i in range (1, n + 1):
    if n < 0 :
        print("không tính được vì k thể giai thừa âm ")
    if (n == 0 or n ==1):
        print("giai thừa bằng 1")
    else:
        ket_qua = ket_qua * i
        print(f"Giai thừa của {n} ({n}!) là: {ket_qua}")