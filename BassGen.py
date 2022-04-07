## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
from migconfigure import *
#import configuration

BassTones = {
"E" : [28], "Fb": [28], "E#": [29],
"F" : [29], "F#": [30], "Gb": [30],
"G" : [31], "G#": [32], "Ab": [32],
"A" : [33], "A#": [34], "Bb": [34],
"B" : [35], "Cb": [35], "B#": [36],
"C" : [36], "C#": [37], "Db": [37],
"D" : [38], "D#": [39], "Eb": [39]
}
#Bass tones ***Different VST Basses use different values, experimentation may be necessary for these numbers to properly match your VST Bass.***

#BassGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List},UsedScale{List},Genre{String})
def BassGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre):
	trackname = "Bass"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = track
	volume = 100
	try:
		for i in range(len(GeneratedChords)):
			rootpitch = BassTones[GeneratedChords[i][0]][0]
			try:
				secondpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 1) % len(UsedScale)]][0]
			except:
				pass
				#No second
			try:
				thirdpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 2) % len(UsedScale)]][0]
			except:
				pass
				#No Third

			try:
				fifthpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 4) % len(UsedScale)]][0]
			except:
				pass
				#No Fifth
			try:
				sixthpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 5) % len(UsedScale)]][0]
			except:
				pass
				#No Sixth
			try:
				seventhpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) + 6) % len(UsedScale)]][0]
			except:
				pass
				#No Seventh

			try:
				leadingpitch = BassTones[UsedScale[(UsedScale.index(GeneratedChords[i][0]) - 1) % len(UsedScale)]][0]
			except:
				pass
				#Leading note not possible

			if Bass[1] == "Basic":
				try:
					#Just play root notes.
					midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
				except:
					raise ValueError
			if Bass[1] == "Advanced":
				if Genre == "Pop":
					RandomNum = random.randint(0,4)
					if RandomNum == 0:
						#Play just root note.
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 1:
						try:
							if (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, leadingpitch,Temptime, Dur[i]/2, volume)
								#Play root then leading pitch
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
					if RandomNum == 2:
						try:
							if (Dur[i] % 2 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/2, volume)
								#Play root then fifth pitch
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
					if RandomNum == 3:
						try:
							if (Dur[i] % 2 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/2, volume)
								#Play root then root
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
					if RandomNum == 4:
						try:
							if (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/2, volume)
								#Play root then leading pitch
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
				if Genre == "Rock":
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
							if (Dur[i] == 2):
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
							if (Dur[i] == 1):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
								Temptime = time + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								Temptime = Temptime + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								#Play triplett on root
							elif (Dur[i] == 2):
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
				if Genre == "Metal":
					RandomNum = random.randint(0,4)
					if RandomNum == 0:
						#Play just root note.
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 1:
						try:
							if (Dur[i] == 1):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
								Temptime = time + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								Temptime = Temptime + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								#Play triplett on root
							elif (Dur[i] % 2 == 0):
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
					if RandomNum == 2:
						try:
							if (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/4, volume)
								#Play root then fifth then root pitch
							elif (Dur[i] % 2 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/4, volume)
								#Play root then fifth then root pitch
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
					if RandomNum == 3:
						try:
							if (Dur[i] % 4 == 1):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
								Temptime = time + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								Temptime = Temptime + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								#Play root 3 times
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
					if RandomNum == 4:
						try:
							if (Dur[i] % 3 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/3, volume)
								Temptime = time + Dur[i]/3
								midi.addNote(track, channel, seventhpitch,Temptime, Dur[i]/3, volume)
								Temptime = Temptime + Dur[i]/3
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/3, volume)
								#Play root 3 times
							else:
								midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
						except:
							raise ValueError
				if Genre == "Blues":
					RandomNum = random.randint(0,3)
					if RandomNum == 0:
						#Play just root note.
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 1:
						try:
							if (Dur[i] % 8 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/8, volume)
								Temptime = time + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, sixthpitch, Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, seventhpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, sixthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								#Walking bass on chord tones
							elif (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch,time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, thirdpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/4, volume)
								#Walking bass on chord tones
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 2:
						try:
							if (Dur[i] % 8 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/8, volume)
								Temptime = time + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, sixthpitch, Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, seventhpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, sixthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								#Walking bass on chord tones
							elif (Dur[i] == 4):
								midi.addNote(track, channel, rootpitch,time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, thirdpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/4, volume)
								#Walking bass on chord tones
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 3:
						try:
							if (Dur[i] % 8 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/8, volume)
								Temptime = time + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch, Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, seventhpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, sixthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/8, volume)
								Temptime = Temptime + Dur[i]/8
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/8, volume)
								#Walking bass on chord tones
							elif (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch,time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, thirdpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, seventhpitch,Temptime, Dur[i]/4, volume)
								#Walking bass on chord tones
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
				if Genre == "Country":
					RandomNum = random.randint(0,5)
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
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/2, volume)
								#Play root then third
							elif (Dur[i] > 4):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
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
							if (Dur[i] == 2):
								midi.addNote(track, channel, fifthpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/2, volume)
								#Play fifth root
							elif (Dur[i] % 4 == 0):
								midi.addNote(track, channel, fifthpitch, time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								#fifth, root, root, fifth
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
							#Triplet not possible in context.
					if RandomNum == 5:
						try:
							if (Dur[i] % 4 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/2, volume)
								Temptime = time + Dur[i]/2
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								#root third fifth
							elif (Dur[i] % 2 == 0):
								midi.addNote(track, channel, rootpitch,time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, fifthpitch,Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, thirdpitch,Temptime, Dur[i]/4, volume)
								#Quarter note then triplet
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
							#Triplet not possible in context.
				if Genre == "Punk":
					RandomNum = random.randint(0,2)
					if RandomNum == 0:
						#Play just root note.
						midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
					if RandomNum == 1:
						try:
							if (int(Dur[i]) % 4 == 0):
								midi.addNote(track, channel, rootpitch, time, Dur[i]/4, volume)
								Temptime = time + Dur[i]/4
								midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/4, volume)
								Temptime = Temptime + Dur[i]/4
								midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/4, volume)
								#4xroot
							else:
								raise Exception
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
							#fifth doesn't exist in chord, play root.

					if RandomNum == 2:
						try:
							Temptime = time
							for x in range(1,Dur[i]+1):
								midi.addNote(track, channel, rootpitch, Temptime, Dur[i]/Dur[i], volume)
								Temptime = Temptime + Dur[i]/Dur[i]
							else:
								raise ValueError
						except:
							midi.addNote(track, channel, rootpitch, time, Dur[i], volume)
							#third doesn't exist in chord or duration too short, play root.
			time = time + Dur[i]
	except ValueError as error:
		print("\nSomething has went wrong\n")
		if Debug == True:
			traceback.print_exc()
	return midi
#Function for generating midi Bass.
#midi{MIDIObject} returned.
