import json
data = {
    "name": ["bobby20", "surya18", "bhargav15"],
    "user": ["bobby", "bhargav", "sai","murari"]
}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


##adding operation
add=input("enter name to add: ")
user=input("enter username: ")
with open('data.json') as f:
    data=json.load(f) 
    if user in data['user']:
        if add not in data['name']:
            data['name'].append(add)  
        else:
            print(f"{add} already exists")
    else:
        print("you are not authorised to perform to add operation")
with open('data.json','w')as f:
    json.dump(data,f)
    print("data upadted")


##remove operation
remove=input('enter name to remove: ')
user=input("enter username: ")
with open('data.json','r')as f:
    data=json.load(f)
    if user in data['user']:
        if remove not in data['name']:
            print(f"{remove} is not avaliable")
        else:
            data['name'].remove(remove)
            print(f"{remove} is removed successfully")
    else:
        print("you are not authorised to perform to remove operation")
with open('data.json','w')as f:
    json.dump(data,f)

