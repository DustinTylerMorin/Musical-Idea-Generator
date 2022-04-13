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
def DrumsGen(midi, track, bpm, Dur, Genre, TimeSig):
	trackname = "Drums"
	channel = track
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	volume = 100
	if Genre == None:
		Genre = Drums[1]

	TotalDur = 0
	CurAccents = Accents.get(TimeSig)
	KickAcc = CurAccents[1:CurAccents.index("Snare")]
	SnareAcc = CurAccents[CurAccents.index("Snare")+1:]
	Top = int(TimeSig.split('/')[0])
	Bottom = int(TimeSig.split('/')[1])
	print (KickAcc,SnareAcc)
	if Genre == "Pop":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], (x/2-.25), .5, volume-25)
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], (x/2-.25), .5, volume-25)
					midi.addNote(track, channel,DrumTones["Hand Clap"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)

	elif Genre == "Rock":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,2)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top  in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-75)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-75)
		if RandomNum == 2:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume)

	if Genre == "Metal":
		RandomNum = random.randint(0,0)
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .5, .5, volume)
					#Kick
				midi.addNote(track, channel, DrumTones["Crash"][0], x/2, .5, volume-25)

	if Genre == "Blues":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum  = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 2, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 2, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)

	if Genre == "Country":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2+.25, .25, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2-.25, .5, volume-25)
					midi.addNote(track, channel,DrumTones["Rim"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-25)
	if Genre == "Punk":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,1)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["OpenHat"][0], (x/2), .5, volume-25)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					#midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2-.25, .25, volume-25)
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-25)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-25)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .5 , .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				if x%2 == 1:
					midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-25)
	elif Genre == "Stoner Rock":
		for i in range (len(Dur)):
			TotalDur += Dur[i]
		RandomNum = random.randint(0,2)
		if RandomNum == 0:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["OpenHat"][0], x/2, .5, volume-75)
		if RandomNum == 1:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .75, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["ClosedHat"][0], x/2, .5, volume-75)
		if RandomNum == 2:
			for x in range (TotalDur * 2):
				if (x)%Top in SnareAcc:
					midi.addNote(track, channel,DrumTones["Snare"][0], x/2, .5, volume)
					#Snare
				if (x)%Top in KickAcc:
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2, .5, volume)
					midi.addNote(track, channel, DrumTones["Kick"][0], x/2 + .25, .5, volume)
					#Kick
				if x == 0:
					midi.addNote(track, channel, DrumTones["Crash"][0], x/2, 1, volume-25)
					#Crash
				midi.addNote(track, channel, DrumTones["Ride"][0], x/2, .5, volume)
	return midi
#Function for generating midi Drums.
#midi{MIDIObject} returned.
