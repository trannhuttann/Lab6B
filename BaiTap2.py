import tkinter as tk

def scan_now():
    status_label.config(text="Đang quét...")

def quick_scan():
    status_label.config(text="Quét nhanh đang chạy...")

def web_protect():
    status_label.config(text="Bảo vệ web đã được kích hoạt.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng bảo mật")
root.geometry("800x500")
root.configure(bg="#dcdcdc")  # Màu nền tùy chỉnh

# Khung chính được chia làm hai phần: sidebar và main_content
sidebar = tk.Frame(root, width=200, bg="#6495ED", padx=10, pady=10)
sidebar.pack(expand=False, fill="y", side="left")

main_content = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
main_content.pack(expand=True, fill="both", side="right")

# Thanh bên (sidebar)
status_label = tk.Label(sidebar, text="Trạng thái", font=("Arial", 14, "bold"), bg="#6495ED", fg="white")
status_label.pack(pady=(10, 20))

update_label = tk.Label(sidebar, text="Cập nhật", font=("Arial", 12), bg="#6495ED", fg="white")
update_label.pack()

scan_button = tk.Button(sidebar, text="Quét ngay", font=("Arial", 12), command=scan_now)
scan_button.pack(pady=10)

# Khu vực chính (main_content)
title_label = tk.Label(main_content, text="Ứng dụng bảo mật", font=("Arial", 24, "bold"), bg="#ffffff")
title_label.pack(pady=(0, 20))

subtitle_label = tk.Label(main_content, text="Bảo vệ máy tính của bạn với các tính năng bảo mật tiên tiến.", font=("Arial", 14), bg="#ffffff")
subtitle_label.pack()

quick_scan_button = tk.Button(main_content, text="Quét nhanh", font=("Arial", 12), command=quick_scan)
quick_scan_button.pack(pady=10)

web_protect_button = tk.Button(main_content, text="Bảo vệ web", font=("Arial", 12), command=web_protect)
web_protect_button.pack(pady=10)

# Nhãn trạng thái
status_label = tk.Label(main_content, text="Sẵn sàng...", font=("Arial", 12), bg="#ffffff")
status_label.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
