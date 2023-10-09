# Định nghĩa một lớp _Node để biểu diễn một nút trong danh sách liên kết
class _Node:
    # __slots__ giới hạn các thuộc tính được phép trong đối tượng, trong trường hợp này, chỉ có 'element' và 'next'
    __slots__ = 'element', 'next'

    # Constructor của lớp _Node, khởi tạo một nút với 'element' là dữ liệu và 'next' là tham chiếu đến nút tiếp theo
    def __init__(self, element, next):
        self.element = element
        self.next = next

# Định nghĩa lớp LinkedList để biểu diễn danh sách liên kết
class LinkedList:
    # Constructor của lớp LinkedList, khởi tạo danh sách liên kết rỗng
    def __init__(self):
        self._head = None  # Đầu danh sách liên kết
        self._tail = None  # Cuối danh sách liên kết
        self._size = 0     # Số lượng phần tử trong danh sách liên kết

    # Phương thức trả về độ dài của danh sách liên kết
    def __len__(self):
        return self._size

    # Phương thức kiểm tra xem danh sách liên kết có rỗng không
    def isempty(self):
        return self._size == 0

    # Phương thức thêm một phần tử vào cuối danh sách liên kết
    def add_last(self, e):
        newest = _Node(e, None)  # Tạo một nút mới với dữ liệu 'e' và tham chiếu 'None'
        if self.isempty():       # Kiểm tra nếu danh sách liên kết rỗng
            self._head = newest  # Đặt 'newest' làm đầu danh sách
            self._tail = newest  # Đặt 'newest' làm cuối danh sách
        else:
            self._tail.next = newest  # Cập nhật tham chiếu 'next' của nút cuối cùng đến 'newest'
            self._tail = newest       # Đặt 'newest' làm cuối danh sách mới
        self._size += 1              # Tăng kích thước danh sách liên kết lên 1

    # Phương thức in danh sách liên kết
    def display(self):
        current = self._head  # Bắt đầu từ đầu danh sách
        while current:        # Duyệt qua từng nút trong danh sách
            print(current.element, end=" --> ")  # In dữ liệu của nút và dấu --> để phân tách
            current = current.next  # Di chuyển đến nút tiếp theo
        print()  # In xuống dòng để kết thúc danh sách liên kết

# Tạo một đối tượng LinkedList
L = LinkedList()

# Thêm các phần tử vào danh sách liên kết
L.add_last(7)
L.add_last(4)
L.add_last(12)

# In danh sách liên kết
L.display()
