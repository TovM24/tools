import psutil

def get_running_browser():
    for process in psutil.process_iter(attrs=['pid', 'name', 'exe']):
        try:
            process_info = process.info
            exe_path = process_info.get('exe', None)
            
            if exe_path is not None:
                exe_path = exe_path.lower()
                if 'chrome.exe' in exe_path:
                    return 'Google Chrome'
                elif 'firefox.exe' in exe_path:
                    return 'Mozilla Firefox'
                elif 'coc_coc.exe' in exe_path:
                    return 'Cốc Cốc'
                elif 'msedge.exe' in exe_path:
                    return 'Microsoft Edge'
                # Thêm các trình duyệt khác ở đây nếu cần

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # trả về giá trị mặc định, trường hợp khong tìm thấy giá tị nào
    return None
