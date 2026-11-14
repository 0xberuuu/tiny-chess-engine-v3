import json as j,os,urllib.request as u
E=os.getenv('MAKEFUN_ENV_URL')
def P(p,b):return j.load(u.urlopen(E+p,j.dumps(b).encode()))
V=[0,100,320,330,500,900,0]
T=b'FFFFKKKKKPPKPUUPUZZUZddZdnndFFFF-7<A7FKP<KUUAPUZAPUZ<KUU7FPP-7<A<AFFAKKKFPPPFPUUFPUUFPPPAKKK<AFF'+b'FFKK'*6+b'PUUUFFFF<AFFAFKKFKKKFKPPFKPPFKKKAFKK<AFFUZPFPPFAFFA<<<77772222----(((((('
N8=[-33,-31,-18,-14,14,18,31,33];R4=[-16,-1,1,16];B4=[-17,-15,15,17];K8=R4+B4
RM={0:2,4:3,7:1,112:8,116:12,119:4}
Z=[i*0x9E3779B9%2**64 for i in range(1,1666)]
B=[9]*256;SD=1;C=SC=0;EP=-1;KS=[0,0];ST=[];H=0;TT={}
X=Exception;NB=25e3;N=0
def W(p,s):a=abs(p);r=s>>4;f=s&7;return(V[a]+T[(a-1)*32+(r,7-r)[p<0]*4+min(f,7-f)]-70)*(p//a)
def AT(s,by):
 t=s-16*by
 if by in(B[t-1],B[t+1])or any(B[s+o]==2*by for o in N8):return 1
 for o in K8:
  t=s+o
  while B[t]==0:t+=o
  if B[t]*by in(5,4-(abs(o)in(15,17)),6*(t==s+o)):return 1
 return 0
def G(cap):
 M=[];A=M.append;Y=lambda:[A((s,t,q))for q in(5,4,3,2)]
 for s in range(128):
  p=B[s]
  if not 0<p*SD<7:continue
  a=abs(p)
  if a==1:
   d=16*SD;t=s+d
   if B[t]==0:
    if t>>4 in(0,7):Y()
    elif not cap:
     A((s,t,0))
     if s>>4==1+5*(SD<0) and B[s+2*d]==0:A((s,s+2*d,0))
   for t in(s+d-1,s+d+1):
    if -6<B[t]*SD<0 or t==EP:
     if t>>4 in(0,7):Y()
     else:A((s,t,0))
  elif a in(2,6):
   for o in(K8,N8)[a==2]:
    t=s+o;v=B[t]
    if v==cap==0 or-6<v*SD<0:A((s,t,0))
   if a==6 and not cap:
    for q2 in(1,-1):
     k2=(1+(q2<0))<<2*(SD<0)
     if C&k2 and B[s+q2]==B[s+2*q2]==0 and(q2>0 or B[s-3]==0)and AT(s,-SD)==AT(s+q2,-SD)==AT(s+2*q2,-SD)==0:A((s,s+2*q2,0))
  else:
   for o in(B4,R4,K8)[a-3]:
    t=s+o
    while B[t]==0:cap or A((s,t,0));t+=o
    if -6<B[t]*SD<0:A((s,t,0))
 return M
def MK(m):
 global C,EP,SC,SD,H
 f,t,q=m;p=B[f];d=-W(p,f);x=0;xs=-1;h=H
 if p*p==1 and t==EP:xs=t-16*SD;x=B[xs];d-=W(x,xs);B[xs]=0;H^=Z[(x+6)<<7|xs]
 elif B[t]:x=B[t];xs=t;d-=W(x,t);H^=Z[(x+6)<<7|t]
 H^=Z[(p+6)<<7|f];B[f]=0;n=SD*q if q else p;B[t]=n;d+=W(n,t);H^=Z[(n+6)<<7|t]
 if p*p==36:
  KS[SD>0]=t
  if abs(t-f)==2:
   rf=f+3-7*(t<f);rt=f+1-2*(t<f);r=B[rf];d-=W(r,rf);H^=Z[(r+6)<<7|rf];B[rt]=r;B[rf]=0;d+=W(r,rt);H^=Z[(r+6)<<7|rt]
 ST.append((x,xs,C,EP,SC,h));C&=~RM.get(f,0)&~RM.get(t,0);EP=f+16*SD if p*p==1 and t-f==32*SD else-1;SC+=d;SD=-SD;H^=Z[1664]
def UM(m):
 global C,EP,SC,SD,H
 SD=-SD;f,t,q=m;x,xs,C,EP,SC,H=ST.pop();p=SD if q else B[t]
 if p*p==36:
  KS[SD>0]=f
  if abs(t-f)==2:
   rf=f+3-7*(t<f);rt=f+1-2*(t<f);B[rf]=B[rt];B[rt]=0
 B[f]=p;B[t]=0
 if xs>=0:B[xs]=x
def S(d,a,b,nm=1):
 global N,C,EP,SC,SD,H
 N+=1
 if N>NB:raise X
 if d<-8:return SC*SD
 e=TT.get(H);tm=e[3]if e else 0
 if e and e[0]>=d:
  v=e[1];f=e[2]
  if f==0 or f==1 and v>=b or f==2 and v<=a:return v
 chk=AT(KS[SD>0],-SD)
 if d<=0 and not chk and(a:=max(a,SC*SD))>=b:return b
 if nm and d>2 and not chk and SC*SD>=b and b<9e4:
  ST.append((C,EP,SC,H));H^=Z[1664];EP=-1;SD=-SD
  v=-S(d-3,-b,1-b,0)
  SD=-SD;C,EP,SC,H=ST.pop()
  if v>=b:return b
 M=G(0 if d>0 else 1-chk);M.sort(key=lambda m:-20000*(m==tm)-V[abs(B[m[1]])]*64-900*m[2]);lg=0;bm=0;o=a
 for m in M:
  MK(m)
  if AT(KS[SD<0],SD):UM(m);continue
  lg+=1;v=-S(d-1,-b,-a);UM(m)
  if v>a:a=v;bm=m
  if a>=b:break
 if lg==0:return-1e5 if chk else(0 if d>0 else a)
 if abs(a)<9e4:TT[H]=(d,a,(a>=b)+2*(a<=o),bm)
 return a
def U2(x):return(ord(x[0])+16*ord(x[1])-881,ord(x[2])+16*ord(x[3])-881,x[4:]and'nbrq'.index(x[4])+2 or 0)
def F():
 global B,SD,C,EP,SC,KS,ST,H
 B=([0]*8+[9]*8)*8+[9]*128;SC=0;H=0
 for f,p in enumerate((4,2,3,5,6,3,2,4)):
  for s,q in((f,p),(f+16,1),(f+96,-1),(f+112,-p)):B[s]=q;SC+=W(q,s);H^=Z[(q+6)<<7|s]
 KS=[116,4];SD=1;C=15;EP=-1;ST=[]
def H(fen,legal,mv):
 global N
 N=0;F()
 for x in mv:MK(U2(x))
 R=[(x,U2(x))for x in legal]
 if len(TT)>2e5:TT.clear()
 best=R[0][0]
 for d in range(12):
  try:
   a=-1e6;cb=best
   for x,m in R:
    MK(m);v=-S(d,-1e6,-a);UM(m)
    if v>a:a=v;cb=x
   best=cb
  except X:break
 return best
while(g:=P('/game',{}))['status']!='done':
 while g['status']=='your_move':
  l=g['legal_moves']
  try:mv=H(g['fen'],l,g['moves'])
  except:mv=l[0]
  g=P('/move',{'game':g['game'],'move':mv})
