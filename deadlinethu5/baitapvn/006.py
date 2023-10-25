def insertionsort(A):
    # Định nghĩa một hàm tên là insertionsort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    for i in range(1, n):
        # Bắt đầu vòng lặp từ 1 đến n-1 (số phần tử trong mảng).
        cvalue = A[i]
        # Lấy giá trị của phần tử hiện tại tại vị trí i và lưu trữ trong biến cvalue.
        position = i
        # Gán giá trị hiện tại của biến i vào biến position.
        while position > 0 and A[position - 1] > cvalue:
            # Bắt đầu vòng lặp while để di chuyển phần tử cvalue sang bên trái để đặt đúng vị trí trong mảng đã sắp xếp.
            A[position] = A[position - 1]
            # Gán giá trị của phần tử tại vị trí position bằng giá trị của phần tử trước nó.
            position = position - 1
            # Giảm giá trị của biến position để tiếp tục so sánh với các phần tử trước đó.
        A[position] = cvalue
        # Sau khi tìm được vị trí đúng cho cvalue, gán cvalue vào vị trí đó.

A = [3, 5, 8, 9, 6, 2]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
insertionsort(A)
# Gọi hàm insertionsort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
