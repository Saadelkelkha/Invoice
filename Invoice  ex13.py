a=int(input("type the number of photocopies :"))
if a<=10 :
    F=a*0.30
    print("the invoice is :",F)
elif a>10 and a<=30 :
    F=(a*0.30)+(a-10)*0.25
    print("the invoice is :",F)
else :
    F=(10*0.30)+(20*0.25)+(a-30)*0.20
    print("the invoice is :",F)