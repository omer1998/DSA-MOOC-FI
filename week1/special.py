def check_year(year):
    rt_half = year % 100
    lf_half = int((year - rt_half) / 100)
    if (rt_half+lf_half)**2 == year:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False