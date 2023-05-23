s=input('dose onoma s=')

k=len(s)
if k==1:
    print('mikos=1')
else:
    if s==s[::-1]:
        print('palindromo')
        adict={s:k}
        alist=[x for x in s]
        print(adict)
        print(alist)
    else:
        print('oxi palindromo')
