devices=[]
file=open("filelist.txt","a")
while True:
    newItem=input("Enter a new Item: ")
    if newItem == 'exit':
        break
    file.write(newItem + "\n")
file.close()
file=open("filelist.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
print("All Done!")


    
        