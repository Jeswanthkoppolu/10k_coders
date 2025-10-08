import re

regex_pan = r"^[A-Z]{5}[0-9]{4}[A-Z]$"  
user_input = input("Enter your PAN number: ").strip().upper()  
if re.search(regex_pan, user_input):
    print("Valid PAN number")
else:
    print("Invalid PAN number")



regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
ip = "2025-09-28"
if re.fullmatch(regex, ip):
    print("Valid date")
else:
    print("Invalid date")


