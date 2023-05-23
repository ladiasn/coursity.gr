import math

a1=int(input('δώστε την καρτεσιανή συντεταγμένη του άξονα x για το διάνυσμα α a1='))
a2=int(input('δώστε την καρτεσιανή συντεταγμένη του άξονα y για το διάνυσμα α a2='))
theta1=math.degrees(math.atan(a2/a1))
print('η γωνία του διανύσματος α ειναι %.2f' % theta1)

b1=int(input('δώστε την καρτεσιανή συντεταγμένη του άξονα x για το διάνυσμα β b1='))
b2=int(input('δώστε την καρτεσιανή συντεταγμένη του άξονα y για το διάνυσμα β b2='))
theta2=math.degrees(math.atan(b2/b1))
print('η γωνία του διανύσματος β ειναι %.2f' % theta2)

arith=a1*b1 + a2*b2
paron=math.sqrt(a1**2 + a2**2) * math.sqrt(b1**2 + b2**2)
costh=arith/paron

goniath=theta1-theta2

print('το συνημίτονο ειναι %.2f' % costh)
print('η γωνία θ %.2f ειναι ' % goniath)
