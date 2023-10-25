def shellsort(A):
    # Định nghĩa một hàm tên là shellsort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    gap = n // 2
    # Bắt đầu với một khoảng bước (gap) ban đầu bằng nửa độ dài của mảng.

    while gap > 0:
        # Bắt đầu vòng lặp while chạy cho đến khi khoảng bước (gap) trở thành 0.
        i = gap
        # Bắt đầu từ vị trí gap (khoảng bước) trong mảng.
        while i < n:
            # Vòng lặp while này di chuyển qua từng phần tử trong khoảng bước (gap).
            temp = A[i]
            # Lưu giá trị của phần tử hiện tại (A[i]) vào biến temp.
            j = i - gap
            # Tìm vị trí j là vị trí cách khoảng bước (gap) so với i.

            while j >= 0 and A[j] > temp:
                # Tiếp tục di chuyển về phía trước trong khoảng bước (gap) để tìm vị trí thích hợp cho phần tử temp.
                A[j + gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            # Gán giá trị của phần tử temp vào vị trí đúng trong khoảng bước (gap).
            i = i + 1
            # Di chuyển đến phần tử tiếp theo trong khoảng bước (gap).

        gap = gap // 2
        # Giảm khoảng bước (gap) đi một nửa để tiếp tục quá trình sắp xếp với khoảng bước (gap) nhỏ hơn.

A = [3, 5, 8, 9, 6, 2]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
shellsort(A)
# Gọi hàm shellsort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
