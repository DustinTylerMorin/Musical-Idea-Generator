## Program created for generating random chords
## Program created by Dustin Morin

import random
import platform
import os
from datetime import datetime
from midiutil.MidiFile import MIDIFile
import traceback

#Configuration
Debug = False
Piano = True
Guitar = True
Bass = True
Drums = True
#Configuration

AllNotes = ["Ab", "A", "A#", "Bb", "B", 'B#', "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
NotesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NotesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
NotesAlt = ["A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#", "F#", "G", "G#"]

Scale = {
"Major": [0,2,2,1,2,2,2],
"Dorian": [0,2,1,2,2,2,1],
"Phrygian": [0,1,2,2,2,1,2],
"Lydian": [0,2,2,2,1,2,2],
"Mixolydian": [0,2,2,1,2,2,1],
"Minor": [0,2,1,2,2,1,2],
"Locrian": [0,1,2,2,1,2,2,2],
"Harmonic Major": [0,2,2,1,2,1,3],
"Dorian b5": [0,2,1,2,1,3,1],
"Phrygian b4": [0,1,2,1,3,1,2],
"Lydian b3": [0,2,1,3,1,2,2],
"Mixolydian b2": [0,1,3,1,2,2,1],
"Lydian Augmented #2": [0,3,1,2,2,1,2],
"Locrian bb7": [0,1,2,2,1,2,1],
"Harmonic Minor": [0,2,1,2,2,1,3],
"Locrian 6": [0,1,2,2,1,3,1],
"Ionian #5": [0,2,2,1,3,1,2],
"Dorian #4": [0,2,1,3,1,2,1],
"Phrygian Dominant": [0,1,3,1,2,1,2],
"Lydian #2": [0,3,1,2,1,2,2],
"Super Locrian bb7": [0,1,2,1,2,2,1],
"Melodic Minor": [0,2,1,2,2,2,2],
"Dorian b2": [0,1,2,2,2,2,1],
"Lydian Augmented": [0,2,2,2,2,1,2],
"Lydian Dominant": [0,2,2,2,1,2,1],
"Mixolydian b6": [0,2,2,1,2,1,2],
"Locrian #2": [0,2,1,2,1,2,2],
"Super Locrian": [0,1,2,1,2,2,2],
"Random": []
}

Modes = list(Scale.keys())

Tones = {
"Ab": [56],
"A" : [57],
"A#": [58],
"Bb": [58],
"B" : [59],
"C" : [60],
"C#": [61],
"Db": [61],
"D" : [62],
"D#": [63],
"Eb": [63],
"E" : [64],
"F" : [65],
"F#": [66],
"Gb": [66],
"G" : [67],
"G#": [68]
}
def main():
	print ("\nProgram created by Dustin Morin for the purposes of generating chord(s) or single notes in a desired key.\n")
	print ("What's the tonic of the desired key?\n\nEx(C, Gb, A#, Random)\n")
	while True:
		try:
			Tonic = str(input(">")).capitalize()
			if Tonic == "Random":
				Rand = random.randint(0,20)
				Tonic = str(AllNotes[Rand])
				print ("\n", Tonic)
			if Tonic in AllNotes:
				if ("#" in Tonic) and (("B" not in Tonic) or ("E" not in Tonic)):
					FS = "Sharp"
				elif "b" in Tonic:
					FS = "Flat"
				elif("#" in Tonic) and (("B" in Tonic) or ("E" in Tonic)):
					FS = "Alt"
				else:
					FS = "Sharp"
				break
			else:
				print("\nTry again!\n")
				pass
		except:
			print("\nTry again!\n")
			pass

	curlinelen=0
	curline=""
	print ("\nChoose a scale/mode.\n\nType the number which corresponds to the desired key.\n")
	for i in range(len(Modes)):
		if curlinelen < 25:
			curline = ((str(i+1)+") " + str(Modes[i])))
			curlinelen = len(curline)
			#buff to 25
			while curlinelen < 25:
				curline = curline+(" ")
				curlinelen += 1

		elif curlinelen == 25:
			curline = curline + ((str(i+1)+") " + str(Modes[i])))
			curlinelen = len(curline)
			#buff to 50
			while curlinelen < 50:
				curline = curline+(" ")
				curlinelen += 1
			print(curline)
			curline=("")
			curlinelen = 0
		if i == (len(Modes) - 1) and (curlinelen != 0):
			print(curline)
	print()

	##print(str(len(Modes)+1)+")","Random")
	while True:
		try:
			Mode = int(input(">"))
			if Mode in range(1,len(Modes)):
				Mode = Modes[Mode-1]
				break
			elif Mode == int(len(Modes)):
				Mode = Modes[random.randint(0,len(Modes))]
				print ("\n",Mode)
				break
			else:
				raise ValueError
		except:
			print("\nTry again!\n")
			pass
	print("\nHow many chord(s) would you like to generate?\n")
	while True:
		try:
			Number = int(input(">"))
			if Number > 0:
				break
			else:
				raise ValueError
		except:
			print("\nTry again!\n")
			pass
	print("\nHow many chord tones per chord? would you like to generate? (1,2,3,4)\n")
	while True:
		try:
			ChordTones = int(input(">"))
			if ChordTones in range (1,5):
				break
			else:
				raise ValueError
		except:
			print("\nTry again!\n")
			pass
	print("\nWould you like the progression to start on the tonic? (y/n)\n")
	while True:
		try:
			StartTonic = str(input(">")).lower()
			if StartTonic == "y" or StartTonic == "n":
				break
			else:
				raise ValueError
		except:
			print("\nTry again!\n")
			pass
	ScaleGen(Tonic, Mode, Number, FS, ChordTones, StartTonic)


def ScaleGen(Tonic, Mode, Number, FS, ChordTones, StartTonic):
	RandomNumbers = []
	ScaleNotes = []
	UsedScale = []
	GeneratedChords = []
	GeneratedRoots = []
	ScaleChordsGen = []
	if FS == "Sharp":
		Notes = NotesSharp
	elif FS == "Flat":
		Notes = NotesFlat
	else:
		Notes = NotesAlt

	Index = Notes.index(Tonic)

	for i in range(Number):
		RandomNumbers.append(random.randint(0,6))
	if StartTonic == 'y':
		RandomNumbers[0] = 0
	if StartTonic == 'n':
		RandomNumbers[0] = random.randint(1,6)
	for z in range(0,7):
		ScaleNotes.append((Scale[Mode])[z])

	for x in range (0,7):
		while True:
			Index = Index + ScaleNotes[x]
			try:
				UsedScale.append(Notes[Index])
				break
			except:
				if Index >= len(Notes)-1:
					Index = Index - len(Notes)
					UsedScale.append(Notes[Index])
					break
	for y in range (len(RandomNumbers)):
		GeneratedRoots.append(UsedScale[RandomNumbers[y]])
	while len(GeneratedChords) != len(GeneratedRoots):
		for i in range(len(GeneratedRoots)):
			Temp = UsedScale.index(GeneratedRoots[i])
			GeneratedChords.insert(i,[GeneratedRoots[i]])
			ChordGen(i, Temp, GeneratedChords, UsedScale, ChordTones)
	for z in range(7):
		Temp = z
		ScaleChordsGen.insert(z,[UsedScale[z]])
		ChordGen(z, Temp, ScaleChordsGen, UsedScale, ChordTones)

	Chords = ChordName(GeneratedChords, Notes)
	ScaleChords = ChordName(ScaleChordsGen, Notes)
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Scale Chords:\n\n",ScaleChords,"\n\n")
	#print ("Chord Notes\n\n",GeneratedChords)
	print ("Chord(s) produced:\n\n",Chords)

	ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords)
	ExportMidi(GeneratedChords)

