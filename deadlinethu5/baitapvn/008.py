def bubblesort(A):
    # Định nghĩa một hàm tên là bubblesort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    for passer in range(n-1, 0, -1):
        # Vòng lặp ngoài cùng, vòng lặp này lặp qua từng lần đi qua toàn bộ mảng (passer).
        for i in range(passer):
            # Vòng lặp trong, lặp qua từng phần tử của mảng từ 0 đến passer-1.
            if A[i] > A[i+1]:
                # So sánh phần tử hiện tại (A[i]) với phần tử kế bên (A[i+1]).
                temp = A[i]
                # Lưu giá trị hiện tại của A[i] vào biến temp.
                A[i] = A[i+1]
                # Gán giá trị của A[i] bằng giá trị của A[i+1].
                A[i+1] = temp
                # Gán giá trị của A[i+1] bằng giá trị của temp (giá trị ban đầu của A[i]).
                
A = [3, 5, 8, 9, 6, 2]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
bubblesort(A)
# Gọi hàm bubblesort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
