puntos = {}
with open('autoscope_agosto_2017.csv', encoding="latin-1") as f:
    lineas = f.readlines()
    i = 0
    for linea in lineas:
        if i == 0:
            i += 1
            continue
        arr = linea.split(';')

        d = {
            'avenida': arr[4],
            'esquina1': arr[5],
            'esquina2': arr[6],
            'lat': arr[7],
            'long': arr[8],
        }

        clave = d['avenida'] + '-' + d['esquina1'] + '-' + d['esquina2']
        puntos[clave] = d['lat'] + ',' + d['long']

        if i % 1000000:
            print(i)

        i += 1

f2 = open('puntos.csv', 'w')
for p in puntos.keys():
    linea = p + ';' + puntos[p]
    print(linea)
    f2.write(linea+"\n")
f2.close()