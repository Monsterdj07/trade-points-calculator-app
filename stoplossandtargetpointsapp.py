e = int(input("Enter Entry price:"))
s = int(input("Enter stop loss:"))
t = int(input("Enter target1:"))
t2 = int(input("Enter target2:"))
stoplosspoints= e-s
targetpoints= t-e
trail= (t2-t)/2
print(f"stop loss points = {stoplosspoints}")
print(f"target points = {targetpoints}")
print(f"trail points = {trail}")