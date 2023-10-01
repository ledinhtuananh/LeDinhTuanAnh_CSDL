def reverse_array_in_place(arr):
    # Xác định chiều dài của mảng
    n = len(arr)

    # Lặp qua mảng từ hai đầu và hoán đổi các phần tử
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

# Tạo một mảng
my_array = [1, 2, 3, 4, 5]

# Gọi hàm để đảo ngược mảng
reverse_array_in_place(my_array)

# In kết quả
print(my_array)
