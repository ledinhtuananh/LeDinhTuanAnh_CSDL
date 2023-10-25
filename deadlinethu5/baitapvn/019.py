def quicksort(A, low, high):
    # Định nghĩa một hàm tên là quicksort và chấp nhận một mảng A, vị trí bắt đầu (low) và vị trí kết thúc (high).
    if low < high:
        # Kiểm tra nếu vẫn còn phần tử để sắp xếp (low < high).
        pi = partition(A, low, high)
        # Gọi hàm partition để chia mảng thành hai phần và lấy phần tử chốt (pivot) làm kết quả.
        quicksort(A, low, pi - 1)
        # Gọi đệ quy quicksort cho phần bên trái của pivot.
        quicksort(A, pi + 1, high)
        # Gọi đệ quy quicksort cho phần bên phải của pivot.

def partition(A, low, high):
    # Định nghĩa hàm partition để chia mảng thành hai phần và lấy phần tử chốt (pivot) làm kết quả.
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
            # Hoán đổi hai phần tử nếu cần thiết để đảm bảo các phần tử nhỏ hơn pivot ở bên trái,
            # và các phần tử lớn hơn pivot ở bên phải.
            A[i], A[j] = A[j], A[i]
        else:
            break
    # Đưa pivot vào vị trí đúng trong mảng đã sắp xếp.
    A[low], A[j] = A[j], A[low]
    return j

A = [3, 5, 8, 9, 6, 2]
# Tạo một mảng A với các giá trị đã cho.
print('Original Array:', A)
# In ra màn hình mảng ban đầu.
quicksort(A, 0, len(A) - 1)
# Gọi hàm quicksort để sắp xếp mảng A từ vị trí 0 đến len(A)-1.
print('Sorted Array:', A)
# In ra màn hình mảng sau khi đã sắp xếp.
