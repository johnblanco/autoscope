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
        puntos[clave] = {'coordenadas': d['lat'] + ' ' + d['long'],
                         'avenida': d['avenida'],
                         'esquina1': d['esquina1'],
                         'esquina2': d['esquina2']}

        if i % 1000000:
            print(i)

        i += 1

f2 = open('puntos.csv', 'w')
f2.write('avenida,esquina 1,esquina 2, coordenadas\n')
for p in puntos.keys():
    linea = '{},{},{},{}'.format(puntos[p]['avenida'],puntos[p]['esquina1'],puntos[p]['esquina2'],
                      puntos[p]['coordenadas'])
    f2.write(linea+"\n")
    print(linea)
f2.close()
