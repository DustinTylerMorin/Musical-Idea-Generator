## Program created for generating random chords
## Program created by Dustin Morin
##GPL-3.0-or-later

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
NotesAltSharp = ["A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#", "F#", "G", "G#"]
NotesAltFlat = ["A", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab"]

Scale = {
"Major": [0,2,2,1,2,2,2],
"Dorian": [0,2,1,2,2,2,1],
"Phrygian": [0,1,2,2,2,1,2],
"Lydian": [0,2,2,2,1,2,2],
"Mixolydian": [0,2,2,1,2,2,1],
"Minor": [0,2,1,2,2,1,2],
"Locrian": [0,1,2,2,1,2,2],
"Major Pentatonic": [0,2,2,3,2],
"Minor Pentatonic": [0,3,2,2,3],
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
"Whole Tone": [0,2,2,2,2,2],
"Chromatic": [0,1,1,1,1,1,1,1,1,1,1,1],
"Random": []
}

Modes = list(Scale.keys())

Tones = {
"Ab": [56],
"A" : [57],
"A#": [58],
"Bb": [58],
"B" : [59],
"Cb": [59],
"B#": [60],
"C" : [60],
"C#": [61],
"Db": [61],
"D" : [62],
"D#": [63],
"Eb": [63],
"E" : [64],
"Fb": [64],
"E#": [65],
"F" : [65],
"F#": [66],
"Gb": [66],
"G" : [67],
"G#": [68]
}
GenreList = {
	"Pop" : {
	"1" : ["Major",1,5,6,4],
	"2" : ["Major",5,6,4,1],
	"3" : ["Major",1,4,5],
	"4" : ["Major",1,6,4,5],
	"5" : ["Major",6,4,1,5],
	"6" : ["Major",1,4,6,5],
	"7" : ["Major",1,6,3,7],
	"8" : ["Major",2,5,1],
	"9" : ["Major",1,5,4]
	},

	"Rock" : {
	"1" : ["Major",1,5,6,4],
	"2" : ["Major",1,4,5],
	"3" : ["Major",4,6,1,5],
	"4" : ["Minor",1,4,7],
	"5" : ["Major",1,5,6,3,4,1,4,5],
	"6" : ["Major",2,4,5],
	"7" : ["Major",5,4,1],
	"8" : ["Major",2,1,5,7],
	"9" : ["Mixolydian",1,7],
	"10": ["Mixolydian",1,7,4,1],
	"11": ["Mixolydian",1,7,4,5,1],
	"12": ["Major",2,1,4,5],
	"13": ["Phrygian",1,3,5,4,6],
	"14": ["Lydian",1,6,2,3,6,2,1],
	"15": ["Harmonic Major",1,4,5],
	"16": ["Harmonic Major",1,2,4,5],
	"17": ["Harmonic Major",1,3,5,4]
	},

	"Blues" : {
	"1" : ["Major",1,1,1,1,4,4,1,1,5,4,1,5],
	"2" : ["Major",1,1,1,1,4,4,1,1,5,5,1,1],
	"3"	: ["Major",1,4,1,1,4,4,1,1,5,4,1,5],
	"4" : ["Major",1,1,1,1,4,4,1,1,5,4,1,4,1,5],
	"5" : ["Major",1,1,1,1,4,4,1,1,5,6,1,5]
	}
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
				if("#" in Tonic) and (("B" in Tonic) or ("E" in Tonic)):
					FS = "AltSharp"
				elif("b" in Tonic) and (("C" in Tonic) or ("F" in Tonic)):
					FS = "AltFlat"
				elif (("#" in Tonic) and ("B" not in Tonic)):
					FS = "Sharp"
				elif (("#" in Tonic) and ("E" not in Tonic)):
					FS = Sharp
				elif (("b" in Tonic) and ("C" not in Tonic)):
					FS = "Flat"
				elif (("b" in Tonic) and ("F" not in Tonic)):
					FS = "Flat"
				else:
					FS = 'Sharp'
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	print("\nWould you like the chords to be:\n \n1)Random Based On Scale \n2)Genre Based \n3)Manual Entry\n")
	while True:
		try:
			OpMode = int(input(">"))
			if OpMode == 3:
				Random = False
				(Mode) = ModeConfig(Tonic,FS)
				(UsedScale, Progression, Notes, Limit)=ScaleGen(Tonic, Mode, 7, FS, 4, "y", True)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(7, UsedScale, 4, Progression, Notes, Limit)
				(Chords, unused, GeneratedChords,MidiLengths)=Manual(UsedScale, Tonic, Mode, FS, ScaleChords,Notes,Random)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,MidiLengths)
				break
			elif OpMode == 2:
				Random = False
				(Mode,Number,StartTonic,Progression) = Genre(Tonic,FS)
				(ChordTones) = NumChordTones(Tonic,Mode,Number,FS)
				(UsedScale, Progression, Notes, Limit) = ScaleGen(Tonic,Mode,Number,FS,ChordTones,StartTonic,Random,Progression)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords)
				break
			elif OpMode ==1:
				Random = True
				(Mode) = ModeConfig(Tonic,FS)
				(Number) = NumChords(Tonic,Mode,FS)
				(ChordTones) = NumChordTones(Tonic,Mode,Number,FS)
				(StartTonic) = ProgressionStart(Tonic,Mode,Number,FS,ChordTones)
				(UsedScale, Progression, Notes, Limit) =ScaleGen(Tonic,Mode,Number,FS,ChordTones,StartTonic,Random)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords)
				break
			else:
				raise ValueError

		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()

