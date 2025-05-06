from exercici2 import ciutats

# Cercant una ciutat per codi postal

codi_pos = int(input("Introdueix el codi postal de la ciutat que vols cercar: "))
ciutat = ciutats.get(codi_pos)
print(ciutat)   

