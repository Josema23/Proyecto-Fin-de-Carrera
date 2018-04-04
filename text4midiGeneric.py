#!/usr/bin/env python

'''
VERSION MEJORADA DE text4midiWMM

Programa completo de extraccion de mensajes y metamensajes, y su insercion en archivo.py para la construccion del midi

Programa hecho para separar los diferentes instrumentos de bateria en distintos archivos midi.
Las notas que sean introducidas por la terminal mantendran su volumen, mientras que el resto establecera su volumen en 0
Los ficheros de salida tendran el nombre del instrumento que corresponda con la nota introducida, proporcionando asi
un mejor manejo y mayor claridad a la hora de trabajar con ellos

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



if (len(sys.argv) != 3):

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
nota=sys.argv[2]

if (int(nota)==33):
    fichero = open ("Metronome_Click"+".py", 'w')
elif (int(nota)==34):
    fichero = open ("Metronome_Bell"+".py", 'w')
elif (int(nota)==35):
    fichero = open ("Acoustic_Bass_Drum"+".py", 'w')
elif (int(nota)==36):
    fichero = open ("Bass_Drum_1"+".py", 'w')
elif (int(nota)==37):
    fichero = open ("Side_Stick"+".py", 'w')
elif (int(nota)==38):
    fichero = open ("Acoustic_Snare"+".py", 'w')
elif (int(nota)==39):
    fichero = open ("Hand_Clap"+".py", 'w')
elif (int(nota)==40):
    fichero = open ("Electric_Snare"+".py", 'w')
elif (int(nota)==41):
    fichero = open ("Low_Floor_Tom"+".py", 'w')
elif (int(nota)==42):
    fichero = open ("Closed_Hi-Hat"+".py", 'w')
elif (int(nota)==43):
    fichero = open ("High_Floor_Tom"+".py", 'w')
elif (int(nota)==44):
    fichero = open ("Pedal_Hi-Hat"+".py", 'w')
elif (int(nota)==45):
    fichero = open ("Low_Tom"+".py", 'w')
elif (int(nota)==46):
    fichero = open ("Open_Hi-Hat"+".py", 'w')
elif (int(nota)==47):
    fichero = open ("Low-Mid_Tom"+".py", 'w')
elif (int(nota)==48):
    fichero = open ("Hi-Mid_Tom"+".py", 'w')
elif (int(nota)==49):
    fichero = open ("Crash_Cymbal_1"+".py", 'w')
elif (int(nota)==50):
    fichero = open ("High_Tom"+".py", 'w')
elif (int(nota)==51):
    fichero = open ("Ride_Cymbal_1"+".py", 'w')
elif (int(nota)==52):
    fichero = open ("Chinese_Cymbal"+".py", 'w')
elif (int(nota)==53):
    fichero = open ("Ride_Bell"+".py", 'w')
elif (int(nota)==54):
    fichero = open ("Tambourine"+".py", 'w')
elif (int(nota)==55):
    fichero = open ("Splash_Cymbal"+".py", 'w')
elif (int(nota)==56):
    fichero = open ("Cowbell"+".py", 'w')
elif (int(nota)==57):
    fichero = open ("Crash_Cymbal 2"+".py", 'w')
elif (int(nota)==58):
    fichero = open ("Vibraslap"+".py", 'w')
elif (int(nota)==59):
    fichero = open ("Ride_Cymbal_2"+".py", 'w')
elif (int(nota)==60):
    fichero = open ("Hi_Bongo"+".py", 'w')
elif (int(nota)==61):
    fichero = open ("Low_Bongo"+".py", 'w')
elif (int(nota)==62):
    fichero = open ("Mute_Hi_Conga"+".py", 'w')
elif (int(nota)==63):
    fichero = open ("Open_Hi_Conga"+".py", 'w')
elif (int(nota)==64):
    fichero = open ("Low_Conga"+".py", 'w')
elif (int(nota)==65):
    fichero = open ("High_Timbale"+".py", 'w')
elif (int(nota)==66):
    fichero = open ("Low_Timbale"+".py", 'w')
elif (int(nota)==67):
    fichero = open ("High_Agogo"+".py", 'w')
elif (int(nota)==68):
    fichero = open ("Low_Agogo"+".py", 'w')
elif (int(nota)==69):
    fichero = open ("Cabasa"+".py", 'w')
elif (int(nota)==70):
    fichero = open ("Maracas"+".py", 'w')
elif (int(nota)==71):
    fichero = open ("Short_Whistle"+".py", 'w')
elif (int(nota)==72):
    fichero = open ("Long_Whistle"+".py", 'w')
elif (int(nota)==73):
    fichero = open ("Short_Guiro"+".py", 'w')
elif (int(nota)==74):
    fichero = open ("Long_Guiro"+".py", 'w')
elif (int(nota)==75):
    fichero = open ("Claves"+".py", 'w')
elif (int(nota)==76):
    fichero = open ("Hi_Wood_Block"+".py", 'w')
elif (int(nota)==77):
    fichero = open ("Low_Wood_Block"+".py", 'w')
elif (int(nota)==78):
    fichero = open ("Mute_Cuica"+".py", 'w')
elif (int(nota)==79):
    fichero = open ("Open_Cuica"+".py", 'w')
elif (int(nota)==80):
    fichero = open ("Mute_Triangle"+".py", 'w')
elif (int(nota)==81):
    fichero = open ("Open_Triangle"+".py", 'w')

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

        elif (msg.type=='note_on' and msg.note==int(nota) and msg.channel==9):
            msg.velocity=msg.velocity
            fichero.write("track.append(Message('"+str(str(msg)[:str(msg).find(" ")])+"'"+str((str(msg)[str(msg).find(" "):]).replace(" ",","))+'))\n')

        elif (msg.type=='note_on' and msg.note!=int(nota) and msg.channel==9):
            msg.velocity=0
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
