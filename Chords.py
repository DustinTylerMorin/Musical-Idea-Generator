## Program created for generating random chords
## Program created by Dustin Morin
import random
AllNotes = ["Ab", "A", "A#", "Bb", "B", 'B#', "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
NotesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NotesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
Modes = ["Major", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Minor", "Locrian", "Harmonic Major", "Dorian b5", "Phrygian b4", "Lydian b3", "Mixolydian b2", "Lydian Augmented #2", "Locrian bb7", "Harmonic Minor", "Locrian 6", "Ionian #5", "Dorian #4", "Phrygian Dominant", "Lydian #2", "Super Locrian bb7"]
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
"Super Locrian bb7": [0,1,2,1,2,2,1]
}
def main():
	print ("\nProgram created by Dustin Morin for the purposes of generating chords in a desired key.\n")
	while True:
		try:
			Tonic = str(input("What's the tonic of the desired key?\nEx(C, Gb, A#)\n\n>")).capitalize()
			if Tonic in AllNotes:
				if "#" in Tonic:
					FS = "Sharp"
				elif "b" in Tonic:
					FS = "Flat"
				else:
					FS = "Sharp"
				break
			else:
				print("\nTry again!\n")
				pass
		except:
			print("\nTry again!\n")
			pass

	while True:
		try:
			print ("Choose a scale/mode.\nType the number which corresponds to the desired key.")
			for i in range(len(Modes)):
				print (str(i+1)+")",Modes[i])
			Mode = int(input(">"))
			if Mode in range(1,22):
				Mode = Modes[Mode-1]
				break
			else:
				print("\nTry again!\n")
				pass
		except:
			print("\nTry again!\n")
			pass
	while True:
		try:
			Number = int(input("How many chords would you like to generate?\n\n>"))
			break
		except:
			print("\nTry again!\n")
			pass
	while True:
		try:
			ChordTones = int(input("How many chord tones per chord? would you like to generate? (1,2,3,4)\n\n>"))
			if ChordTones in range (1,5):
				break
			else:
				raise ValueError
		except:
			print("\nTry again!\n")
			pass
	ScaleGen(Tonic, Mode, Number, FS, ChordTones)


def ScaleGen(Tonic, Mode, Number, FS, ChordTones):
	RandomNumbers = []
	ScaleNotes = []
	UsedScale = []
	GeneratedChords = []
	GeneratedRoots = []
	Overflow = False
	if FS == "Sharp":
		Notes = NotesSharp
	else:
		Notes = NotesFlat

	Index = Notes.index(Tonic)

	for i in range(Number):
		RandomNumbers.append(random.randint(0,6))

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
			ChordGen(i, Temp, GeneratedChords, GeneratedRoots, UsedScale, ChordTones)
	Chords = ChordName(GeneratedChords, Notes)

	print ("Scale Used:\n\n",UsedScale,"\n")
	print ("Chords produced:\n\n",Chords)

def ChordGen(i, Temp, GeneratedChords, GeneratedRoots, UsedScale, ChordTones):
	while len(GeneratedChords[i]) != ChordTones:
		try:
			Temp = Temp + 2
			if Temp >= len(UsedScale):
				Temp = Temp - len(UsedScale)
				GeneratedChords[i].append(UsedScale[Temp])
			else:
				GeneratedChords[i].append(UsedScale[Temp])
		except:
			raise ValueError("Something has gone wrong.")

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
					name[0]=(name[0]+"+5")

			else:
				if Notes.index(Fifth) + 12 - Notes.index(Root) == 7:
					pass
				elif Notes.index(Fifth) +12  - Notes.index(Root) == 6:
					name[0]=(name[0]+"b5")
				elif Notes.index(Fifth) +12  - Notes.index(Root) == 8:
					name[0]=(name[0]+"+5")

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
		if "Maj+57" in name:
			name = name.replace("Maj+57","Maj7#5")
		if "mb" in name:
			name = name.replace("mb","m")

		if "Majb7" in name:
			name = name.replace("Majb7","7")
		if "m5b7" in name:
			name = name.replace("m5b7","m7b5")
		if "m5bb7" in name:
			name = name.replace("m5bb7","dim7")
		Chords.append(name)
	print ("\nChords\n")
	pass
if (__name__ == "__main__"):
	main()
