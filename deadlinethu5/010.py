class _Node:
    __slots__ = 'element', 'next'

    # Định nghĩa lớp _Node để biểu diễn một nút trong danh sách liên kết.
    # Mỗi nút chứa hai thuộc tính: 'element' (dữ liệu) và 'next' (tham chiếu đến nút tiếp theo).
    def __init__(self, element, next):
        self.element = element  # Gán giá trị dữ liệu cho nút
        self.next = next        # Gán tham chiếu đến nút tiếp theo

# Định nghĩa lớp LinkedList để biểu diễn danh sách liên kết.
class LinkedList:
    def __init__(self):
        self._head = None    # Đặt con trỏ đầu danh sách (head) thành None
        self._tail = None    # Đặt con trỏ cuối danh sách (tail) thành None
        self._size = 0       # Khởi tạo kích thước danh sách bằng 0

    # Phương thức trả về độ dài của danh sách liên kết.
    def __len__(self):
        return self._size   # Trả về kích thước danh sách

    # Phương thức kiểm tra xem danh sách liên kết có rỗng không.
    def isempty(self):
        return self._size == 0  # Trả về True nếu danh sách rỗng, ngược lại trả về False

    # Phương thức thêm một phần tử vào cuối danh sách liên kết.
    def add_last(self, e):
        newest = _Node(e, None)  # Tạo một nút mới với dữ liệu 'e' và tham chiếu 'None'
        if self.isempty():       # Kiểm tra nếu danh sách liên kết rỗng
            self._head = newest  # Đặt 'newest' làm đầu danh sách
            self._tail = newest  # Đặt 'newest' làm cuối danh sách
        else:
            self._tail.next = newest  # Cập nhật tham chiếu 'next' của nút cuối cùng đến 'newest'
            self._tail = newest       # Đặt 'newest' làm cuối danh sách mới
        self._size += 1              # Tăng kích thước danh sách liên kết lên 1

    # Phương thức thêm một phần tử vào đầu danh sách liên kết.
    def add_first(self, e):
        newest = _Node(e, None)  # Tạo một nút mới với dữ liệu 'e' và tham chiếu 'None'
        if self.isempty():       # Kiểm tra nếu danh sách liên kết rỗng
            self._head = newest  # Đặt 'newest' làm đầu danh sách
            self._tail = newest  # Đặt 'newest' làm cuối danh sách
        else:
            newest.next = self._head  # Cập nhật tham chiếu 'next' của 'newest' đến nút hiện tại đầu danh sách
            self._head = newest       # Đặt 'newest' làm đầu danh sách mới
        self._size += 1              # Tăng kích thước danh sách liên kết lên 1

    # Phương thức tìm kiếm một phần tử trong danh sách liên kết và trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy.
    def search(self, key):
        p = self._head     # Bắt đầu từ đầu danh sách
        index = 0          # Biến index để theo dõi vị trí của phần tử trong danh sách
        while p:           # Duyệt qua danh sách
            if p.element == key:  # So sánh giá trị của phần tử hiện tại (p.element) với giá trị cần tìm (key)
                return index      # Nếu tìm thấy, trả về vị trí (index) của phần tử trong danh sách
            p = p.next   # Di chuyển con trỏ p đến phần tử tiếp theo trong danh sách
            index += 1   # Tăng biến index lên 1 để theo dõi vị trí của phần tử trong danh sách

        return -1  # Nếu không tìm thấy phần tử sau khi duyệt qua toàn bộ danh sách, trả về -1

    # Phương thức in danh sách liên kết ra màn hình.
    def display(self):
        current = self._head  # Bắt đầu từ đầu danh sách
        while current:        # Duyệt qua danh sách
            print(current.element, end=" --> ")  # In dữ liệu của nút và dấu --> để phân tách
            current = current.next  # Di chuyển đến nút tiếp theo
        print()  # In xuống dòng để kết thúc danh sách liên kết
L = LinkedList()  # Tạo một danh sách liên kết mới, 'L' là một đối tượng của lớp LinkedList.

L.add_last(7) 
L.add_last(4)  
L.add_last(12) 
L.add_last(8)  
L.add_last(3)  

L.display()  # Gọi phương thức 'display' để in danh sách liên kết ra màn hình.
# Kết quả in ra sẽ là: 7 --> 4 --> 12 --> 8 --> 3 -->

print('Size:', len(L))  # In ra kích thước của danh sách liên kết bằng cách sử dụng phương thức '__len__'.
# Kết quả in ra sẽ là: Size: 5

L.add_first(15)  # Thêm phần tử có giá trị 15 vào đầu danh sách liên kết.

L.display()  # In danh sách liên kết sau khi thêm phần tử 15 vào đầu.
# Kết quả in ra sẽ là: 15 --> 7 --> 4 --> 12 --> 8 --> 3 -->

print('Size:', len(L))  # In ra kích thước của danh sách liên kết sau khi thêm phần tử.
# Kết quả in ra sẽ là: Size: 6

L.add_first(25)  # Thêm phần tử có giá trị 25 vào đầu danh sách liên kết.

L.display()  # In danh sách liên kết sau khi thêm phần tử 255 vào đầu.
# Kết quả in ra sẽ là: 255 --> 15 --> 7 --> 4 --> 12 --> 8 --> 3 -->

print('Size:', len(L))  # In ra kích thước của danh sách liên kết sau khi thêm phần tử.
# Kết quả in ra sẽ là: Size: 7
