from datetime import datetime
from Tests.login import login
from Tests.input_user_name import input_user_name


# تابع مدیریت اجرای تست‌ها
def run_test(test_func):
    try:
        status_code = test_func()
        if status_code == 200:
            print(f"Test {test_func.__name__} succeeded.")
            return True
        else:
            print(f"Test {test_func.__name__} failed with status code {status_code}.")
            return False
    except Exception as e:
        print(f"An error occurred during {test_func.__name__}: {e}")
        return False


# اجرای تست‌ها
if __name__ == "__main__":
    all_tests_passed = True
    all_tests_passed &= run_test(login)
    all_tests_passed &= run_test(input_user_name)

    print(datetime.now())
    print("====================================================")
