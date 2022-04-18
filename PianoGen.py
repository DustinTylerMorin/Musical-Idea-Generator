## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
from migconfigure import *
#import configuration

PianoTones = {
"Ab": [56], "A" : [57], "A#": [58],
"Bb": [58], "B" : [59], "Cb": [59],
"B#": [60], "C" : [60], "C#": [61],
"Db": [61], "D" : [62], "D#": [63],
"Eb": [63], "E" : [64], "Fb": [64],
"E#": [65], "F" : [65], "F#": [66],
"Gb": [66], "G" : [67], "G#": [68]
}
#Piano tones

#PianoGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List},UsedScale{List},Genre{String})
def PianoGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre, TimeSig):
	trackname = "Piano"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = track
	volume = 100
	for i in range(len(GeneratedChords)):
		if GeneratedChords[i][0] != "Rest":
			pitch = PianoTones[GeneratedChords[i][0]][0]
			for x in range(0,len(GeneratedChords[i])):
				if PianoTones[GeneratedChords[i][x]][0] < pitch:
					pitch = (PianoTones[GeneratedChords[i][x]][0]) + 12
				elif PianoTones[GeneratedChords[i][x]][0] >= pitch:
					pitch =	(PianoTones[GeneratedChords[i][x]][0])
				else:
					print ("Something went terribly wrong")
				midi.addNote(track, channel, pitch, time, Dur[i], volume)
		else:
			midi.addNote(track, channel, 0, time, Dur[i], 0)
		time = time + Dur[i]
	if Piano[1] == "Lead":
		time = 0
		track += 1
		channel = track
		trackname = "Lead Piano"
		midi.addTrackName(track, time, trackname)
		midi.addTempo(track, time, bpm)
		try:
			for i in range(len(GeneratedChords)):
				if GeneratedChords[i][0] != "Rest":
					rootpitch = PianoTones[GeneratedChords[i][0]][0]
					try:
						secondpitch = PianoTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 1) % len(UsedScale)]][0]
					except:
						pass
						#No second
					try:
						thirdpitch = PianoTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 2) % len(UsedScale)]][0]
					except:
						pass
						#No Third

					try:
						fifthpitch = PianoTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 4) % len(UsedScale)]][0]
					except:
						pass
						#No Fifth

					try:
						leadingpitch = PianoTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) - 1) % len(UsedScale)]][0]
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
							elif (Dur[i] > 3):
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
				else:
					midi.addNote(track, channel, 0, time, Dur[i], 0)
				time = time + Dur[i]
		except:
			print("\nSoemthing has gone terribly wrong!\n")
			if Debug == True:
				traceback.print_exc()
	return midi
#Function for generating midi Piano.
#midi{MIDIObject} returned.