def ChordGen(i, Temp, GenChords, UsedScale, ChordTones):
	while len(GenChords[i]) != ChordTones:
		try:
			Temp = Temp + 2
			if Temp >= len(UsedScale):
				Temp = Temp - len(UsedScale)
				GenChords[i].append(UsedScale[Temp])
			else:
				GenChords[i].append(UsedScale[Temp])
		except Exception as e:
			print(e)
			print("\nSomething has went wrong\n")

def ChordName(GeneratedChords, Notes):
	Chords = []
	for i in range(len(GeneratedChords)):
		name = []
		Index = GeneratedChords[i]
		if len(GeneratedChords[i]) >= 1:
			Root=GeneratedChords[i][0]
			name.append(Root)

		if len(GeneratedChords[i]) >= 2:
			Third=GeneratedChords[i][1]
			if (Notes.index(Root) < Notes.index(Third)):
				if Notes.index(Third) - Notes.index(Root) == 4:
					name[0]=(name[0]+"Maj")
				elif Notes.index(Third) - Notes.index(Root) == 3:
					name[0]=(name[0]+"m")
			else:
				if Notes.index(Third) + 12 - Notes.index(Root) == 4:
					name[0]=(name[0]+"Maj")
				elif Notes.index(Third) +12  - Notes.index(Root) == 3:
					name[0]=(name[0]+"m")


		if len(GeneratedChords[i]) >= 3:
			Fifth=GeneratedChords[i][2]
			if (Notes.index(Root) < Notes.index(Fifth)):
				if Notes.index(Fifth) - Notes.index(Root) == 7:
					pass
				elif Notes.index(Fifth) - Notes.index(Root) == 6:
					name[0]=(name[0]+"b5")
				elif Notes.index(Fifth) - Notes.index(Root) == 8:
					name[0]=(name[0]+"#5")

			else:
				if Notes.index(Fifth) + 12 - Notes.index(Root) == 7:
					pass
				elif Notes.index(Fifth) +12  - Notes.index(Root) == 6:
					name[0]=(name[0]+"b5")
				elif Notes.index(Fifth) +12  - Notes.index(Root) == 8:
					name[0]=(name[0]+"#5")

		if len(GeneratedChords[i]) == 4:
			Seventh=GeneratedChords[i][3]
			if (Notes.index(Root) < Notes.index(Seventh)):
				if Notes.index(Seventh) - Notes.index(Root) == 11:
					name[0]=(name[0]+"7")
				elif Notes.index(Seventh) - Notes.index(Root) == 10:
					name[0]=(name[0]+"b7")
				elif Notes.index(Seventh) - Notes.index(Root) == 9:
					name[0]=(name[0]+"bb7")
			else:
				if Notes.index(Seventh) + 12 - Notes.index(Root) == 11:
					name[0]=(name[0]+"7")
				elif Notes.index(Seventh) +12  - Notes.index(Root) == 10:
					name[0]=(name[0]+"b7")
				elif Notes.index(Seventh) +12  - Notes.index(Root) == 9:
					name[0]=(name[0]+"bb7")
		name = str(name[0])
		if "m7" in name:
			name = name.replace("m7","mMaj7")
		if "mb5bb7" in name:
			name = name.replace("mb5bb7","dim7")
		if "Maj#57" in name:
			name = name.replace("Maj#57","Maj7#5")
		if "mb5b7" in name:
			name = name.replace("mb5b7","m7b5")
		if "mb5" in name:
			name = name.replace("mb5","dim")
		if "mb" in name:
			name = name.replace("mb","m")
		if "Majb7" in name:
			name = name.replace("Majb7","7")
		if "dimb7" in name:
			name = name.replace("dimb7","dim7")
		Chords.append(name)
	return(Chords)

def ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords):
	print("\nWould you like to output these chords to a .txt file? (y/n)\n")
	while True:
		try:
			export = str(input(">")).lower()
			if export == "y":
				cwd = os.getcwd()
				try:
					os.mkdir("Music")
				except OSError as error:
					if Debug == True:
						print(error)
					else:
						pass
				if platform.system() == ("Linux" or "MacOS") :
					now = str(cwd)+'/Music'+'/'+'chords_'+datetime.now().strftime("%H-%M-%S")+'.txt'
				else:
					now = str(cwd)+'\\Music'+"\\"+"chords_"+datetime.now().strftime("%H-%M-%S")+'.txt'
				with open(now, 'w') as file:
					file.write("Scale Used:\n\n")
					file.write("%s %s" % (Tonic,Mode) +"\n\n")
					file.write("%s" % UsedScale)
					file.write("\n\nScale Chords:\n\n")
					file.write("%s" % ScaleChords)
					file.write('\n\nChord(s) produced:\n\n')
					for i in range(len(Chords)):
						file.write(str(i+1)+") ")
						file.write("%s %s" % (Chords[i],GeneratedChords[i]) + "\n")
					file.write('\n')
					file.close()
					if platform.system() == ("Linux" or "MacOS") :
						print ("\nFile output to:"+now)
					else:
						print ("\nFile output to:"+now)

				break
			elif export == "n":
				break
			else:
				print("\nTry again!\n")
		except Exception as e:
			print(e)
			print("\nSomething has went wrong\n")

