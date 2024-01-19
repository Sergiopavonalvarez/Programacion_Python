

base=int(input("Introduzca la base imponible: "))
tipo=input("Introduzca el tipo de IVA (general, reducido o supereducido ")

tgeneral=21
treducido=10
tsuperreducido=4
iva=0
codigo=input("Introduzca el codigo promocional: nopro, mitad, meno5, 5porc ")

if tipo=="general":
    iva=base*(tgeneral/100)
if tipo=="reducido":
    iva=base*(treducido/100)
if tipo=="supereducido":
    iva=base*(tsuperreducido/100)
precioiva=base+iva
promocion=0

if codigo=="mitad":
    promocion=base/2
if codigo=="meno5":
    promocion=5
if codigo=="5porc":
    promocion = (base * 5) / 100

print("Base imponible: ",base)
print("IVA: ",tipo,":",iva)
print("Precio con IVA: ",precioiva)
print("Cod. promo. ",codigo," : -",promocion)
print(" TOTAL: ",precioiva-promocion)
