import re
regex=re.compile(r'^[987]\d{9}')

while True:
  mobno=input("Enter mobile no")
  if len(mobno)!=10:
      print("Please Enter 10 digits")
  else:
      if regex.search(mobno):
          print("Finally !You have Entered a Valid mob no")
          print("You can try again")
      else:
          print("Please Enter digits only and that too starting from nine")
      
    
