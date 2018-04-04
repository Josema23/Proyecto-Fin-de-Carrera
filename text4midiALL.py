#!/usr/bin/env python

'''
VERSION MEJORADA DE text4midiWMM

Programa completo de extraccion de mensajes y metamensajes, y su insercion en archivo.py para la construccion del midi

Programa hecho para extraer los diferentes instrumentos de bateria con la intencion de formar un unico midi.
Todas las notas mantendran su volumen, lo unico que hace es extraer los instrumentos de bateria

POSIBLE MEJORA

(HECHO) Establecer una condicion en cada mensaje de las notas que obligue a controlar el numero de canal (9) para asi asegurar
que las notas introducidas son de bateria y no pertenece a cualquier otro instrumento

Otra posible mejora seria introducir condiciones para TODOS los mensajes y metamensajes que puedan ser encontrados en cualquier
archivo midi. De esta forma, ningun mensaje quedaria atras y todos serian procesados con este programa

'''


import midi
import os
import sys
import mido
import argparse
from mido import MidiFile, Message



if (len(sys.argv) != 2):

    print(len(sys.argv))
    print 'Error en la ejecucion del programa'
    print "Uso del programa:"
    print "The arguments are: " , str(sys.argv)
    print "python [text4midiWMM.py] [archivo.mid] [nota]"
    sys.exit(1)

else:
    pass
    print("Ejecucion correcta")
    print "The arguments are: " , str(sys.argv)


def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

    print(len(sys.argv))


midi_file=MidiFile(sys.argv[1])

fichero = open ("Drums_Full"+".py", 'w')

for i, track in enumerate(midi_file.tracks):
    for msg in track:

        if (msg.type=='smpte_offset'):
	    fichero.write("track.append(MetaMessage('"+str(str(msg)[findnth(str(msg)," ", 1)+1:findnth(str(msg)," ", 2)])+"'"+str((str(msg)[findnth(str(msg)," ", 2):str(msg).find(">")]).replace(" ",","))+'))\n')

        elif (msg.type=='time_signature'):
		fichero.write("track.append(MetaMessage('"+str(str(msg)[findnth(str(msg)," ", 1)+1:findnth(str(msg)," ", 2)])+"'"+str((str(msg)[findnth(str(msg)," ", 2):str(msg).find(">")]).replace(" ",","))+'))\n')

        elif (msg.type=='key_signature'):
		fichero.write("track.append(MetaMessage('"+str(str(msg)[findnth(str(msg)," ", 1)+1:findnth(str(msg)," ", 2)])+"'"+str((str(msg)[findnth(str(msg)," ", 2):str(msg).find(">")]).replace(" ",","))+'))\n')

        elif (msg.type=='set_tempo'):
		fichero.write("track.append(MetaMessage('"+str(str(msg)[findnth(str(msg)," ", 1)+1:findnth(str(msg)," ", 2)])+"'"+str((str(msg)[findnth(str(msg)," ", 2):str(msg).find(">")]).replace(" ",","))+'))\n')

        elif (msg.type=='program_change' and msg.channel==9):
            fichero.write("track.append(Message('"+str(str(msg)[:str(msg).find(" ")])+"'"+str((str(msg)[str(msg).find(" "):]).replace(" ",","))+'))\n')

        elif (msg.type=='control_change' and msg.channel==9):
            fichero.write("track.append(Message('"+str(str(msg)[:str(msg).find(" ")])+"'"+str((str(msg)[str(msg).find(" "):]).replace(" ",","))+'))\n')

        elif (msg.type=='note_on' and msg.channel==9):
            fichero.write("track.append(Message('"+str(str(msg)[:str(msg).find(" ")])+"'"+str((str(msg)[str(msg).find(" "):]).replace(" ",","))+'))\n')

fichero.close()





'''



for i, track in enumerate(midi_file.tracks):
    if (track.name=='Drums'):                                   #Solo extrae aquellas pistas que sean de percusion
        fichero = open ("QueSaldra"+".py", 'w')
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if (msg.type=='program_change' or msg.type=='control_change' or msg.type=='note_on'):

                fichero.write("track.append(Message('"+str(str(msg)[:str(msg).find(" ")])+"'"+str((str(msg)[str(msg).find(" "):]).replace(" ",","))+'))\n')
fichero.close()
'''
