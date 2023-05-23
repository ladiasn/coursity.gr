import statistics

def squares(*args):
    if len(args)==1:
        return print('den mporoun na ipologistoun ta zitoumena tis askisis')
    else:
        ave=int(statistics.mean(args))
        for i in args:
            d=int(i-ave)**2
            yield d
    
for k in squares(2,7,3,12):
    print(k)
   
    