def	ModeConfig(Tonic,FS):
	print ("\nChoose a scale/mode.\n\nType the number which corresponds to the desired key.\n")
	curlinelen=0
	curline=""
	for i in range(len(Modes)):
		if curlinelen < 25:
			curline = ((str(i+1)+") " + str(Modes[i])))
			curlinelen = len(curline)
			while curlinelen < 25:
				curline = curline+(" ")
				curlinelen += 1

		elif curlinelen == 25:
			curline = curline + ((str(i+1)+") " + str(Modes[i])))
			curlinelen = len(curline)
			while curlinelen < 50:
				curline = curline+(" ")
				curlinelen += 1
			print(curline)
			curline=("")
			curlinelen = 0
		if i == (len(Modes) - 1) and (curlinelen != 0):
			print(curline)
	print()

	while True:
		try:
			Mode = int(input(">"))
			if Mode in range(1,len(Modes)):
				Mode = Modes[Mode-1]
				break
			elif Mode == int(len(Modes)):
				Mode = Modes[random.randint(0,len(Modes)-2)]
				print ("\n",Mode)
				break
			else:
				raise ValueError
			NumChords(Tonic,Mode,FS)
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return (Mode)

def Genre(Tonic,FS):
	TempGenre = list(GenreList.keys())
	print ("\nChoose a Genre:\n")
	for i in range(len(TempGenre)):
		print((str(i+1)+") " + str(TempGenre[i])))
	print()
	while True:
		try:
			Genre=int(input(">"))
			if Genre in range(1,len(TempGenre)+1):
				Genre = Genre - 1
				TempGenreList = list(GenreList.keys())
				GenreValues = GenreList[TempGenreList[Genre]]
				TempInt = str(random.randint(1,len(GenreValues)))
				Progression = GenreValues[TempInt]
				Number = 0
				Mode = Progression[0]
				Number = (len(Progression)-1)
				StartTonic = Progression[1]
				Progression = Progression[1:]
				for i in range (len(Progression)):
					Progression[i] = int(Progression[i]-1)
				break

		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return (Mode,Number,StartTonic,Progression)

