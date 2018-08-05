import json

# el archivo sarmiento_requena_rambla.csv surge de hacer
#  grep ";Sarmiento;Requena;Rambla;" autoscope_agosto_2017.csv > sarmiento_requena_rambla.csv
trafico = {}
with open('sarmiento_requena_rambla.csv', encoding="latin-1") as f:
    lineas = f.readlines()
    i = 0
    for linea in lineas:
        arr = linea.split(';')
        d = {
            'fecha': arr[2],
            'hora': arr[3],
            'carril': arr[1],
            'avenida': arr[4],
            'esquina1': arr[5],
            'esquina2': arr[6],
            'autos': int(arr[9])
        }

        hora = d['hora']
        if d['fecha'] == '2017-08-01':
            # la hora exacta aparece una vez por cada carril, yo sumo los volumenes de los carriles
            # no me interesa el detalle de cada carril
            if not hora in trafico:
                trafico[hora] = d['autos']
            else:
                trafico[hora] += d['autos']

f2 = open('estudio_avenida.csv', 'w')
for hora in trafico.keys():
    linea = '{},{}'.format(hora,trafico[hora])
    print(linea)
    f2.write(linea + "\n")
f2.close()

# ideas:
#   avenidas mas transitadas
#   diferencias con el fin de semana
#   muestreo de avenidas
