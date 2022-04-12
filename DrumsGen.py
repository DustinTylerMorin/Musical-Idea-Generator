## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
from migconfigure import *
#import configuration

DrumTones = {
"Kick": [36],
"Snare": [38],
"Hand Clap": [39],
"Rim": [40],
"ClosedHat": [42],
"OpenHat": [46],
"Crash": [49],
"Ride": [48],
"Floor": [57],
"Rack1": [45],
"Rack2": [43]
}
#Drum tones ***Different VST Drums use different values, experimentation may be necessary for these numbers to properly match your VST Drums.***

#DrumGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},Genre{String})
def DrumsGen(midi, track, bpm, Dur, Genre):
	trackname = "Drums"
	channel = track
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	volume = 100
	if Genre == None:
		Genre = Drums[1]

	TotalDur = 0

	if Genre == "Pop":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], (x/2-.25), .5, volume-25)
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur-.5), .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], (x/2-.25), .5, volume-25)
					midi.addNote(track, channel,DrumTones["Hand Clap"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur-.5), .5, volume-25)

	elif Genre == "Rock":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,2)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-75)
			midi.addNote(track, channel, DrumTones["OpenHat"][0], (TotalDur-.5), .5, volume-75)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-75)
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur-.5), .5, volume-75)
		if RandomNum == 2:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume)
			midi.addNote(track, channel, DrumTones["Ride"][0], (TotalDur-.5), .5, volume)

	if Genre == "Metal":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		for x in range (TotalDur * 2 - 1):
			if x%4 == 2:
				midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
				#Snare
			if x%4 == 0:
				midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
				midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
				midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .5, .5, volume)
				#Kick
			midi.addNote(track, channel, DrumTones["Crash"][0], x/2, .5, volume-25)
		midi.addNote(track, channel, DrumTones["Crash"][0], (TotalDur-.5), .5, volume-25)

	if Genre == "Blues":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum  = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, 1, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, 1, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 2, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2 + .5, .5, volume-25)
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, 1, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, 1, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, 1, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 2, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2 + .5, .5, volume-25)
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)

	if Genre == "Country":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 1:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2+.25, .25, volume-25)
					pass
					#Hat
				if x%4 == 3:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2+.25, .25, volume-25)
					pass
					#Hat
				if x%4 == 2:
					#midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2-.25, .25, volume-25)
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .75, volume-25)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur - .25), .25, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%8 == 1:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
					#Hat
				if x%4 == 2:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2-.25, .5, volume-25)
					midi.addNote(track, channel,DrumTones["Rim"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2 +.75, .5, volume-25)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur-.5), .5, volume-25)
			#add missing last hat beat
	if Genre == "Punk":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-25)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .75, volume-25)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				if x%2 == 1:
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .75, volume-25)
					#Hat
			midi.addNote(track, channel, DrumTones["OpenHat"][0], (TotalDur - .5), .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					#midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2-.25, .25, volume-25)
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-25)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .75, volume-25)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .5 , .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				if x%2 == 1:
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .75, volume-25)
			midi.addNote(track, channel, DrumTones["OpenHat"][0], (TotalDur - .5), .5, volume-25)
			#add missing last hat beat
	elif Genre == "Stoner Rock":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,2)
		if RandomNum == 0:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-75)
			midi.addNote(track, channel, DrumTones["OpenHat"][0], (TotalDur-.5), .5, volume-75)
		if RandomNum == 1:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-75)
			midi.addNote(track, channel, DrumTones["ClosedHat"][0], (TotalDur-.5), .5, volume-75)
		if RandomNum == 2:
			for x in range (TotalDur * 2 - 1):
				if x%4 == 2:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .75, volume)
					#Snare
				if x%4 == 0:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .75, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume)
			midi.addNote(track, channel, DrumTones["Ride"][0], (TotalDur-.5), .5, volume)
	return midi
#Function for generating midi Drums.
#midi{MIDIObject} returned.