def Manual(UsedScale, Tonic, Mode, FS, ScaleChords,Notes,Random):
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Chords Avaliable:\n\n",ScaleChords,"\n")
	print ("Enter Chords 1 by 1 in this format:\n\nRoot,ChordTones,Midi Length(Currently Broken, Use any positive int),Modifier(s) as list\n\nEx)>"+Tonic+",3,4,sus2,add11\n\n"+Tonic+"sus2add11\n\nType 'r' to remove a chord, and 'q' to quit and lock in your progression.\n")
	Modifiers = ["sus2","sus4","6","9","11","13","add9","add11","add13", "m6", "none"]
	ChordInputList = []
	while True:
		ChordInput = (str(input(">")))
		try:
			if ChordInput.lower() == "q":
				break
			elif ChordInput.lower() == "r":
				del ChordInputList[-1]

			else:
				TempInput = ChordInput.split(",")
				ChordInput = list(([str(TempInput[0].capitalize()),int(TempInput[1]),int(TempInput[2]),(TempInput[3:])]))
				if (ChordInput[0].capitalize() in AllNotes) == False:
					raise ValueError
				if (ChordInput[1] in range(1,8)) == False:
					raise ValueError
				if (ChordInput[2] <= 0) == True:
					raise ValueError
				for i in range(0,len(ChordInput[3])):
					if (ChordInput[3][i].lower() in Modifiers) == True:
						ChordInput[3][i] = ChordInput[3][i].lower()
					else:
						raise ValueError
				ChordInputList.append(ChordInput)
			print(ChordInputList)
		except:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	while True:
		try:
			ChordsList = []
			Progression = []
			GenChordsList = []
			MidiLengths = []
			Progression.append(UsedScale.index((ChordInputList[0])[0]))
			ChordTones = ChordInputList[0][1]
			StartTonic = None
			(UsedScale, Progression, Notes, Limit) = ScaleGen(Tonic,Mode,7,FS,4,"y","n",Progression)

			for i in range(len(ChordInputList)):
				Progression = []
				Progression.append(UsedScale.index((ChordInputList[i])[0]))
				Modifier = list(ChordInputList[i][3])
				ChordTones = ChordInputList[i][1]
				Limit = 1
				MidiLengths.append(ChordInputList[i][2])
				(Chords,unused,GeneratedChords)=ChordGenPrep(1, UsedScale, ChordTones, Progression, Notes, Limit, Modifier)
				ChordsList.append(str(Chords[0]))
				GenChordsList.append(GeneratedChords[0])
				if i == (len(ChordInputList)):
					break
			break
		except:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
			Manual(UsedScale, Tonic, Mode, FS, ScaleChords,Notes,Random)

	#ChordsList = ChordsList[0]
	return(ChordsList, unused, GenChordsList, MidiLengths)

def NumChords(Tonic,Mode,FS):
	print("\nHow many chord(s) would you like to generate?\n")
	while True:
		try:
			Number = int(input(">"))
			if Number > 0:
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(Number)
def NumChordTones(Tonic,Mode,Number,FS):
	print("\nHow many chord tones per chord? would you like to generate? (1,2,3,4)\n")
	while True:
		try:
			ChordTones = int(input(">"))
			if ChordTones in range (1,5):
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(ChordTones)
def ProgressionStart(Tonic, Mode, Number, FS, ChordTones):
	print("\nWould you like the progression to start on the tonic? (y/n)\n")
	while True:
		try:
			StartTonic = str(input(">")).lower()
			if StartTonic == "y" or StartTonic == "n":
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(StartTonic)

def ScaleGen(Tonic, Mode, Number, FS, ChordTones, StartTonic, Random, Progression=None):
	RandomNumbers = []
	ScaleNotes = []
	UsedScale = []
	if FS == "Sharp":
		Notes = NotesSharp
	elif FS == "Flat":
		Notes = NotesFlat
	elif FS == "AltFlat":
		Notes = NotesAltFlat
	elif FS == "AltSharp":
		Notes = NotesAltSharp
	else:
		raise ValueError

	Index = Notes.index(Tonic)
	Limit = len(Scale.get(Mode))
	if Random == True:
		for i in range(Number):
			RandomNumbers.append(random.randint(0,Limit-1))
		if StartTonic == 'y':
			RandomNumbers[0] = 0
		if StartTonic == 'n':
			RandomNumbers[0] = random.randint(1,Limit-1)
		for z in range(0,Limit):
			ScaleNotes.append((Scale[Mode])[z])
		Progression = RandomNumbers
	else:
		for z in range(0,Limit):
			ScaleNotes.append((Scale[Mode])[z])
	for x in range (0,Limit):
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
	return(UsedScale, Progression, Notes, Limit)

def ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit, Modifier = "none"):
	ScaleChordsGen = []
	GeneratedChords = []
	GeneratedRoots = []
	for y in range (Number):
		GeneratedRoots.append(UsedScale[Progression[y]])
	while len(GeneratedChords) != len(GeneratedRoots):
		for i in range(len(GeneratedRoots)):
			Temp = UsedScale.index(GeneratedRoots[i])
			GeneratedChords.insert(i,[GeneratedRoots[i]])
			(GeneratedChords)=ChordGen(i, Temp, GeneratedChords, UsedScale, ChordTones, Modifier)
	for z in range(Limit):
		Temp = z
		ScaleChordsGen.insert(z,[UsedScale[z]])
		(ScaleChords)=ChordGen(z, Temp, ScaleChordsGen, UsedScale, ChordTones, Modifier)
	Chords = ChordName(GeneratedChords, Notes, Modifier)
	ScaleChords = ChordName(ScaleChordsGen, Notes, Modifier)
	return (Chords, ScaleChords, GeneratedChords)


