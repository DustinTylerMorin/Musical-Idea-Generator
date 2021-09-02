## Program created for generating random chords
## Program created by Dustin Morin
import random
import platform
import os
from datetime import datetime
from midiutil.MidiFile import MIDIFile


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
				print ("\n")
				break
			else:
				print("\nTry again!\n")
				pass
		except:
			print("\nTry again!\n")
			pass
	while True:
		try:
			Number = int(input("How many chord(s) would you like to generate?\n\n>"))
			print ("\n")
			break
		except:
			print("\nTry again!\n")
			pass
	while True:
		try:
			ChordTones = int(input("How many chord tones per chord? would you like to generate? (1,2,3,4)\n\n>"))
			if ChordTones in range (1,5):
				print ("\n")
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

	print ("Scale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Chord Notes\n\n",GeneratedChords)
	print ("\nChord(s) produced:\n\n",Chords)

	ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode)
	ExportMidi(GeneratedChords)

def ChordGen(i, Temp, GeneratedChords, GeneratedRoots, UsedScale, ChordTones):
	while len(GeneratedChords[i]) != ChordTones:
		try:
			Temp = Temp + 2
			if Temp >= len(UsedScale):
				Temp = Temp - len(UsedScale)
				GeneratedChords[i].append(UsedScale[Temp])
			else:
				GeneratedChords[i].append(UsedScale[Temp])
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
		if "mb5bb7" in name:
			name = name.replace("mb5bb7","dim7")
		if "Maj+57" in name:
			name = name.replace("Maj+57","Maj7#5")
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

def ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode):
	while True:
		try:
			export = str(input("\nWould you like to output these chords to a .txt file? (y/n)\n\n>")).lower()
			if export == "y":
				now = 'chords_'+datetime.now().strftime("%H:%M:%S")+'.txt'
				with open(now, 'w') as file:
					file.write("Scale Used:\n\n")
					file.write("%s %s" % (Tonic,Mode) +"\n\n")
					file.write("%s" % UsedScale)
					file.write('\n\nChord(s) produced:\n\n')
					for i in range(len(Chords)):
						file.write(str(i+1)+") ")
						file.write("%s %s" % (Chords[i],GeneratedChords[i]) + "\n")
					file.write('\n')
					file.close()
					if platform.system() == "Linux" or "MacOS" :
						print ("\nFile output to:"+os.getcwd()+"/"+now)
					else:
						print ("\nFile output to:"+os.getcwd()+'\\'+now)

				break
			elif export == "n":
				break
			else:
				print("\nTry again!\n")
		except Exception as e:
			print(e)
			print("\nSomething has went wrong\n")

def ExportMidi(GeneratedChords):
	while True:
		try:
			export = str(input("\nWould you like to output these chords to a .mid file? (y/n)\n\n>")).lower()
			if export == "y":
				now = 'chords_'+datetime.now().strftime("%H:%M:%S")+'.mid'
				midi = MIDIFile(1)
				track = 0
				time = 0
				name = str("ChordGen"+str(now))
				midi.addTrackName(track, time, "MidiOut")
				midi.addTempo(track, time, 60)
				channel = 0
				volume = 100
				for i in range(len(GeneratedChords)):
					pitch = Tones[GeneratedChords[i][0]][0]
					time = i
					duration = 4
					midi.addNote(track, channel, pitch, time, duration, volume)
					for x in range(1,len(GeneratedChords[i])):
						if Tones[GeneratedChords[i][x][0]][0] < pitch:
							pitch = (Tones[GeneratedChords[i][x][0]][0]) + 12
						elif Tones[GeneratedChords[i][x][0]][0] > pitch:
							pitch =	Tones[GeneratedChords[i][x][0]][0]
						else:
							print ("Something went terribly wrong")
						time = i
						duration = 4
						midi.addNote(track, channel, pitch, time, duration, volume)
					# write it to disk
				with open(now, 'wb') as file:
					midi.writeFile(file)
					file.close()
				if platform.system() == "Linux" or "MacOS" :
					print ("\nFile output to:"+os.getcwd()+"/"+now)
				else:
					print ("\nFile output to:"+os.getcwd()+'\\'+now)
				break
			elif export == "n":
				break
			else:
				print("\nTry again!\n")
		except Exception as e:
			print(e)
			print("\nSomething has went wrong\n")



if (__name__ == "__main__"):
	main()
