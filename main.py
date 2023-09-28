from modules import recognize_progress


running_browser = recognize_progress.get_running_browser()

# if running_browser:
#     print(f"Trình duyệt đang chạy: {running_browser}")
# else:
#     print("Không có trình duyệt nào đang chạy")

if running_browser == "Google Chrome":
    # nhận diện hình ảnh thanh search click vào nó xong thực hiện nv theo module 
    print("Google Chrome")
elif running_browser == "Mozilla Firefox":
    print("Mozilla Firefox")
elif running_browser == "Cốc Cốc":
    print("Cốc Cốc")
elif running_browser == "Microsoft Edge":
    print("Microsoft Edge")
