def mergesort(A, left, right):
    # Định nghĩa một hàm tên là mergesort và chấp nhận một mảng A, vị trí bắt đầu (left) và vị trí kết thúc (right).
    if left < right:
        # Kiểm tra nếu chỉ còn một phần tử hoặc không có phần tử nào cần sắp xếp nữa.
        mid = (left + right) // 2
        # Tìm vị trí giữa của mảng.
        mergesort(A, left, mid)
        # Gọi đệ quy mergesort cho nửa đầu của mảng (từ left đến mid).
        mergesort(A, mid + 1, right)
        # Gọi đệ quy mergesort cho nửa sau của mảng (từ mid+1 đến right).
        merge(A, left, mid, right)
        # Gọi hàm merge để trộn hai nửa đã sắp xếp lại với nhau.

def merge(A, left, mid, right):
    # Định nghĩa hàm merge để trộn hai mảng con đã sắp xếp thành một mảng con sắp xếp hoàn chỉnh.
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)
    # Tạo một mảng B để lưu trữ các phần tử đã được trộn lại.
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    # So sánh và đặt phần tử nhỏ hơn vào mảng B.
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1
    for x in range(left, right + 1):
        A[x] = B[x]
    # Sao chép các phần tử từ mảng B trở lại mảng A.

A = [3, 5, 8, 9, 2, 4]
# Tạo một mảng A với các giá trị đã cho.
print("Original Array:", A)
# In ra màn hình mảng ban đầu.
mergesort(A, 0, len(A) - 1)
# Gọi hàm mergesort để sắp xếp mảng A từ vị trí 0 đến len(A)-1.
print("Sorted Array:", A)
# In ra màn hình mảng sau khi đã sắp xếp.
