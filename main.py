"""
for i in range(0,101):
  if i % 2==0 and i%3==0:
    print("fizzbuzz")
  elif i % 3==0:
    print("buzz")
  elif i % 2==0:
    print("fizz")
  else:
    print(i)


"""
alma = "szia uram"

for betu in alma:
  print(betu)

igaz = None
print(type(igaz))

lista=["január","február","március",1,2,3,4,5.01,True]
for i in lista:
  print(i)
  if i =="március":
    lista.remove("március")

print(f"A lista harmadik eleme: {lista[2]}")



print("_____________________indexelés____________________________")
szoveg="elkáposztástalanították"
print(f"A szöveg változónak első karaktere: {szoveg[1]}")  # indexelésnek nevezzük amikor egy bizonyos dolognak csak egyes elemeit akarjuk látni vagy használni 

print(f"A szöveg változónak ötödik karaktere: {szoveg[4]}")

# indexelés 0 tól kezdödik

print(f"A szöveg változónak utolsó karaktere: {szoveg[-1]}")

print(f"A szöveg első négy karaktere: {szoveg[0:4]}")

print(f"A szöveg első négy karaktere: {szoveg[:4]}")

#káposztástalanit
print(szoveg[2:-5])

print(szoveg[5:])


e_betusek = ["Elemér","elem","eszes","egér","Endre","eper","elvezet","Eszter","Evelin"]
print("tulajdon nevek__________________________________")
for szo in e_betusek:
  if szo[0] == "E":
    print(szo)

print("köznevek_____________________________________")
for szo in e_betusek:
  if szo[0] == "e":
    print(szo)

print("tulajdon nevek nagy betüvel_______________________")
for szo in e_betusek:
  if szo[0] == "E":
    print(szo.upper())


print("tulajdon nevek kis betüvel betüvel_______________________")
for szo in e_betusek:
  if szo[0] == "E":
    print(szo.lower())

print("köznevek nagy betüvel kezdődve__________________________")
for szo in e_betusek:
  if szo[0] == "e":
    print(szo.capitalize())


print("tulajdon nevek r-rel végződve__________________________")
for szo in e_betusek:
  if szo[0] == "E" and szo[-1] =="r":
    print(szo)

e_betusek = ["Elemér","elem","eszes","egér","Endre","eper","elvezet","Eszter","Evelin"]

e_betusek1= 0
nagy_e_betusek= 0
for szo in e_betusek:
  if szo[0] =="e":
    e_betusek1 += 1
  if szo[0] =="E":
    nagy_e_betusek += 1

print(e_betusek1)
print(nagy_e_betusek)
    
    


