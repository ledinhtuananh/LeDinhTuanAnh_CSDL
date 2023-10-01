def find_duplicates(arr):
    # Tạo một danh sách (list) để đánh dấu các phần tử đã xem thấy
    max_num = max(arr)
    seen = [False] * (max_num + 1)
    
    # Duyệt qua mảng và kiểm tra các phần tử
    duplicates = []
    for num in arr:
        # Nếu phần tử đã được xem thấy trước đó, thì đây là phần tử trùng lặp
        if seen[num]:
            duplicates.append(num)
        else:
            seen[num] = True
    
    return duplicates

# Tạo một mảng ví dụ
my_array = [1, 2, 3, 1, 5]

# Gọi hàm để tìm các phần tử trùng lặp
duplicate_elements = find_duplicates(my_array)

# In kết quả
print("Các phần tử trùng lặp là:", duplicate_elements)
