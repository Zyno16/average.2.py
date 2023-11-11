count =0
total=0
while True:
    inp = input ("enter the number : ")
    if inp == "done": break
    
    value = float(inp)
    total = total +value
    count = count +1
avg  = total / count
print ("the average is ",avg)
