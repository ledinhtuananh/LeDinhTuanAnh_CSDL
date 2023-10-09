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

    # Phương thức tìm kiếm một phần tử trong danh sách liên kết và trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy
    def search(self, key):
        p = self._head  # Bắt đầu từ đầu danh sách
        index = 0       # Biến index để theo dõi vị trí của phần tử trong danh sách
        while p:
            if p.element == key:  # So sánh giá trị của phần tử hiện tại (p.element) với giá trị cần tìm (key)
                return index  # Nếu tìm thấy, trả về vị trí (index) của phần tử trong danh sách
            p = p.next   # Di chuyển con trỏ p đến phần tử tiếp theo trong danh sách
            index += 1   # Tăng biến index lên 1 để theo dõi vị trí của phần tử trong danh sách
        return -1  # Nếu không tìm thấy phần tử sau khi duyệt qua toàn bộ danh sách, trả về -1 để thể hiện rằng phần tử không tồn tại trong danh sách

    # Phương thức in danh sách liên kết
    def display(self):
        current = self._head  # Bắt đầu từ đầu danh sách
        while current:
            print(current.element, end=" --> ")  # In dữ liệu của nút và dấu --> để phân tách
            current = current.next  # Di chuyển đến nút tiếp theo
        print()

# Tạo một đối tượng LinkedList
L = LinkedList()

# Thêm các phần tử vào danh sách liên kết
L.add_last(7)
L.add_last(4)
L.add_last(12)

# In danh sách liên kết
L.display()
print('Size:', len(L))

# Thêm thêm phần tử vào danh sách liên kết
L.add_last(8)
L.add_last(3)

# In danh sách liên kết sau khi thêm phần tử
L.display()
print('Size:', len(L))

# Tìm kiếm phần tử trong danh sách liên kết và in kết quả
i = L.search(8)
print('Result:', i)
