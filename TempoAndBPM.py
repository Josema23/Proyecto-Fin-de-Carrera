#!/usr/bin/env python
import midi
import os
import sys
import mido
import argparse
from mido import MidiFile, Message, tempo2bpm, second2tick

if (len(sys.argv) != 2):

    print 'Error en la ejecucion del programa'
    print "Uso del programa:"
    print "python prueba.py archivo.mid"

else:
    pass

    midi_file=MidiFile(sys.argv[1])
    length=midi_file.length
    print('Duracion: {} minutos, {} segundos.'.format(
            int(length / 60),
            int(length % 60)))

    print('Duracion: {} segundos.'.format(
            int(length)))

    for message in midi_file:
        if message.type == 'set_tempo':
            print('Tempo (BPM) {:.1f}'.format(
            tempo2bpm(message.tempo)))

            print('Tempo (Microsecs per Beat) {:.1f}'.format(
            message.tempo))

            print('Second2tick {:.1f}'.format(
            second2tick(length,105,message.tempo)))
