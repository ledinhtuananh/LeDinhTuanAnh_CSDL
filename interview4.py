def are_anagrams(word1, word2):
    # Loại bỏ khoảng trắng và chuyển tất cả ký tự thành chữ thường
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Kiểm tra xem hai từ có cùng độ dài
    if len(word1) != len(word2):
        return False

    # Tạo một từ điển (dictionary) để đếm số lần xuất hiện của mỗi ký tự trong từ 1
    char_count = {}
    for char in word1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Kiểm tra số lần xuất hiện của các ký tự trong từ 2
    for char in word2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # Nếu tất cả số lần xuất hiện của các ký tự đều bằng 0, thì đây là anagram
    return all(value == 0 for value in char_count.values())

# Nhập hai từ cần kiểm tra
word1 = input("Nhap tu 1: ")
word2 = input("Nhap tu 2: ")

# Kiểm tra xem hai từ có phải là anagram hay không
if are_anagrams(word1, word2):
    print("Hai tu la anagram.")
else:
    print("Hai tu khong phai la anagram.")
