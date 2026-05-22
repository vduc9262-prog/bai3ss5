


num_classrooms = int(input("Số lượng phòng học cần kiểm tra: "))

# Bẫy 1
if num_classrooms <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, num_classrooms + 1):
        print(f"Phòng học {room}")
        
        rows = int(input("Nhập số lượng hàng ghế: "))
        seats_per_row = int(input("Nhập số ghế trên mỗi hàng: "))
        
        # Bẫy 2
        if rows <= 0 or seats_per_row <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
        
        # Bẫy 3
        if rows > 10 or seats_per_row > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
        
        # In sơ đồ chỗ ngồi
        print(f"Sơ đồ chỗ ngồi phòng {room}:")
        for r in range(rows):
            print("* " * seats_per_row)
        
        print()

    





# Đề xuất giải pháp

# sử dụng vòng lặp for cho từng phòng học.
# kiểm tra điều kiện ngay sau khi nhập dữ liệu của từng phòng.
# sử dụng vòng lặp lồng nhau để vẽ sơ đồ ghế ngồi.
# dùng break để dừng chương trình khi gặp phòng quá lớn
