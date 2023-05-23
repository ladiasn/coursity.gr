import math

with open('inputdata.txt') as inn:
    arxeio= inn.read().splitlines()

arxeionew=[]
for i in arxeio:
    num1= i.split(',')
    for n in num1:
        arxeionew.append(float(n))

print(arxeionew)
print(type(arxeionew[0]))
mikos= len(arxeionew)
print ('mikos listas', mikos)


summ=0
for x in arxeionew:
    summ += x
else:
    mesos_oros=summ/mikos
    print('mesos oros einai %.3f' % mesos_oros)

summ1=0
for x in arxeionew:
    summ1 += (x-mesos_oros)**2
else:
    apoklisi=math.sqrt(summ1/mikos)
    print('tipiki apoklisi einai %.3f' % apoklisi)

mm=str('%.3f' % mesos_oros)
ta=str('%.3f' % apoklisi)


    
with open('outputdata.txt','a+') as outt:
    outt.write('mesos oros=' + mm + '\n')

with open('outputdata.txt','a+') as outt:
    outt.write('tipiki apoklisi=' + ta + '\n')

    
