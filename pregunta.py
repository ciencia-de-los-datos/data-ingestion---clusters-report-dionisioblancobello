"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    with open('clusters_report.txt') as file:
        data = [line for line in file.readlines()]
    data = data[4:]
    data = [line.replace('\n', '') for line in data]
    data = [line.strip() for line in data]

    lista = []
    cadena = ''
    i = 0
    while i < len(data):
        if data[i] != '':
            cadena += ' ' + data[i]
        else:
            lista.append(cadena)
            cadena = ''
        i +=1

    lista = [line.strip() for line in lista]

    info = []
    for i in lista:
        regular = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', i)
        linea = regular.group(1) + '*' + regular.group(2) + '*' + regular.group(3) + '.' + regular.group(5) + '*' + regular.group(7)
        info.append(linea)
    datos = [line.split('*') for line in info]
    df = pd.DataFrame(columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    principales_palabras_clave = [line[3].replace('    ', ' ') for line in datos]
    principales_palabras_clave = [line.replace('   ', ' ') for line in principales_palabras_clave]
    principales_palabras_clave = [line.replace('  ', ' ') for line in principales_palabras_clave]
    principales_palabras_clave = [line.replace('.', '') for line in principales_palabras_clave]
    principales_palabras_clave = [line.split(',') for line in principales_palabras_clave]
    principales_palabras_clave = [[element.strip() for element in line] for line in principales_palabras_clave]
    principales_palabras_clave = [', '.join(line) for line in principales_palabras_clave]

    j = 0
    while j < 3:
        df[list(df.columns)[i]] = [element[i] for element in datos]
        j +=1
    df.principales_palabras_clave = principales_palabras_clave
    df.cluster = df.cluster.astype('int')
    df.cantidad_de_palabras_clave = df.cantidad_de_palabras_clave.astype('int')
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.astype('float')

    return df

