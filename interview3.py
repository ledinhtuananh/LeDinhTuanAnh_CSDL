def reverse_integer(num):
    # Xác định dấu của số
    if num < 0:
        is_negative = True
        num = -num
    else:
        is_negative = False

    # Chuyển số thành chuỗi để dễ dàng đảo ngược
    num_str = str(num)

    # Đảo ngược chuỗi số
    reversed_str = num_str[::-1]

    # Chuyển lại thành số nguyên và bảo toàn dấu nếu có
    reversed_num = int(reversed_str)
    if is_negative:
        reversed_num = -reversed_num

    return reversed_num

# Nhập số nguyên cần đảo ngược
input_num = int(input("Nhap so nguyen: "))

# Gọi hàm để đảo ngược số
reversed_num = reverse_integer(input_num)

# In kết quả
print("So sau dao nguoc: ", reversed_num)
