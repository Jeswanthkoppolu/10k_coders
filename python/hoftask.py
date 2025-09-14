
#1
op=map(lambda x:'+91' + x,['8688989342','8639395957','9959439119','9490246084'])
print(list(op))

#2
op=map(lambda x:x*83,[10,25,40,100] )
print(list(op))

#3
op=filter(lambda x: "@gmail.com" in x,["harish@gmail.com", "abc@yahoo.com", "xyz@gmail.com"])
print(list(op))

#4
op=filter(lambda x:len(x)<=5,["Pen", "Notebook", "Laptop", "Charger", "Bag"])
print(list(op))

#5
op=map(lambda x: x.lower()+'@gmail.com',['Harish', 'Sushma', 'Nandu'])
print(list(op))

#6
op = filter(lambda x: x < 2025, [2022, 2023, 2025, 2026])
print(list(op))

#7
op = map(lambda x: "*" * 12 + x[-4:], ["1234567890123456", "9876543210987654"])
print(list(op))

#8
op = filter(lambda x: x >= 40000, [25000, 45000, 60000, 15000, 80000])
print(list(op))

#9
op = map(lambda x: "Product: " + x.capitalize(), ["apple", "mango", "orange"])
print(list(op))

#10
op = filter(lambda x: x >= 40, [35, 80, 55, 20, 90])
print(list(op))

#11
op = filter(lambda x: len(x) >= 8 and ('@' in x or '$' in x), ["abc123", "Admin@123", "hello", "Pa$$word"])
print(list(op))

#12
#a
op = map(lambda x: int(x.split("-")[0]), ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"])
print(list(op))

#b
op = filter(lambda x: "CREDIT" in x, ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"])
print(list(op))

#c
op = filter(lambda x: "DEBIT" in x, ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"])
print(list(op))

