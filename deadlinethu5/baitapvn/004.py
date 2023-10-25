def selectionsort(A):
    # Định nghĩa một hàm tên là selectionsort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    for i in range(n-1):
        # Bắt đầu vòng lặp ngoài cùng qua các phần tử của mảng A từ 0 đến (n-1).
        position = i
        # Gán giá trị của biến position bằng giá trị hiện tại của biến i.
        for j in range(i+1, n):
            # Bắt đầu vòng lặp trong cùng để tìm phần tử nhỏ nhất trong mảng chưa sắp xếp.
            if A[j] < A[position]:
                # So sánh phần tử thứ j với phần tử tại vị trí position.
                # Nếu phần tử tại vị trí j nhỏ hơn, thì gán position = j.
                position = j
        temp = A[i]
        # Lưu giá trị hiện tại của phần tử tại vị trí i vào biến temp.
        A[i] = A[position]
        # Gán giá trị của phần tử tại vị trí i bằng giá trị của phần tử tại vị trí position (phần tử nhỏ nhất tìm được).
        A[position] = temp
        # Gán giá trị của phần tử tại vị trí position (phần tử nhỏ nhất tìm được) bằng giá trị của biến temp (phần tử ban đầu tại vị trí i).

A = [3, 5, 8, 9, 6, 2]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
selectionsort(A)
# Gọi hàm selectionsort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
