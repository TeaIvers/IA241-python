'''
Lab 7
'''
#3.1
i=6
while i>=1:
    i=i-1
    if i==3:
        continue
    print(i)
#3.2
i = 1
result = 1
while i<=5:
     result = result * i
     i = i + 1 
print(result)
#3.3
result = 0
i = 1
while i <= 5:
    result = result + i  
    i = i +1  
print(result)
#3.4
k = 3
result =1

while k <= 8:
    result = result * k  
    k = k + 1  
print(result)
#3.5
i=4
result=1
while i<=8:
    result*=i
    i+=1
print(result)
#3.6
num_list = [12, 32, 43, 35]
while len(num_list) > 0:
    num_list.pop()  
    print(num_list)  

    
    