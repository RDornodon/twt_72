for I in[I:=input]*int(I()):
 D=I();r,l=0>1,len(D)
 for v in range(1,l):r|=D==''.join(map(str,range(i:=int(D[:v]),i+l//v)))
 print(r)
