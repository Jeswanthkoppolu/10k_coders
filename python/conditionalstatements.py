
tickets=True
if(tickets):
    print("go and watch in stadium")
else:
    print ("watch in tv")   
    
    
#check eligibilty of person vote are not
age=int(input("enter your age:"))
if(age>=18):
    print(" eligible for vote")
else:
   print ( "not eligible for vote")   


#even or odd
num=int(input("enter the number"))
if(num%2==0):
   print("the number is even")
else:
    print("the number is odd")   



#another way for even or odd
se=[0,2,4,6,8]
ip=1234567
conv=str(ip)
if(int(conv[-1]) in se):
  print("even")
else:
   print("odd")  


#elif model
eamcetrank=int(input("enter your rank:"))
if(eamcetrank< 25000):
   print("you cn join in cmr clg")
elif(eamcetrank < 50000):
   print("you can join in kakateeya clg")
elif(eamcetrank > 75000):
   print("you can join in mallareddy") 
elif(eamcetrank< 100000):
   print("you can join in scel clg") 
else:
   print("join in dregee")  



#nested if     

developer=True
role=input("enter your role:")
if(developer):
   if(role=="frontend"):
      print("you were frontend developer") 
   elif(role=="backend"):
      print("you were backend developer ")
   elif(role=="database"):
      print("you were database side")   
   elif(role=="fullstack"):
      print("you were fullstack developer")
   else:
      print("join in 10k coders")         


