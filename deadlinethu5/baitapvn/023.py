def radixsort(A):
    # Định nghĩa một hàm tên là radixsort và chấp nhận một mảng A làm đối số đầu vào.
    n = len(A)
    # Lấy độ dài của mảng A và lưu trữ trong biến n.
    maxelement = max(A)
    # Tìm giá trị lớn nhất trong mảng A và lưu trữ trong biến maxelement.
    digits = len(str(maxelement))
    # Tính số chữ số của giá trị lớn nhất và lưu trữ trong biến digits.
    bins = [[] for _ in range(10)]
    # Tạo một mảng bins để lưu trữ các phần tử theo chữ số từ 0 đến 9.

    for i in range(digits):
        # Lặp qua từng chữ số, bắt đầu từ hàng đơn vị và di chuyển lên hàng trăm, hàng nghìn, v.v.
        for j in range(n):
            # Lặp qua từng phần tử trong mảng A.
            e = int((A[j] / pow(10, i)) % 10)
            # Tính chữ số thứ i của phần tử thứ j trong mảng A.
            bins[e].append(A[j])
            # Đặt phần tử vào thùng bins tương ứng với chữ số e.

        k = 0
        for x in range(10):
            while len(bins[x]) > 0:
                A[k] = bins[x].pop(0)
                k += 1
        # Trích xuất các phần tử từ các thùng bins và đặt lại vào mảng A để sắp xếp.

A = [63, 250, 835, 947, 651, 28]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
radixsort(A)
# Gọi hàm radixsort để sắp xếp mảng A.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
