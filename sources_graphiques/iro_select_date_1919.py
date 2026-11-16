# Dessine l'image du signet 1919 : village du Nord en ruine à l'aube après l'armistice.
import random, math, sys
from PIL import Image, ImageDraw, ImageFilter
S=4; W,H=180*S,104*S
random.seed(1919)
img=Image.new("RGBA",(W,H))
d=ImageDraw.Draw(img)
# ciel : aube d'hiver, gris-bleu en haut, ocre pâle à l'horizon
top=(58,66,80); mid=(150,132,104); hor=(214,180,122)
for y in range(H):
    t=y/(H*0.62)
    if t<0.6: c=[int(top[i]+(mid[i]-top[i])*t/0.6) for i in range(3)]
    else:
        u=min((t-0.6)/0.4,1); c=[int(mid[i]+(hor[i]-mid[i])*u) for i in range(3)]
    d.line([(0,y),(W,y)],fill=tuple(c)+(255,))
# soleil bas, voilé
sun=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sun)
sd.ellipse([W*0.66-38,H*0.58-38,W*0.66+38,H*0.58+38],fill=(240,214,160,170))
img=Image.alpha_composite(img,sun.filter(ImageFilter.GaussianBlur(10)))
d=ImageDraw.Draw(img)
# nuages en bandes
for i in range(9):
    y=random.randint(int(H*0.08),int(H*0.45)); x=random.randint(-100,W); w=random.randint(120,300)
    cl=Image.new("RGBA",(W,H),(0,0,0,0)); cd=ImageDraw.Draw(cl)
    cd.ellipse([x,y,x+w,y+random.randint(10,22)],fill=(40,44,54,110))
    img=Image.alpha_composite(img,cl.filter(ImageFilter.GaussianBlur(6)))
d=ImageDraw.Draw(img)
far=(92,84,78); near=(38,34,32)
hz=int(H*0.62)
# collines lointaines
pts=[(0,hz)]+[(x,hz-8-12*math.sin(x/90)-6*math.sin(x/37)) for x in range(0,W+1,8)]+[(W,hz+10),(0,hz+10)]
d.polygon(pts,fill=far+(255,))
# ruines lointaines : murs écroulés et clocher éventré
def mur(x,b,w,h,c):
    p=[(x,b)]; n=6
    for k in range(n+1):
        p.append((x+w*k/n,b-h*random.uniform(0.4,1.0)))
    p.append((x+w,b)); d.polygon(p,fill=c)
for x in (40,110,170,420,470,540,600):
    mur(x,hz+4,random.randint(30,60),random.randint(14,30),(74,66,62,255))
# clocher éventré
cx=300; b=hz+6
d.polygon([(cx-22,b),(cx-22,b-95),(cx-6,b-118),(cx+4,b-104),(cx+12,b-122),(cx+22,b-92),(cx+22,b)],fill=(66,58,56,255))
d.rectangle([cx-8,b-80,cx+6,b-58],fill=(176,150,110,255))  # baie ouverte sur le ciel
d.polygon([(cx-60,b),(cx-60,b-40),(cx-40,b-52),(cx-30,b-30),(cx-22,b-34),(cx-22,b)],fill=(66,58,56,255))
d.polygon([(cx+22,b),(cx+22,b-28),(cx+40,b-46),(cx+52,b-20),(cx+70,b-26),(cx+70,b)],fill=(66,58,56,255))
# sol boueux, trous d'obus
for y in range(hz,H):
    u=(y-hz)/(H-hz); c=[int(far[i]*(1-u)+near[i]*u) for i in range(3)]
    d.line([(0,y),(W,y)],fill=tuple(c)+(255,))
for _ in range(26):
    x=random.randint(0,W); y=random.randint(hz+12,H-10); r=random.randint(10,28)
    d.ellipse([x-r,y-r*0.3,x+r,y+r*0.3],fill=(30,27,26,255))
    d.arc([x-r,y-r*0.3,x+r,y+r*0.3],190,350,fill=(120,108,92,255),width=2)
# eau stagnante qui reflète le ciel
d.ellipse([W*0.55,H*0.80,W*0.80,H*0.86],fill=(170,146,108,255))
# arbres déchiquetés
def arbre(x,b,h,w):
    d.polygon([(x-w,b),(x-w*0.5,b-h),(x+w*0.2,b-h*1.05),(x+w,b)],fill=near+(255,))
    for k in range(2):
        yy=b-h*random.uniform(0.5,0.9); s=random.choice((-1,1))
        d.line([(x,yy),(x+s*random.randint(10,24),yy-random.randint(8,18))],fill=near+(255,),width=3)
for x,h in ((60,120),(92,70),(640,140),(690,90),(250,60)):
    arbre(x,H-6,h,7)
# piquets et barbelés au premier plan
piq=[20,130,210,330,450,560,700]
for x in piq:
    yb=H-random.randint(4,18); d.line([(x,yb),(x+random.randint(-6,6),yb-random.randint(34,52))],fill=(26,23,22,255),width=4)
for row in (0,1):
    pts=[]
    for x in range(0,W+1,6):
        pts.append((x,H-34+row*14+5*math.sin(x/15+row)))
    d.line(pts,fill=(28,25,24,255),width=1)
    for x in range(0,W,22):
        y=H-34+row*14+5*math.sin(x/15+row)
        d.line([(x-3,y-3),(x+3,y+3)],fill=(28,25,24,255),width=1)
img=img.resize((180,104),Image.LANCZOS)
# vignette légère
v=Image.new("L",(180,104),0); vd=ImageDraw.Draw(v)
vd.ellipse([-30,-30,210,134],fill=255); v=v.filter(ImageFilter.GaussianBlur(18))
dark=Image.new("RGBA",(180,104),(20,18,18,255)); 
out=Image.composite(img,Image.blend(img,dark,0.45),v)
# encoche du bas (cercle de rayon 35 centré en x=90, y=130, d'après le wiki) laissée transparente
a=out.split()[3].copy(); ad=ImageDraw.Draw(a); ad.ellipse([90-35,130-35,90+35,130+35],fill=0)
out.putalpha(a)
out.save(sys.argv[1])
