def is_palindrome(s):
    # Loại bỏ khoảng trắng và chuyển chuỗi về chữ thường
    s = s.replace(" ", "").lower()
    
    # So sánh chuỗi gốc với phiên bản đảo ngược của nó
    return s == s[::-1]

# Nhập chuỗi cần kiểm tra
input_string = input("Nhap chuoi: ")

# Kiểm tra xem chuỗi có phải là palindrome hay không
if is_palindrome(input_string):
    print("Chuoi la palindrome.")
else:
    print("Chuoi khong phai la palindrome.")
