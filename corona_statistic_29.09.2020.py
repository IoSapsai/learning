import turtle

def drawbar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    
bl = (7952 / 302694)*100
brg = (6610 / 409265)*100
vn = (9505 / 469885)*100
vt = (2683 / 232568)*100
vdn = (1031 / 82835)*100
vrts = (2594 / 159470)*100
gbv = (3115 / 106598)*100
dbr = (2273 / 171809)*100
krd = (1379 / 158204)*100
kst = (3286 / 116915)*100
lv = (1370 / 122546)*100
mn = (2261 / 127001)*100
pz = (3538 / 252776)*100
pk = (2536 / 119190)*100
pvn = (3464 / 236305)*100
pvd = (13105 / 666801)*100
rr = (1576 / 110789)*100
rs = (4786 / 215477)*100
ss = (1562 / 108018)*100
svn = (3082	/ 184119)*100
smo = (1545 / 103532)*100
sf = (3874 / 226671)*100
sfg = (43318 / 1328790)*100
stz = (5958 / 313396)*100
trg = (1754	/ 110914)*100
hs = (2326 / 225317)*100
shum = (3001 / 172262)*100
ya = (2263 / 117335)*100

xs = [bl, brg, vn, vt, vdn, vrts, gbv, dbr, krd, kst, lv, mn, pz, pk, pvn, pvd, rr, rs, ss, svn, smo, sf, sfg, stz, trg, hs, shum, ya]

maxheight = max(xs)
bars = len(xs)
border = 1

wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*bars+border, maxheight+border)
stat = turtle.Turtle()
stat.color("blue")
stat.fillcolor("fuchsia")
stat.pensize(1)
stat.speed(50)
wn.bgcolor("black")

for a in xs:
    drawbar(stat, a)
    
wn.exitonclick()
print ("Percentage of people who contracted COVID - 19 by town, as of 29.09.2020:")
print ("Blagoevgrad - ", bl, "Burgas-", brg, "Varna- ", vn, "Veliko Tarnovo-", vt, "Vidin - ", vdn, "Vratsa - ", vrts, "Gabrovo - ", gbv,"Dobrich - ", dbr,"Kardjali - ", krd, "Kyustendil - " , kst, "Lovech - ", lv, "Montana - ", mn,"Pazardjik - ", pz,"Pernik - ", pk,"Pleven - ", pvn,"Plovdiv - ", pvd,"Razgrad - ", rr,"Rusa -", rs,"Silistra - ", ss,"Sliven - ", svn,"Smolyan -", smo,"Sofia, muncipality - " , sf,"Sofia city - " , sfg,"Stara Zagora -", stz,"Targovishte - ", trg,"Haskovo -", hs,"Shumen - ", shum, "Yambol -", ya)

