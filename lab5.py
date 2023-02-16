'''
Lab 5
'''
#3.1
alien_color ='green'
if alien_color =='green':
    print('you got 5 points')
#3.2
alien_color='red'
if alien_color == 'green':
    print('you got 5 points')
else: 
    print('you got 10 points')
#3.3
favorite_fruits=['apple','strawberry','banana']
if 'apple' in favorite_fruits:
    print('you really like apples!')
    
if 'strawberry' in favorite_fruits:
    print('you really like strawberrys!')
if 'banana' in favorite_fruits:
    print('you really like bananas!')
#3.4
age= 19
if age<10:
    print('Kid')
elif age <20:
    print('Teenager')
elif age >=65:
    print('Elder')
else:
    print('Adult')
    