def ExportMidi(GeneratedChords):
	print("\nWould you like to output these chords to a .mid file? (y/n)\n")
	while True:
		try:
			export = str(input(">")).lower()
			if export == "y":
				print("\nWhat BPM would you like for your .mid file?\n")
				while True:
					try:
						bpm = int(input(">"))
						break
					except:
						print("\nTry again!\n")
						pass
				print("\nWould you like beats to be random or fixed?(r/f)\n")
				while True:
					try:
						RanDur = str(input(">")).lower()
						if RanDur == "f" or RanDur == "r":
							Dur = []
							break
						else:
							raise ValueError
					except:
						print("\nTry again!\n")
						pass
				print ("\nHow many beats would you like each chord to last?\n")
				while True:
					if RanDur == "f":
						try:
							inputDur = int(input(">"))
							for i in range(len(GeneratedChords)):
								Dur.append(inputDur)
							break
						except:
							print("\nTry again!\n")
							pass
					elif RanDur == "r":
						Durations = [1,2,4]
						for i in range(len(GeneratedChords)):
							Dur.append(Durations[random.randint(0,2)])
						break
					else:
						print("\nSomething has went wrong\n")
				cwd = os.getcwd()
				try:
					os.mkdir("Music")
				except OSError as error:
					if Debug == True:
						print(error)
					else:
						pass
				if platform.system() == ("Linux" or "MacOS") :
					now = str(cwd)+'/Music'+'/'+'chords_'+datetime.now().strftime("%H-%M-%S")+'.mid'
				else:
					now = str(cwd)+'\\Music'+"\\"+"chords_"+datetime.now().strftime("%H-%M-%S")+'.mid'
				numtracks = 0
				if Piano == True:
					numtracks += 1
				if Guitar == True:
					numtracks += 1
				if Bass == True:
					numtracks += 1
				if Drums == True:
					numtracks += 1
				midi = MIDIFile(numtracks)
				track = 0
				if Piano == True:
					midi = PianoGen(midi, track, bpm, Dur, GeneratedChords)
					track += 1
				if Guitar == True:
					midi =	GuitarGen(midi, track, bpm, Dur, GeneratedChords)
					track += 1
				if Bass == True:
					midi = BassGen(midi, track, bpm, Dur, GeneratedChords)
					track += 1
				if Drums == True:
					midi = DrumsGen(midi, track, bpm, Dur, GeneratedChords)
					track += 1
				with open(now, 'wb') as file:
					midi.writeFile(file)
					file.close()
				if platform.system() == ("Linux" or "MacOS") :
					print ("\nFile output to:"+now)
				else:
					print ("\nFile output to:"+now)
				break
			elif export == "n":
				print()
				break
			else:
				print("\nTry again!\n")
		except Exception as e:
			print(e)
			print("\nSomething has went wrong\n")
			traceback.print_exc()
def PianoGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Piano"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 0
	volume = 100
	for i in range(len(GeneratedChords)):
		pitch = Tones[GeneratedChords[i][0]][0]
		for x in range(0,len(GeneratedChords[i])):
			if Tones[GeneratedChords[i][x]][0] < pitch:
				pitch = (Tones[GeneratedChords[i][x]][0]) + 12
			elif Tones[GeneratedChords[i][x]][0] >= pitch:
				pitch =	Tones[GeneratedChords[i][x]][0]
			else:
				print ("Something went terribly wrong")
			midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
	return midi
		# write it to disk
def GuitarGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Guitar"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 1
	volume = 100
	for i in range(len(GeneratedChords)):
		pitch = Tones[GeneratedChords[i][0]][0]
		for x in range(0,len(GeneratedChords[i])):
			if Tones[GeneratedChords[i][x]][0] < pitch:
				pitch = (Tones[GeneratedChords[i][x]][0]) + 12
			elif Tones[GeneratedChords[i][x]][0] >= pitch:
				pitch =	Tones[GeneratedChords[i][x]][0]
			else:
				print ("Something went terribly wrong")
			midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
	return midi
		# write it to disk
def BassGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Bass"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 2
	volume = 100
	for i in range(len(GeneratedChords)):
		pitch = Tones[GeneratedChords[i][0]][0]
		if Tones[GeneratedChords[i][0]][0] < pitch:
			pitch = (Tones[GeneratedChords[i][0]][0]) - 12
		elif Tones[GeneratedChords[i][0]][0] >= pitch:
			pitch =	Tones[GeneratedChords[i][0]][0]
		else:
			print ("Something went terribly wrong")
		midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
	return midi
def DrumsGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Drums"
	channel = 3
	time = 0
	volume = 100
	DrumTones = {
	"Kick": [36],
	"Snare": [38],
	"Hat": [42],
	"Crash": [49],
	"Ride": [51],
	"Floor": [43],
	"Rack": [48],
	"Crash2": [57]
	}
	TotalDur = 0
	for i in range (len(Dur)):
		TotalDur += Dur[i]
	for x in range (TotalDur):
		if x%4 == 2:
			midi.addNote(track, channel, 38, x, 1, volume)
		if x%4 == 0:
			midi.addNote(track, channel, 36, x, 1, volume)
		if x%16 == 0:
			midi.addNote(track, channel, 49, x, 1, volume-25)
		midi.addNote(track, channel, 42, x, 1, volume-25)
	return midi
if (__name__ == "__main__"):
	main()
