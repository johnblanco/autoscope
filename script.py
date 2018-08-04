#['id_detector', 'id_carril', 'fecha', 'hora', 'dsc_avenida', 'dsc_int_anterior', 'dsc_int_siguiente', 'latitud', 'longitud', 'volumen', 'volumen_hora']
with open('autoscope_agosto_2017.csv', encoding="latin-1") as f:
    lines = f.readlines()
    i=0

    avs = {}

    for line in lines:
        if i == 0:
            i+=1
            continue
        arr = line.split(';')

        d = {
            'date': arr[2],
            'time': arr[3],
            'avenue': arr[4],
            'corner1': arr[5],
            'corner2': arr[6],
            'cars': arr[9]
        }

        key = d['avenue']
        if d['avenue'] in avs:
            avs[key]['count'] += 1
            avs[key]['days'].update(d['date'])
            avs[key]['corner1'].update(d['corner1'])
            avs[key]['corner2'].update(d['corner2'])
        else:
            avs[key] =  {
                'corner1': {d['corner1']},
                'corner2': {d['corner2']},
                'count': 1,
                'days': {d['date']}
            }


        print(avs)

        if i > 10:
            exit()
        i+=1