                                                #8 bit DES
operation=int(input("Encryption-1 or Decryption-2 "))
text=list(map(int,input("text ").split()))
ip=list(map(int,input("ip ").split()))
e_p=list(map(int,input("e/p ").split()))
inverse_ip=list(map(int,input("inverse ip ").split()))
p4=list(map(int,input("p4 ").split()))
key=list(map(int,input("key ").split()))
p10=list(map(int,input("p10 ").split()))
p8=list(map(int,input("p8 ").split()))

#finding k1
p10_key=[key[i-1] for i in p10]
p10_key.insert(4,p10_key.pop(0))
p10_key.insert(9,p10_key.pop(5))
k1=[p10_key[i-1] for i in p8]

#finding k2
p10_key.insert(4,p10_key.pop(0))
p10_key.insert(4,p10_key.pop(0))
p10_key.insert(9,p10_key.pop(5))
p10_key.insert(9,p10_key.pop(5))
k2=[p10_key[i-1] for i in p8]

if operation==1:
    #processing encryption
    temp=[text[i-1] for i in ip]
    l1=temp[0:4]
    r1=temp[4:]

    temp1=[r1[i-1] for i in e_p]
    l2r2=[(temp1[i]^k1[i]) for i in range(8)]
    l2=l2r2[0:4]
    r2=l2r2[4:]
    
    #s-box
    s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

    a=int(('0b'+(''.join([str(l2[0]),str(l2[3])]))),2)
    b=int(('0b'+(''.join([str(l2[1]),str(l2[2])]))),2)

    x=list(bin(int(s0[a][b])))[2:]
    if len(x)==1:
        x.insert(0,'0')
    
    c=int(('0b'+(''.join([str(r2[0]),str(r2[3])]))),2)
    d=int(('0b'+(''.join([str(r2[1]),str(r2[2])]))),2)

    y=list(bin(int(s1[c][d])))[2:]
    if len(y)==1:
        y.insert(0,'0')

    z=x+y
    temp2=[z[i-1] for i in p4]
    l3=[(int(temp2[i])^l1[i]) for i in range(4)]

    before_switch=l3+r1
    
    #switching
    after_switch=r1+l3
    l4=after_switch[0:4]
    r4=after_switch[4:]

    temp3=[r4[i-1] for i in e_p]
    l5r5=[(temp3[i]^k2[i]) for i in range(8)]
    l5=l5r5[0:4]
    r5=l5r5[4:]

    e=int(('0b'+(''.join([str(l5[0]),str(l5[3])]))),2)
    f=int(('0b'+(''.join([str(l5[1]),str(l5[2])]))),2)

    u=list(bin(int(s0[e][f])))[2:]
    if len(u)==1:
        u.insert(0,'0')
    
    g=int(('0b'+(''.join([str(r5[0]),str(r5[3])]))),2)
    h=int(('0b'+(''.join([str(r5[1]),str(r5[2])]))),2)

    v=list(bin(int(s1[g][h])))[2:]
    if len(v)==1:
        v.insert(0,'0')
    
    w=u+v
    temp4=[w[i-1] for i in p4]
    l6=[(int(temp4[i])^l4[i]) for i in range(4)]

    final=l6+r4
    ciphertext=[str(final[i-1]) for i in inverse_ip]

    print("\n"+"The cipher text is:")
    print("\n"+"".join(ciphertext))

else:
    #processing decryption
    temp=[text[i-1] for i in ip]
    l1=temp[0:4]
    r1=temp[4:]

    temp1=[r1[i-1] for i in e_p]
    l2r2=[(temp1[i]^k2[i]) for i in range(8)]
    l2=l2r2[0:4]
    r2=l2r2[4:]

    #s-box
    s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

    a=int(('0b'+(''.join([str(l2[0]),str(l2[3])]))),2)
    b=int(('0b'+(''.join([str(l2[1]),str(l2[2])]))),2)

    x=list(bin(int(s0[a][b])))[2:]
    if len(x)==1:
        x.insert(0,'0')
    
    c=int(('0b'+(''.join([str(r2[0]),str(r2[3])]))),2)
    d=int(('0b'+(''.join([str(r2[1]),str(r2[2])]))),2)

    y=list(bin(int(s1[c][d])))[2:]
    if len(y)==1:
        y.insert(0,'0')

    z=x+y
    temp2=[z[i-1] for i in p4]
    l3=[(int(temp2[i])^l1[i]) for i in range(4)]

    before_switch=l3+r1

    after_switch=r1+l3
    l4=after_switch[0:4]
    r4=after_switch[4:]

    temp3=[r4[i-1] for i in e_p]
    l5r5=[(temp3[i]^k1[i]) for i in range(8)]
    l5=l5r5[0:4]
    r5=l5r5[4:]

    e=int(('0b'+(''.join([str(l5[0]),str(l5[3])]))),2)
    f=int(('0b'+(''.join([str(l5[1]),str(l5[2])]))),2)

    u=list(bin(int(s0[e][f])))[2:]
    if len(u)==1:
        u.insert(0,'0')
    
    g=int(('0b'+(''.join([str(r5[0]),str(r5[3])]))),2)
    h=int(('0b'+(''.join([str(r5[1]),str(r5[2])]))),2)

    v=list(bin(int(s1[g][h])))[2:]
    if len(v)==1:
        v.insert(0,'0')
    
    w=u+v
    temp4=[w[i-1] for i in p4]
    l6=[(int(temp4[i])^l4[i]) for i in range(4)]

    final=l6+r4
    plaintext=[str(final[i-1]) for i in inverse_ip]

    print("\n"+"The plain text is:")
    print("\n"+"".join(plaintext))


