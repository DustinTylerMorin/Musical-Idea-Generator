## Program created for generating random melodies/riffs
## Program created by Dustin Morin
import random
AllNotes = ["Ab", "A", "A#", "Bb", "B", 'B#', "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
NotesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NotesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
Modes = ["Major", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Minor", "Locrian"]
Scale = {
"Major": [0,2,2,1,2,2,2],
"Dorian": [0,2,1,2,2,2,1],
"Phrygian": [0,1,2,2,2,1,2],
"Lydian": [0,2,2,2,1,2,2],
"Mixolydian": [0,2,2,1,2,2,1],
"Minor": [0,2,1,2,2,1,2],
"Locrian": [0,1,2,2,1,2,2,2]
}
def main():
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
				pass
		except:
			pass

	while True:
		try:
			Mode = int(input("Choose a mode.\nType the number which corresponds to the desired key.\n1)Major/Ionian\n2)Dorian\n3)Phrygian\n4)Lydian\n5)Mixolydian\n6)Minor/Aeolian\n7)Locrian\n\n>"))
			if Mode in range(1,8):
				Mode = Modes[Mode-1]
				break
			else:
				pass
		except:
			pass
	while True:
		try:
			Number = int(input("How many notes would you like to generate?\n\n>"))
			break
		except:
			pass
	Gen(Tonic, Mode, Number, FS)
def Gen(Tonic, Mode, Number, FS):
	RandomNumbers = []
	ScaleNotes = []
	UsedScale = []
	GeneratedNotes = []

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
			try:
				Index = Index + ScaleNotes[x]
				UsedScale.append(Notes[Index])
				break
			except:
				if Index > len(Notes):
					Index = len(Notes) - Index
				pass
	for y in range (len(RandomNumbers)):
		GeneratedNotes.append(UsedScale[RandomNumbers[y]])
	print ("Scale Used:\n\n",UsedScale,"\n")
	print ("Notes produced:\n\n",GeneratedNotes)




if (__name__ == "__main__"):
	main()
