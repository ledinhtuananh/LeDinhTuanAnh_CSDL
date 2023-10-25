class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element  # Lưu trữ giá trị dữ liệu của nút
        self._next = next  # Con trỏ trỏ đến nút kế tiếp

class CircularLinkedList:
    def __init__(self):
        self._head = None  # Con trỏ đến nút đầu danh sách
        self._tail = None  # Con trỏ đến nút cuối danh sách
        self._size = 0  # Số lượng phần tử trong danh sách

    def __len__(self):
        return self._size  # Trả về kích thước danh sách

    def isempty(self):
        return self._size == 0  # Kiểm tra xem danh sách có rỗng không

    def addlast(self, e):
        newest = _Node(e, None)  # Tạo một nút mới với giá trị dữ liệu là 'e' và con trỏ 'next' ban đầu trỏ đến 'None'
        if self.isempty():
            newest._next = newest  # Nếu danh sách rỗng, nút mới trỏ vào chính nó
            self._head = newest  # Gán 'head' và 'tail' cho nút mới
        else:
            newest._next = self._tail._next  # Nối nút mới vào danh sách liên kết vòng
            self._tail._next = newest
        self._tail = newest  # Cập nhật 'tail' để trỏ đến nút mới
        self._size += 1  # Tăng kích thước danh sách lên 1

    def display(self):
        p = self._head  # Bắt đầu từ nút đầu của danh sách
        i = 0
        while i < len(self):  # Duyệt qua danh sách dựa trên kích thước của danh sách
            print(p._element, end='-->')  # In giá trị dữ liệu của nút
            p = p._next  # Di chuyển đến nút kế tiếp
            i = i + 1
        print()  # In xuống dòng để kết thúc dãy giá trị

C = CircularLinkedList()  # Khởi tạo một danh sách liên kết vòng mới

C.addlast(7)  # Thêm các phần tử vào danh sách
C.addlast(4)
C.addlast(12)

C.display()  # Hiển thị danh sách liên kết vòng
