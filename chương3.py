def hexToDec(hexNum):
    hexadecimals = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    hexNum = hexNum.upper()
    decimal_value = 0
    power = 0

    for digit in reversed(hexNum):
        if digit not in hexadecimals:
            print(f"Lỗi: '{digit}' không phải là ký tự Hexadecimal hợp lệ.")
            return None

        dec_digit = hexadecimals[digit]
        decimal_value += dec_digit * (16 ** power)
        power += 1

    return decimal_value

hex_input = input("Nhập số Hexadecimal cần chuyển đổi: ")

result = hexToDec(hex_input)

if result is not None:
    print(f"Giá trị thập phân: {result}")
else:
    print("Không thể chuyển đổi do đầu vào không hợp lệ.")