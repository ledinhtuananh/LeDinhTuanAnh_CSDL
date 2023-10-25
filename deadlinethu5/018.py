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
    def add_any(self, e, position):  # Sửa tên phương thức thành 'add_any'
        newest = _Node(e, None)  # Tạo một nút mới 'newest' với dữ liệu 'e' và tham chiếu 'None'
        p = self._head           # Khởi tạo con trỏ 'p' từ đầu danh sách liên kết
        i = 1                     # Khởi tạo biến 'i' để theo dõi vị trí trong danh sách

        # Duyệt danh sách đến vị trí trước vị trí cần thêm phần tử (position - 1)
        while i < position - 1:
            p = p.next  # Di chuyển con trỏ 'p' đến phần tử tiếp theo trong danh sách
            i += 1      # Tăng biến 'i' lên 1 để tiếp tục kiểm tra vị trí

        # Cập nhật tham chiếu 'next' của 'newest' và 'p' để thêm 'newest' vào vị trí 'position'
        newest.next = p.next  # Tham chiếu 'next' của 'newest' trỏ đến phần tử sau 'p' trong danh sách
        p.next = newest       # Tham chiếu 'next' của 'p' trỏ đến 'newest'

        self._size += 1       # Tăng kích thước danh sách liên kết lên 1 sau khi thêm phần tử


    # Phương thức tìm kiếm một phần tử trong danh sách liên kết và trả về vị trí nếu tìm thấy, -1 nếu không tìm thấy.
    def removefirst(self):
        # kiểm tra xme danh sách liên kết có rỗng không. 
        if self.isempty():
            print('List is empty')
            # In thông báo nếu danh sách liên kết rỗng.
            return None
        e = self._head.element
        self._head = self._head.next
        # Giảm kích thước danh sách liên kết đi 1 sau khi loại bỏ phần tử đầu tiên.
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e
    # Phương thức loại bỏ phần tử cuối cùng trong danh sách liên kết.
    def removelast(self):
        if self.isempty():
            print('List is empty')# Kiểm tra xem danh sách có rỗng không
            return None
        p = self._head
        i = 1
         # Duyệt danh sách đến phần tử trước phần tử cuối cùng
        while i < len(self) - 1:
            p = p.next
            i += 1
        self._tail = p# Cập nhật con trỏ tail để trỏ đến phần tử trước phần tử cuối cùng
        p = p.next# Di chuyển con trỏ p đến phần tử cuối cùng
        e = p.element# Lấy giá trị của phần tử cuối cùng
        self._tail.next = None# Đặt tham chiếu 'next' của phần tử trước phần tử cuối cùng thành None
        self._size -= 1 # Giảm kích thước danh sách liên kết đi 1
        return e
    def removeany(self, position):
        p = self._head # Khởi tạo con trỏ 'p' từ đầu danh sách liên kết
        i = 1  # Khởi tạo biến 'i' để theo dõi vị trí trong danh sách


        while i < position - 1:
            p = p.next# Di chuyển con trỏ 'p' đến phần tử tiếp theo trong danh sách
            i += 1

        e = p.next.element# Lấy giá trị của phần tử nằm sau vị trí cần loại bỏ (position)
        p.next = p.next.next
        self._size -= 1
        return e

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

L.add_last(7)  # Thêm phần tử có giá trị 7 vào cuối danh sách liên kết.
L.add_last(4)  # Thêm phần tử có giá trị 4 vào cuối danh sách liên kết.
L.add_last(12) # Thêm phần tử có giá trị 12 vào cuối danh sách liên kết.
L.add_last(8)  # Thêm phần tử có giá trị 8 vào cuối danh sách liên kết.
L.add_last(3)  # Thêm phần tử có giá trị 3 vào cuối danh sách liên kết.

L.display()  # In ra danh sách liên kết sau khi thêm các phần tử.
print('Size:', len(L))  # In ra kích thước của danh sách liên kết bằng cách sử dụng phương thức '__len__'.

ele = L.removelast()  # Loại bỏ phần tử cuối cùng và lưu giá trị đã loại bỏ.
L.display()  # In ra danh sách sau khi loại bỏ phần tử cuối cùng.
print('Size:', len(L))  # In ra kích thước mới của danh sách liên kết.
print('Element Removed:', ele)  # In giá trị đã loại bỏ.