def ChordGen(i, Temp, GeneratedChords, UsedScale, ChordTones, Modifier):
	Scale=[]
	ScaleLen = len(UsedScale)
	for x in range(len(UsedScale)):
		try:
			Scale.append(UsedScale[Temp])
			Temp += 1
		except:
			Temp = 0
			Scale.append(UsedScale[Temp])
			Temp += 1
	Temp = 0
	while len(GeneratedChords[i]) != ChordTones:
		try:
			ScaleLen = len(UsedScale)
			Temp = Temp + 2
			if Temp >= ScaleLen:
				Temp = Temp - ScaleLen
				GeneratedChords[i].append(Scale[Temp])
			else:
				GeneratedChords[i].append(Scale[Temp])


		except ValueError as error:
			print("\nSomething has went wrong\n")
			if Debug == True:
				traceback.print_exc()
	Temp = 0
	GeneratedChords=Modify(i, GeneratedChords, Scale, ChordTones, Modifier,ScaleLen)
	return(GeneratedChords)

def Modify(i, GeneratedChords, UsedScale, ChordTones, Modifier, ScaleLen):
	Modifier = str(Modifier[0:])
	if ("sus2" in Modifier) and (len(GeneratedChords[i]) >= 2):
		GeneratedChords[i][1] = (UsedScale[1])

	if ("sus4" in Modifier) and (len(GeneratedChords[i]) >= 2):
		GeneratedChords[i][1] = (UsedScale[3])

	if ("6" in Modifier) and (len(GeneratedChords[i]) >= 4):
		GeneratedChords[i][3] = (UsedScale[5])

	if ("9" in Modifier):
		if (len(GeneratedChords[i]) == 4):
			GeneratedChords[i][3] = (UsedScale[1])
		if (len(GeneratedChords[i]) == 5):
			GeneratedChords[i][2] = (UsedScale[1])

	if ("11" in Modifier):
		if (len(GeneratedChords[i]) == 4):
			GeneratedChords[i][3] = (UsedScale[3])
		if (len(GeneratedChords[i]) == 5):
			GeneratedChords[i][4] = (UsedScale[3])
		if (len(GeneratedChords[i]) == 6):
			GeneratedChords[i][5] = (UsedScale[3])

	if ("13" in Modifier):
		if (len(GeneratedChords[i]) == 4):
			GeneratedChords[i][3] = (UsedScale[5])
		if (len(GeneratedChords[i]) == 5):
			GeneratedChords[i][4] = (UsedScale[5])
		if (len(GeneratedChords[i]) == 6):
			GeneratedChords[i][5] = (UsedScale[5])
		if (len(GeneratedChords[i]) == 7):
			GeneratedChords[i][6] = (UsedScale[5])

	return(GeneratedChords)

