year=int(input('dose etos year='))

if (year%4==0 and year%100!=0) or year%400==0:
    disekto=True
else:
    disekto=False

print(disekto)

if disekto:
    print('to etos', year ,'einai disekto')
else:
    print('to etos', year ,'den einai disekto')
