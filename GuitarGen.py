## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
from migconfigure import *
#import configuration

GuitarTones = {
"E" : [40], "Fb": [40], "E#": [41],
"F" : [41], "F#": [42], "Gb": [42],
"G" : [43], "G#": [44], "Ab": [44],
"A" : [45], "A#": [46], "Bb": [46],
"B" : [47], "Cb": [47], "B#": [48],
"C" : [48], "C#": [49], "Db": [49],
"D" : [50], "D#": [51], "Eb": [51]
}
#Guitar tones ***Different VST Guitars use different values, experimentation may be necessary for these numbers to properly match your VST Guitar.***

#GuitarGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List},UsedScale{List},Genre{String})
def GuitarGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre, TimeSig):
	trackname = "Rhythm Guitar"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = track
	volume = 100
	for i in range(len(GeneratedChords)):
		pitch = GuitarTones[GeneratedChords[i][0]][0]
		for x in range(0,len(GeneratedChords[i])):
			if GuitarTones[GeneratedChords[i][x]][0] < pitch:
				pitch = (GuitarTones[GeneratedChords[i][x]][0]) + 12
			elif GuitarTones[GeneratedChords[i][x]][0] >= pitch:
				pitch =	(GuitarTones[GeneratedChords[i][x]][0])
			else:
				print ("Something went terribly wrong")
			midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
		#Generate Rhythm Guitar
	if Guitar[1] == "Lead":
		time = 0
		track += 1
		channel = track
		trackname = "Lead Guitar"
		midi.addTrackName(track, time, trackname)
		midi.addTempo(track, time, bpm)
		try:
			for i in range(len(GeneratedChords)):
				rootpitch = GuitarTones[GeneratedChords[i][0]][0]
				try:
					secondpitch = GuitarTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 1) % len(UsedScale)]][0]
				except:
					pass
					#No second
				try:
					thirdpitch = GuitarTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 2) % len(UsedScale)]][0]
				except:
					pass
					#No Third

				try:
					fifthpitch = GuitarTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 4) % len(UsedScale)]][0]
				except:
					pass
					#No Fifth

				try:
					leadingpitch = GuitarTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) - 1) % len(UsedScale)]][0]
				except:
					pass
					#Leading note not possible

				RandomNum = random.randint(0,7)
				if RandomNum == 0:
					#Play just root note.
					midi.addNote(track, channel, rootpitch, time, Dur[i], volume)

				if RandomNum == 1:
					try:
						if (int(Dur[i]) >= 2):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
							Temptime = time + Dur[i]/2
							midi.addNote(track, channel, fifthpitch, Temptime, Dur[i]/2, volume)
							#Play root then fifth
						else:
							raise Exception
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#fifth doesn't exist in chord, play root.

				if RandomNum == 2:
					try:
						if (2 <=Dur[i]<=4):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
							Temptime = time + Dur[i]/2
							midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/2, volume)
							#Play root then third
						elif (Dur[i] > 4):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
							Temptime = time + Dur[i]/3
							midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/3, volume)
							Temptime = Temptime + Dur[i]/3
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#third doesn't exist in chord or duration too short, play root.
				if RandomNum == 3:
					try:
						if (Dur[i] % 4 == 0):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
							Temptime = time + Dur[i]/2
							midi.addNote(track, channel, leadingpitch,Temptime, Dur[i]/2, volume)
							#Play root then leading pitch
						elif (Dur[i] % 6 == 0):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
							Temptime = time + Dur[i]/3
							midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/3, volume)
							Temptime = Temptime + Dur[i]/3
							midi.addNote(track, channel, leadingpitch,Temptime, Dur[i]/3, volume)
							#root,thrid,leading.
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#third or leading doesn't exist in chord or duration too short, play root.
				if RandomNum == 4:
					try:
						if (Dur[i] > 2):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
							Temptime = time + Dur[i]/3
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
							Temptime = Temptime + Dur[i]/3
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
							#Play triplett on root
						elif (Dur[i] == 4):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/6, volume)
							Temptime = time + Dur[i]/6
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/6, volume)
							Temptime = Temptime + Dur[i]/6
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/6, volume)
							Temptime = Temptime + Dur[i]/6
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/2, volume)
							#Triplet then quarter note
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#Triplet not possible in context.
				if RandomNum == 5:
					try:
						if (Dur[i] > 2):
							midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
							Temptime = time + Dur[i]/3
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
							Temptime = Temptime + Dur[i]/3
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
							#Play triplett on root
						elif (Dur[i] > 2):
							midi.addNote(track, channel, rootpitch,time, Dur[i]/2, volume)
							Temptime = time + Dur[i]/2
							midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/6, volume)
							Temptime = Temptime + Dur[i]/6
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/6, volume)
							Temptime = Temptime + Dur[i]/6
							midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/6, volume)
							#Quarter note then triplet
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#Triplet not possible in context.
				if RandomNum == 6:
					try:
						if (fifthpitch in locals()):
							midi.addNote(track, channel, fifthpitch, time, Dur[i], volume)
							#play fifth.
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#fifth doesnt exist, play root.
				if RandomNum == 7:
					try:
						if (thridpitch in locals()):
							midi.addNote(track, channel, thridpitch, time, Dur[i], volume)
							#play fifth.
						else:
							raise ValueError
					except:
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						#fifth doesnt exist, play root.
				time = time + Dur[i]
		except:
			print("\nSoemthing has gone terribly wrong!\n")
			if Debug == True:
				traceback.print_exc()
	return midi
#Function for generating midi Guitar.
#midi{MIDIObject} returned.
