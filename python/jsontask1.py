import json
data=['bobby20','surya18','bhargav15']
with open('data.json','w')as f:
    json.dump(data,f)
    

##adding operation
ip=input("enter name to add: ")
with open('data.json') as f:
    data=json.load(f)  #
    if ip not in data:
        data.append(ip)  
    else:
        print(f"{ip} already exists")
with open('data.json','w')as f:
    json.dump(data,f)
    print("data upadted")


##remove operation
remove=input('enter name to remove: ')
with open('data.json','r')as f:
    data=json.load(f)
    if remove not in data:
        print(f"{remove} is not avaliable")
    else:
        data.remove(remove)
        print(f"{remove} is removed successfully")
with open('data.json','w')as f:
    json.dump(data,f)

