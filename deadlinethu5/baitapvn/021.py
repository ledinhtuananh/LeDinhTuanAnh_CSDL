def countsort(A):
    # Định nghĩa một hàm tên là countsort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    maxsize = max(A)
    # Tìm giá trị lớn nhất trong mảng A và lưu trữ trong biến maxsize.
    carray = [0] * (maxsize + 1)
    # Tạo một mảng đếm (counting array) carray có kích thước bằng với giá trị lớn nhất trong mảng A + 1.

    for i in range(n):
        # Đếm số lần xuất hiện của mỗi phần tử trong mảng A và lưu vào carray.
        carray[A[i]] = carray[A[i]] + 1

    i = 0
    j = 0
    while i < maxsize + 1:
        # Đặt lại các giá trị trong mảng A dựa trên thông tin từ carray để sắp xếp mảng.
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1
    # Quá trình trích xuất các phần tử từ mảng đếm carray và đặt lại vào mảng A để sắp xếp.

A = [3, 5, 8, 9, 6, 2, 3, 5, 5]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
countsort(A)
# Gọi hàm countsort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
