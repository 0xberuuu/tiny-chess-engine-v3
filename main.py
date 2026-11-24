import os,json,urllib.request as w
U=os.getenv('MAKEFUN_ENV_URL','http://127.0.0.1:18080')
def P(p,b):return json.load(w.urlopen(w.Request(U+p,data=json.dumps(b).encode())))
V=(0,100,320,330,500,900,20000)
Y='00000000122,,2211/.00./1000440001125521122466422::::::::00000000&(****(&(,0110,(*123321**034430**134431**023320*(,0000,(&(****(&4620026444000044.,,,,,,.,**((**,*((&&((**((&&((**((&&((**((&&((*'
KN=(-33,-31,-18,-14,14,18,31,33)
KI=(-17,-16,-15,-1,1,15,16,17)
DG=(-17,-15,15,17)
OR=(-16,-1,1,16)
SQ=tuple(s for s in range(128)if not s&136)
CR=[15]*128
for s,v in((4,12),(0,13),(7,14),(116,3),(112,7),(119,11)):CR[s]=v
N=0;NB=20000
def W(p,s):
 q=(s>>4)*8+(s&7);a=p if p>0 else-p
 if 2<a<6:return V[a]if p>0 else-V[a]
 t=a-1 if a<3 else 2
 return(V[a]+(ord(Y[t*64+(q^56*(p<0))])-48)*5)*(1 if p>0 else-1)
def F(f):
 B=[9]*256;KS=[0,0]
 for s in SQ:B[s]=0
 a=f.split();r=7
 for row in a[0].split('/'):
  s=r*16
  for ch in row:
   if ch.isdigit():s+=int(ch)
   else:
    i='PNBRQKpnbrqk'.index(ch);p=i+1 if i<6 else 5-i
    B[s]=p
    if abs(p)==6:KS[p>0]=s
    s+=1
  r-=1
 SD=1-2*(a[1]=='b')
 C=sum(1<<'KQkq'.index(ch)for ch in a[2]if ch in'KQkq')
 EP=-1 if a[3]=='-'else 16*int(a[3][1])+ord(a[3][0])-113
 return(B,SD,C,EP,KS)
def AT(B,s,d):
 if d in(B[s-15*d],B[s-17*d]):return 1
 for O,P,L in((KN,2,0),(KI,6,0),(DG,3,1),(OR,4,1)):
  for o in O:
   t=s+o
   while B[t]!=9:
    v=B[t]
    if v:
     if v==P*d or(L and v==5*d):return 1
     break
    if not L:break
    t+=o
 return 0
def G(p,c):
 B,SD,C,EP,KS=p;m=[]
 def R(f,t):
  if(t>>4)==7*(SD>0):m.extend(f|(t<<7)|(q<<14)for q in(2,3,4,5))
  else:m.append(f|(t<<7))
 for s in SQ:
  x=B[s]
  if x==0 or(x>0)!=(SD>0):continue
  a=x if x>0 else-x
  if a==1:
   d=16*SD;t=s+d
   if B[t]==0:
    if(t>>4)==7*(SD>0)or not c:R(s,t)
    if not c and(s>>4)==6-5*(SD>0)and B[s+2*d]==0:m.append(s|((s+2*d)<<7))
   for o in(d-1,d+1):
    t=s+o;v=B[t]
    if v==9:continue
    if v and(v>0)!=(SD>0):R(s,t)
    elif t==EP:m.append(s|(t<<7))
  else:
   O=KN if a==2 else KI if a==6 else DG if a==3 else OR if a==4 else DG+OR
   L=a>2 and a!=6
   for o in O:
    t=s+o
    while B[t]!=9:
     v=B[t]
     if v:
      if(v>0)!=(SD>0):m.append(s|(t<<7))
      break
     if not c:m.append(s|(t<<7))
     if not L:break
     t+=o
   if a==6 and not c:
    e=4+112*(SD<0);D=-SD
    for k in(1,-1):
     if C&(1<<(2*(SD<0)+(k<0)))and B[e+k]==0 and B[e+2*k]==0 and(k>0 or B[e-3]==0)and not(AT(B,e,D)or AT(B,e+k,D)or AT(B,e+2*k,D)):m.append(e|((e+2*k)<<7))
 return m
def M(p,m):
 B,SD,C,EP,KS=p;b=B[:];k=KS[:]
 f=m&127;t=(m>>7)&127;q=m>>14
 x=b[f]
 b[f]=0
 if abs(x)==1 and t==EP and b[t]==0:b[t-16*SD]=0
 b[t]=q*SD if q else x
 if abs(x)==6 and abs(t-f)==2:
  r,n=(f+3,f+1)if t>f else(f-4,f-1)
  b[r]=0;b[n]=4*SD
 c=C&CR[f]&CR[t]
 e=(f+t)//2 if abs(x)==1 and abs(t-f)==32 else-1
 if abs(x)==6:k[SD>0]=t
 return(b,-SD,c,e,k)
def S(p,a,b,d,y):
 global N
 N+=1
 if N>=NB:raise StopIteration
 B,SD,C,EP,KS=p
 i=AT(B,KS[SD>0],-SD)
 if d<=0:
  if not i:
   s=sum(W(B[q],q)for q in SQ if B[q])*SD+10
   if s>=b:return b
   if s>a:a=s
   ms=G(p,1)
  else:ms=G(p,0)
 else:ms=G(p,0)
 ms.sort(key=lambda m:-V[abs(B[(m>>7)&127])])
 f=0
 for m in ms:
  p2=M(p,m)
  if AT(p2[0],p2[4][SD>0],-SD):continue
  f=1
  v=-S(p2,-b,-a,d-1,y+1)
  if v>a:a=v
  if a>=b:break
 if not f:return-100000+y if i else(0 if d>0 else a)
 return a
def U(m):
 f=m&127;t=(m>>7)&127;q=m>>14
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+('nbrq'[q-2]if q else'')
def H(fen,legal,*a):
 global N
 p=F(fen);N=0;bm=0
 SD=p[1]
 try:
  for d in range(1,40):
   ms=G(p,0)
   if bm in ms:ms.remove(bm);ms.insert(0,bm)
   a=-10**6;best=0
   for m in ms:
    p2=M(p,m)
    if AT(p2[0],p2[4][SD>0],-SD):continue
    v=-S(p2,-10**6,-a,d-1,1)
    if v>a:a=v;best=m
   if best:bm=best
 except StopIteration:pass
 except:return legal[0]
 return U(bm)if bm else legal[0]
while 1:
 try:g=P('/game',{})
 except:break
 if g.get('status')=='done':break
 while g.get('status')=='your_move':
  try:g=P('/move',{'game':g['game'],'move':H(g['fen'],g['legal_moves'],g.get('moves'))})
  except:break