def ChordName(GeneratedChords, Notes, Modifier):
	Chords = []
	try:
		for i in range(len(GeneratedChords)):
			name = []
			Index = GeneratedChords[i]
			if len(GeneratedChords[i]) >= 1:
				Root=GeneratedChords[i][0]
				name.append(Root)

			if len(GeneratedChords[i]) >= 2:
				Second=GeneratedChords[i][1]
				Third=GeneratedChords[i][1]
				Fourth=GeneratedChords[i][1]
				if (Notes.index(Root) < Notes.index(Third)):
					if Notes.index(Third) - Notes.index(Root) == 4:
						name[0]=(name[0]+"Maj")
					elif Notes.index(Third) - Notes.index(Root) == 3:
						name[0]=(name[0]+"m")
					elif Notes.index(Second) - Notes.index(Root) == 2:
						name[0]=(name[0]+"sus2")
					elif Notes.index(Fourth) - Notes.index(Root) == 5:
						name[0]=(name[0]+"sus4")

				else:
					if Notes.index(Third) + 12 - Notes.index(Root) == 4:
						name[0]=(name[0]+"Maj")
					elif Notes.index(Third) + 12 - Notes.index(Root) == 3:
						name[0]=(name[0]+"m")
					elif Notes.index(Second)+ 12 - Notes.index(Root) == 2:
							name[0]=(name[0]+"sus2")
					elif Notes.index(Fourth)+ 12 - Notes.index(Root) == 5:
						name[0]=(name[0]+"sus4")



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
					elif Notes.index(Fifth) +12 - Notes.index(Root) == 6:
						name[0]=(name[0]+"b5")
					elif Notes.index(Fifth) + 12 - Notes.index(Root) == 8:
						name[0]=(name[0]+"#5")

			if len(GeneratedChords[i]) >= 4:
				Sixth=GeneratedChords[i][3]
				Seventh=GeneratedChords[i][3]
				if (Notes.index(Root) < Notes.index(Seventh)):
					if Notes.index(Seventh) - Notes.index(Root) == 11:
						name[0]=(name[0]+"7")
					elif Notes.index(Seventh) - Notes.index(Root) == 10:
						name[0]=(name[0]+"b7")
					elif Notes.index(Sixth) - Notes.index(Root) == 9:
						name[0]=(name[0]+"6")
					elif Notes.index(Sixth) - Notes.index(Root) == 8:
						name[0]=(name[0]+"6")

				else:
					if Notes.index(Seventh) + 12 - Notes.index(Root) == 11:
						name[0]=(name[0]+"7")
					elif Notes.index(Seventh) +12  - Notes.index(Root) == 10:
						name[0]=(name[0]+"b7")
					elif Notes.index(Sixth) +12  - Notes.index(Root) == 9:
						name[0]=(name[0]+"6")
					elif Notes.index(Sixth)+12 - Notes.index(Root) == 8:
						name[0]=(name[0]+"6")

			if len(GeneratedChords[i]) >= 4:
				for x in range(3,len(GeneratedChords[i])):
					Ninth=GeneratedChords[i][x]
					if (Notes.index(Ninth)+12 - Notes.index(Root) == 2) or (Notes.index(Ninth) - Notes.index(Root) == 2):
						break
				if (Notes.index(Root) < Notes.index(Ninth)):
					if (("Majb7" in name[0]) and (Notes.index(Ninth) - Notes.index(Root) == 2)):
						name[0]=(name[0]+"9")
					elif ("sus2" not in name[0]) and Notes.index(Ninth) - Notes.index(Root) == 2:
						name[0]=(name[0]+"add9")
				else:
					if (("Majb7" in name[0]) and (Notes.index(Ninth)+12 - Notes.index(Root) == 2)):
						name[0]=(name[0]+"9")
					elif ("sus2" not in name[0]) and Notes.index(Ninth)+12 - Notes.index(Root) == 2:
						name[0]=(name[0]+"add9")

			if len(GeneratedChords[i]) >= 4 :
				for x in range(3,len(GeneratedChords[i])):
					Eleventh=GeneratedChords[i][x]
					if (Notes.index(Eleventh)+12 - Notes.index(Root) == 5) or (Notes.index(Eleventh) - Notes.index(Root) == 5):
						break
				if (Notes.index(Root) < Notes.index(Eleventh)):
					if (("Majb7" in name[0]) and (Notes.index(Eleventh) - Notes.index(Root) == 5)):
						name[0]=(name[0]+"11")
					elif ("sus4" not in name[0]) and Notes.index(Eleventh) - Notes.index(Root) == 5:
						name[0]=(name[0]+"add11")
				else:
					if (("Majb7" in name[0]) and (Notes.index(Eleventh)+12 - Notes.index(Root) == 5)):
						name[0]=(name[0]+"11")
					elif ("sus4" not in name[0]) and Notes.index(Eleventh) + 12 - Notes.index(Root) == 5:
						name[0]=(name[0]+"add11")

			if len(GeneratedChords[i]) >=4 :
				for x in range(3,len(GeneratedChords[i])):
					Thirteenth=GeneratedChords[i][x]
					if (Notes.index(Thirteenth)+12 - Notes.index(Root) == 9) or (Notes.index(Thirteenth) - Notes.index(Root) == 9):
						break
				if (Notes.index(Root) < Notes.index(Thirteenth)):
					if (("Majb7" in name[0]) and Notes.index(Thirteenth) - Notes.index(Root) == 9):
						name[0]=(name[0]+"13")
					elif ("6" not in name[0]) and Notes.index(Thirteenth) - Notes.index(Root) == 9:
						name[0]=(name[0]+"add13")
				else:
					if (("Majb7" in name[0]) and Notes.index(Thirteenth)+12 - Notes.index(Root) == 9):
						name[0]=(name[0]+"13")
					elif ("6" not in name[0]) and Notes.index(Thirteenth)+12 - Notes.index(Root) == 9:
						name[0]=(name[0]+"add13")

			name = str(name[0])
			if "m7" in name:
				name = name.replace("m7","mMaj7")
			if "mb5bb7" in name:
				name = name.replace("mb5bb7","dim7")
			if "Maj#57" in name:
				name = name.replace("Maj#57","Maj7#5")
			if "Maj#5" in name:
				name = name.replace("Maj#5","aug")
			if "b56add13" in name and "add13" not in Modifier:
				name = name.replace("b56add13","dim7")
			if "b56add13" in name and "6" in Modifier:
				name = name.replace("b56add13","dim6")
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
			if "sus2sus4" in name:
				name = name.replace("sus2sus4","")
			if "sus26" in name:
				name = name.replace("sus26","6sus2")
			if "Maj6" in name:
				name = name.replace("Maj6","6")
			if "add9add11add13" in name:
				name = name.replace("add9add11add13","add13")
			if "add9add11" in name:
				name = name.replace("add9add11","add11")
			if "add9add13" in name:
				name = name.replace("add9add13","add13")
			if "791113" in name:
				name = name.replace("791113","13")
			if "7911" in name:
				name = name.replace("7911","11")
			if "79" in name:
				name = name.replace("79","9")
			if "6add13" in name:
				name = name.replace("6add13","add13")
			if "913" in name:
				name = name.replace("913","9/13")
			if "713" in name:
				name = name.replace("713","7/13")
			if "sus47" in name:
				name = name.replace("sus47","Maj7sus4")
			Chords.append(name)
	except:
		if Debug == True:
			traceback.print_exc()
	return(Chords)

