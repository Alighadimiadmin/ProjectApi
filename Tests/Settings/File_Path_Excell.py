from openpyxl import load_workbook
from pathlib import Path
# Develop By Ali_Ghadimi
def Excell_file_path():
    # پیدا کردن مسیر فایل اسکریپت فعلی
    current_directory = Path(__file__).resolve().parent
    # تنظیم مسیر نسبی فایل اکسل
    project_root = current_directory.parents[1]  # تغییر این مقدار برای تنظیم دقیق مسیر
    excel_file_path = project_root /"Tests"/ "Settings" / "Excells" / "Environment_Hosts.xlsx"
    # تبدیل به مسیر مطلق و نرمال‌سازی
    excel_file_path = excel_file_path.resolve()
    # بارگذاری فایل اکسل
    workbook = load_workbook(excel_file_path)
    worksheet = workbook.active
    return worksheet





