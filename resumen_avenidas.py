import json
# ['id_detector', 'id_carril', 'fecha', 'hora', 'dsc_avenida', 'dsc_int_anterior', 'dsc_int_siguiente', 'latitud', 'longitud', 'volumen', 'volumen_hora']

#lines: 2M
with open('autoscope_agosto_2017.csv', encoding="latin-1") as f:
# with open('1000.csv', encoding="latin-1") as f:
    lineas = f.readlines()
    i = 0
    avs = {}

    for linea in lineas:
        if i == 0:
            i += 1
            continue
        arr = linea.split(';')

        d = {
            'fecha': arr[2],
            'hora': arr[3],
            'avenida': arr[4],
            'esquina1': arr[5],
            'esquina2': arr[6],
            'autos': arr[9]
        }

        clave = d['avenida']
        fecha = d['fecha']
        if clave in avs:
            avs[clave]['cant'] += 1
            avs[clave]['fecha'].add(fecha)
            avs[clave]['esquina1'].add(d['esquina1'])
            avs[clave]['esquina2'].add(d['esquina2'])
        else:
            avs[clave] = {
                'esquina1': {d['esquina1']},
                'esquina2': {d['esquina2']},
                'cant': 1,
                'fecha': {fecha}
            }

        if i % 1000000:
            print(i)

        i += 1

    for clave in avs.keys():
        avs[clave]['esquina1'] = list(avs[clave]['esquina1'])
        avs[clave]['esquina2'] = list(avs[clave]['esquina2'])
        avs[clave]['fecha'] = sorted(list(avs[clave]['fecha']))
        print(clave)

    result = json.dumps(avs, indent=2)
    print(result)
    f2 = open('resumen_avenidas.json','w', encoding="latin-1")
    f2.write(result)