def Output(Tonic, Mode, UsedScale, ScaleChords, Chords):
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Scale Chords:\n\n",ScaleChords,"\n\n")
	print ("Chord(s) produced:\n\n",Chords)

def export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,MidiLengths = []):
	ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords)
	ExportMidi(GeneratedChords,MidiLengths)

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
						traceback.print_exc()
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
		except ValueError as error:
			print("\nSomething has went wrong\n")
			if Debug == True:
				traceback.print_exc()

def ExportMidi(GeneratedChords, MidiLengths):
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
					except ValueError as error:
						print("\nTry again!\n")
						if Debug == True:
							traceback.print_exc()
				Dur = []
				if len(MidiLengths) == 0:
					print("\nWould you like beats to be random or fixed?(r/f)\n")
					while True:
						try:
							RanDur = str(input(">")).lower()
							if RanDur == "f" or RanDur == "r":
								print ("\nHow many beats would you like each chord to last?\n")
								break
							else:
								raise ValueError
						except ValueError as error:
							print("\nTry again!\n")
							if Debug == True:
								traceback.print_exc()
				else:
					RanDur = "Manual"
					for i in range(len(MidiLengths)):
						Dur.append(MidiLengths[i])
				while True:
					if RanDur == "f":
						try:
							inputDur = int(input(">"))
							for i in range(len(GeneratedChords)):
								Dur.append(inputDur)
							break
						except ValueError as error:
							print("\nTry again!\n")
							if Debug == True:
								traceback.print_exc()
					elif RanDur == "r":
						Durations = [1,2,4]
						for i in range(len(GeneratedChords)):
							Dur.append(Durations[random.randint(0,2)])
						break
					elif RanDur == "Manual":
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
	for x in range (TotalDur * 2 - 1):
		if x%4 == 2:
			midi.addNote(track, channel, 38, x/2, .5, volume)
		if x%4 == 0:
			midi.addNote(track, channel, 36, x/2, .5, volume)
		if x%16 == 0:
			midi.addNote(track, channel, 49, x/2, 1, volume-25)
		midi.addNote(track, channel, 42, x/2, 1, volume-25)
	return midi
if (__name__ == "__main__"):
	main()
