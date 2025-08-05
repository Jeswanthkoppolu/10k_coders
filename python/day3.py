#dictionary
dict={"name":"k.jeswanth",
      "age":21,
      "gendear":"male",
      "height":5.10,
      "address":{
          "dr.no":1-2-263,
          "street name":"yanamalapalem",
          "land mark":"beside vinayaka temple",
          "city":"nellore",
          "state":"AP",
          "pincode":521002
                 },
      "is he married":False,
      "skills":{"html","css","j.s","python","mysql"}
      }
dict["height"]=5.9
dict["fav food"]="briyani"
dict["hobbies"]="watching series","playing cricket"
dict["contact"]=8688989
print(dict)


#nested list
a=int(input())
b=[]
for i in range(a):
    c=input().split()
    d=list(map(int,c))
    b.append(d)
print(b)  