## Program created for generating random chords.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
import platform
import os
from datetime import datetime
from midiutil.MidiFile import MIDIFile
import traceback
#Import required libraries.

#Configuration.
Debug = False
#Debug messages will print when issues occur.
Piano = True
Guitar = True
Bass = True
Drums = True
#Enable/Disable each instrument in Midi output files.
#Configuration.

AllNotes = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
NotesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NotesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
NotesAltSharp = ["A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#", "F#", "G", "G#"]
NotesAltFlat = ["A", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab"]
#Lists of notes to be used for Scale/Note/Chord Generation.

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
#Dict of possible scales. Numbers represent the number of steps between notes.
#For ex, 2 will move 2 keys on a piano or 2 frets on a guitar ie. A -> B.

Modes = list(Scale.keys())
#List of Modes/Scales derived from the dict of possible scales.

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
#Nested Dicts of preset chord progressions for a few genres.
#For each genre the progressions are given an index, a Scale/Mode, and a list of scale degree(s).
#For ex) "Pop" : {"1" : ["Major",1,5,6,4]} would mean a major scale, in the specified keys using scale degrees 1,5,6,and 4.
#If C was chosen as the tonic, this would be a progression of C, G, A, F.

def main():
	print ("\nProgram created by Dustin Morin for the purposes of generating chord(s) or single notes in a desired key.\n")
	print ("What's the tonic of the desired key?\n\nEx(C, Gb, A#, Random)\n")
	while True:
		try:
			Tonic = str(input(">")).capitalize()
			#Tonic is the root of the key or the 1 of the key.
			FS = DetermineFS(Tonic)
			if FS != None:
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
				(Mode) = ModeConfig(Tonic, FS)
				(UsedScale, Progression, Notes, Limit)=ScaleGen(Tonic, Mode, 7, FS, "y", True)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(7, UsedScale, 4, Progression, Notes, Limit)
				(Chords, GeneratedChords, MidiLengths, UsedScale, ScaleChords)=ManualConfig(UsedScale, Tonic, Mode, FS, ScaleChords, Notes)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords, MidiLengths)
				break
			elif OpMode == 2:
				Random = False
				(Mode, Number, StartTonic, Progression) = Genre(Tonic, FS)
				(ChordTones) = NumChordTones()
				(UsedScale, Progression, Notes, Limit) = ScaleGen(Tonic, Mode, Number, FS, StartTonic, Random, Progression)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords)
				break
			elif OpMode ==1:
				Random = True
				(Mode) = ModeConfig(Tonic, FS)
				(Number) = NumChords()
				(ChordTones) = NumChordTones()
				(StartTonic) = ProgressionStart()
				(UsedScale, Progression, Notes, Limit) =ScaleGen(Tonic, Mode, Number, FS, StartTonic, Random)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords)
				break
			else:
				raise ValueError
			#Based upon user input, 1 of the 3 modes will be chosen and the needed functions for that mode called.
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
#main function which is used to facilitate what the tonic to be used is.
#Determines which mode of operation is being used. ie. Random, Genre Based, or Manual.
#Users can specify how many chords are generated, their number of chord tones, if the progression starts on the tonic.
#If export by midi is chosen the user can specify note length.
#Random uses the user input Tonic and Scale/Mode to generate a progresion.
#Genre uses a preset progression based upon user Tonic and Genre selection.
#Manual gives fine control over what notes/chords(including substitutions) are used and how long each will last in midi if exported as midi.

#DetermineFS(Tonic{String})
def DetermineFS(Tonic):
	try:
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
			#User input Tonic determines what set of notes will be used.
			#There are usecases for sharp, flat, and both for notes that are not typically b/#.
			#ie. E#, B#, Fb, Cb. since these are *typically* not how you would reference these notes.
		else:
			raise ValueError
	except ValueError as error:
		FS = None
		if Debug == True:
			traceback.print_exc()

	return(FS)
#Function used to determine set of notes to use based upon tonic
#FS{String} returned

#ModeConfig(Tonic{String},FS{String})
def	ModeConfig(Tonic,FS):
	print ("\nChoose a scale/mode.\n\nType the number which corresponds to the desired key.\n")

	curlinelen=0
	curline=""
	#Used for printing modes into a clean list.

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
		#Modes/scales are numbered and appended to a line to be printed.
		#This is to better format the options so a user doesn't need to scroll up to see every option on one screen.
	print()

	while True:
		try:
			Mode = int(input(">"))
			#Mode is the scale to be used from Modes list.

			if Mode in range(1,len(Modes)):
				Mode = Modes[Mode-1]
				break
			elif Mode == int(len(Modes)):
				Mode = Modes[random.randint(0,len(Modes)-2)]
				print ("\n",Mode)
				break
			else:
				raise ValueError
			NumChords()
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
		#Check for in the mode exists or if Random was selected.
	return (Mode)
#Funtion used to get user input on what mode/scale to use.
#if random is picked there is a random mode/scale chosen from the list Modes.
#Mode{String} returned to main() to be used in subsequent functions.

#Genre(Tonic{String},FS{String})
def Genre(Tonic,FS):
	TempGenre = list(GenreList.keys())
	#Temp var so list(GenreList.keys()) doesn't need called multiple times.

	print ("\nChoose a Genre:\n")
	for i in range(len(TempGenre)):
		print((str(i+1)+") " + str(TempGenre[i])))
	print()
	while True:
		try:
			Genre=int(input(">"))
			#Int associated with menu item/genre.

			if Genre in range(1,len(TempGenre)+1):
				Genre = Genre - 1
				#Change user input into an index.

				TempGenreList = list(GenreList.keys())
				#Temp List variable to hold a list of the genres contained in GenreList.

				GenreValues = GenreList[TempGenreList[Genre]]
				#List Var to store the values associated with the selected genre.
				#ie. the index(s) and Scale Degree(s) of the sel;ected genre.

				TempInt = str(random.randint(1,len(GenreValues)))
				#Temp String var to store the index of which Genre progression to use from the list of GenreValues.

				Progression = GenreValues[TempInt]
				#List of scale degrees based upon the selected Genre progression.

				Mode = Progression[0]
				#Set mode to the preset value in GenreList[Genre]

				Progression = Progression[1:]
				#Shave Scale/Mode value off the front of the list.

				Number = (len(Progression))
				#Number of chords to generate.
				#In this case this is set by the preset progresion.

				StartTonic = Progression[0]
				#Set StartTonic to the first value of the progression.

				for i in range (len(Progression)):
					Progression[i] = int(Progression[i]-1)
					#Change the scale degree into an index
				break

		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return (Mode,Number,StartTonic,Progression)
#Function used if Genre mode is selected in main().
#User chooses a genre based upon the nested Dict GenreList.
#A random progression is chosen from the Genres Dict.
#Mode{String},Number{Integer},StartTonic{String},Progression{List} returned to main() for use in subsequent functons.

#ManualConfig(UsedScale{List},Tonic{String},Mode{String},FS{String},ScaleChords{List},Notes{List},Random{Boolean})
def ManualConfig(UsedScale, Tonic, Mode, FS, ScaleChords,Notes):
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Chords Avaliable:\n\n",ScaleChords,"\n")
	print ("Enter Chords 1 by 1 in this format:\n\nNote,ChordTones,Midi Length,Modifier(s),Alt Scale Tonic,Alt Scale Number(Optional)\n\nEx)>"+Tonic+",4,4,sus2,add11,"+Tonic+",1""\n\n"+Tonic+"sus2add11\n\nType 'r' to remove a chord, and 'q' to quit and lock in your progression.\n")

	Modifiers = ["sus2","sus4","6","9","11","13","add9","add11","add13", "m6", "none"]
	#List of possible modifications that can be made to chords.

	ChordInputList = []
	#Used for containing the "config" of chords to be generated.

	AltTonic = []
	AltMode =[]
	AltNotes = []
	#Used for substitutions.

	ChosenScale = UsedScale
	ChosenChords = ScaleChords
	ChosenNotes = Notes

	#Set aside for scale and chord return.
	#This avoids the UsedScale/Chords being from a substitution if the last note is a substitution.

	while True:
		ChordInput = (str(input(">")))
		#string of the currently input chord and configuration.

		try:
			if ChordInput.lower() == "q":
				break
				#Exit manual entry.
			elif ChordInput.lower() == "r":
				del ChordInputList[-1]
				#Remove the last added chord.
			else:
				TempInput = ChordInput.split(",")
				#Create list of all items from user input config.
				ChordInput = list(([str(TempInput[0].capitalize()),int(TempInput[1]),int(TempInput[2]),list()]))
				if (ChordInput[0].capitalize() in AllNotes) == False:
					raise ValueError
					#Check for if the ChordInput[0] is a Note.
				if (ChordInput[1] in range(1,8)) == False:
					raise ValueError
					#Check if ChordInput[1] represents a valid number of chord tones.
				if (ChordInput[2] <= 0) == True:
					raise ValueError
					#Check if ChordInput[2] is a valid length for midi export.
				if (TempInput[-1].lower() in Modifiers) and (TempInput[-2].capitalize() not in AllNotes):
					#if the last item in config is a modifier and there's no substitution occuring.
					for i in range(3,len(TempInput[3:])+3):
						#For every Modifier.
						if (TempInput[i].lower() in Modifiers) == True:
							TempInput[i] = TempInput[i].lower()
							ChordInput[3].append(TempInput[i])
							#Ensure modifier(s) are changed to lower().
						else:
							raise ValueError
				else:
					#Subsitution might exist
					for i in range(3,len(TempInput[3:-2])+3):
						#For every Modifier.
						if (TempInput[i].lower() in Modifiers) == True:
							#Ensure Modifier Exists.
							TempInput[i] = TempInput[i].lower()
							ChordInput[3].append(TempInput[i])
							#Ensure modifier(s) are changed to lower().
							#Add Modifiers to ChordInput list.
						else:
							raise ValueError
					if (TempInput[-2]).capitalize() in AllNotes:
						#Ensure substitute tonic exists.
						ChordInput.append(TempInput[-2].capitalize())
						#Add substitute tonic to ChordInput.
					else:
						raise ValueError
					if int(TempInput[-1]) in range(1,len(Modes[0:-2])):
						#Ensure substitute mode/scale exists.
						ChordInput.append(Modes[int(TempInput[-1])-1])
						#Add substitute mode to ChordInput.
					else:
						raise ValueError
					AltTonic.append(ChordInput[-2].capitalize())
					AltMode.append(Modes[Modes.index(ChordInput[-1])])
					#Since substitution exists, assign tonic and mode alt values as compared to the tonic/mode selected prior.

				ChordInputList.append(ChordInput)
				#After input checked and sanitized, add it to the list of chords to be generated.
			print(ChordInputList)
		except:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	while True:
		try:
			ChordsList = []
			GenChordsList = []
			MidiLengths = []
			Progression = []
			#Lists to be appended to for each chord input.
			ChordTones = ChordInputList[0][1]
			#Grab value from ChordInputList.
			(UsedScale, Progression, Notes, Limit) = ScaleGen(Tonic, Mode, 7, FS, "Other", False, Progression)

			for i in range(len(ChordInputList)):
				Progression = []
				FS = DetermineFS(Tonic)
				Notes = ChosenNotes
				#Ensure FS is default to selected Scale.
				try:
					if (ChordInputList[i][-1] in Modes):
						#If substitution exists.
						TempAltTonic = AltTonic.pop(0)
						TempAltMode = AltMode.pop(0)
						#Temp Alts.
						FS = DetermineFS(TempAltTonic)
						#Ensure FS is set to substitution Scale.
						(UsedScale, Progression, Notes, Limit) = ScaleGen(TempAltTonic, TempAltMode, 7, FS, "Other", False, Progression)
						#Update UsedScale to reflect substitution.
						Progression.append(UsedScale.index((ChordInputList[i])[0]))
						#Add note index to progression for ChordGenPrep.
					else:
						UsedScale = ChosenScale
						#Update UsedScale to reflect chosen scale.
						Progression.append(UsedScale.index((ChordInputList[i])[0]))
						#Add note index to progression for ChordGenPrep.
				except:
					print("\nTry again!\n")
					if Debug == True:
						traceback.print_exc()
				Modifier = list(ChordInputList[i][3])
				#Set Modifier(s) list for ChordGenPrep.
				ChordTones = ChordInputList[i][1]
				#Set ChordTones for ChordGenPrep.
				Limit = 1
				#Limit set to 1 to skip cycles generating scale chords again.
				MidiLengths.append(ChordInputList[i][2])
				#Add midi length from current chord to MidiLengths List.
				(Chords,unused,GeneratedChords)=ChordGenPrep(1, UsedScale, ChordTones, Progression, Notes, Limit, Modifier)
				#Generate chord name and notes.
				ChordsList.append(str(Chords[0]))
				#Add Chord to ChordList.
				GenChordsList.append(GeneratedChords[0])
				#Add Chord notes to GenChordsList.
				if i == (len(ChordInputList)):
					break
					#Break out of loop when done generating chords.
			break
		except:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()

	return(ChordsList, GenChordsList, MidiLengths,ChosenScale,ChosenChords)
#Function used for manual configuration of chords.
#User inputs chords based on tonic,scale,length,chord tones,modifiers.
#ChordsList{List}, GenChordsList{List}, MidiLengths{List}, ChosenScale{List}, ChosenScale{List} Returned to main().

#NumChords()
def NumChords():
	print("\nHow many chord(s) would you like to generate?\n")
	while True:
		try:
			Number = int(input(">"))
			#Number of chords to generate.
			if Number > 0:
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(Number)
#Function for determining number of chords to generate when using random generation.
#Number{Int} returned.

#NumChordTones()
def NumChordTones():
	print("\nHow many chord tones per chord? would you like to generate? (1,2,3,4)\n")
	while True:
		try:
			ChordTones = int(input(">"))
			#Number of ChordTones to generate.
			if ChordTones in range (1,5):
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(ChordTones)
#Function for determining number of chord tones to generate when using genre or random generation.
#NumChordTones{Int} returned.

#ProgressionStart()
def ProgressionStart():
	print("\nWould you like the progression to start on the tonic? (y/n)\n")
	while True:
		try:
			StartTonic = str(input(">")).lower()
			#Whether or not to start on tonic.
			if StartTonic == "y" or StartTonic == "n":
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return(StartTonic)
#Function for determining whether ot not to start on the tonic when using random generation.
#ProgressionStart{Int} returned.

#ScaleGen(Tonic{String},Mode{String},FS{String},StartTonic{String},Random{Boolean},Progresion{List})
def ScaleGen(Tonic, Mode, Number, FS, StartTonic, Random, Progression=None):
	ScaleNotes = []
	UsedScale = []
	#Lists for Notes and Scales

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
	#Select the list of notes to use for generation.

	Index = Notes.index(Tonic)
	#Index var based on tonic.

	Limit = len(Scale.get(Mode))
	#Limit based on the number of notes in scale.

	if Random == True:
		RandomNumbers = []
		for i in range(Number):
			RandomNumbers.append(random.randint(0,Limit-1))
		if StartTonic == 'y':
			RandomNumbers[0] = 0
		if StartTonic == 'n':
			RandomNumbers[0] = random.randint(1,Limit-1)
		Progression = RandomNumbers
	#If Random True, generate scale indexes.

	for z in range(0,Limit):
		ScaleNotes.append((Scale[Mode])[z])
	#Generate Scale.

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
	#Add chord notes based on the indexs from ScaleNotes.

	return(UsedScale, Progression, Notes, Limit)
#Function for generating the scale to be used in chord generation.
#UsedScale{List},Progresion{List},Notes{List},Limit{Int} returned.

#ChordGenPrep(Number{Int},UsedScale{List},ChordTones{Int},Progression{List},Notes{List},Limit{Int},Modifier{List})
def ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit, Modifier = "none"):
	ScaleChordsGen = []
	GeneratedChords = []
	GeneratedRoots = []
	#Lists for chord and name generation.

	for y in range (Number):
		GeneratedRoots.append(UsedScale[Progression[y]])
		#Add roots to list.
	while len(GeneratedChords) != len(GeneratedRoots):
		for i in range(len(GeneratedRoots)):
			Temp = UsedScale.index(GeneratedRoots[i])
			GeneratedChords.insert(i,[GeneratedRoots[i]])
			(GeneratedChords)=ChordGen(i, Temp, GeneratedChords, UsedScale, ChordTones, Modifier)
			#Generate chords(s) based on the provided roots.
	for z in range(Limit):
		Temp = z
		ScaleChordsGen.insert(z,[UsedScale[z]])
		(ScaleChords)=ChordGen(z, Temp, ScaleChordsGen, UsedScale, ChordTones, Modifier)
		#Generate chords that are in the scale.
	Chords = ChordName(GeneratedChords, Notes, Modifier)
	ScaleChords = ChordName(ScaleChordsGen, Notes, Modifier)
	#Chords and scale chords named.

	return (Chords, ScaleChords, GeneratedChords)
#Function for preparing data for generation.
#Passes variable to ChordGen and ChordName.
#Chords{List},ScaleChords{List},GeneratedChords{List} returned.

#ChordGen(i{Int},Temp{Int},GeneratedChords{List},UsedScale{List},ChordTones{Int},Modifier{List})
def ChordGen(i, Temp, GeneratedChords, UsedScale, ChordTones, Modifier):
	Scale = []
	ScaleLen = len(UsedScale)
	#Variables for scale length.

	for x in range(len(UsedScale)):
		try:
			Scale.append(UsedScale[Temp])
			Temp += 1
		except:
			Temp = 0
			Scale.append(UsedScale[Temp])
			Temp += 1
	#Generate scale

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

	#Add chord tones until the chord is done.
		except ValueError as error:
			print("\nSomething has went wrong\n")
			if Debug == True:
				traceback.print_exc()

	GeneratedChords=Modify(i, GeneratedChords, Scale, Modifier)
	#Modify chords based on modifiers

	return(GeneratedChords)
#Function for generating chords.
#Passes variable Modify to make changes through modifiers.
#GeneratedChords{List} returned.

def Modify(i, GeneratedChords, UsedScale, Modifier):
	Modifier = str(Modifier[0:])
	#Convert Modifier from a list to a string.

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
	#Check for if a modifier exists, if it does, based on the conditions, the modifiers will occur.

	return(GeneratedChords)
#Function for modifying chords.
#GeneratedChords{List} returned.

#ChordName(GeneratedChords{List},Notes{List},Modifier{List})
def ChordName(GeneratedChords, Notes, Modifier):
	Chords = []
	#List for chord names when the name is complete.

	try:
		for i in range(len(GeneratedChords)):
			name = []
			Index = GeneratedChords[i]
			#List of chord names and Index

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
					if (((Notes.index(Thirteenth)+12 - Notes.index(Root) == 9) or (Notes.index(Thirteenth)+12 - Notes.index(Root) == 8)) or ((Notes.index(Thirteenth) - Notes.index(Root) == 9) or (Notes.index(Thirteenth) - Notes.index(Root) == 8))):
						break
				if (Notes.index(Root) < Notes.index(Thirteenth)):
					if (("Majb7" in name[0]) and ((Notes.index(Thirteenth) - Notes.index(Root) == 9) or (Notes.index(Thirteenth) - Notes.index(Root) == 8))):
						name[0]=(name[0]+"13")
					elif ("6" not in name[0]) and ((Notes.index(Thirteenth) - Notes.index(Root) == 9) or (Notes.index(Thirteenth) - Notes.index(Root) == 8)):
						name[0]=(name[0]+"add13")
				else:
					if (("Majb7" in name[0]) and ((Notes.index(Thirteenth)+12 - Notes.index(Root) == 9) or (Notes.index(Thirteenth)+12 - Notes.index(Root) == 8))):
						name[0]=(name[0]+"13")
					elif ("6" not in name[0]) and ((Notes.index(Thirteenth)+12 - Notes.index(Root) == 9) or (Notes.index(Thirteenth)+12 - Notes.index(Root) == 8)):
						name[0]=(name[0]+"add13")
			#Conditionals for determining what a chord is named.

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
			if "sus27" in name:
				name = name.replace("sus27","Maj7sus2")
			#Conditionals to make chord names more proper.

			Chords.append(name)
			#After chord name is sanitized, add it to the list of chord names.

	except:
		if Debug == True:
			traceback.print_exc()
	return(Chords)
#Function for naming generated chords.
#Chords{List} returned.

#Output(Tonic{String},Mode{String},UsedScale{List},ScaleChords{List},Chords{List})
def Output(Tonic, Mode, UsedScale, ScaleChords, Chords):
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Scale Chords:\n\n",ScaleChords,"\n\n")
	print ("Chord(s) produced:\n\n",Chords)
#Function for outputing the scale and chords generated.

#Export(UsedScale{List},GeneratedChords{List},Chords{List},Tonic{String},Mode{String},ScaleChords{List},MidiLengths{List})
def Export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,MidiLengths = []):
	ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords)
	ExportMidi(GeneratedChords,MidiLengths)
#Function for Exporting Txt and/or Midi files.
#Pass values to ExportTxt and ExportMidi

#ExportTxt(UsedScale{List},GeneratedChords{List},Chords{List},Tonic{String},Mode{String},ScaleChords{List})
def ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords):
	print("\nWould you like to output these chords to a .txt file? (y/n)\n")
	while True:
		try:
			export = str(input(">")).lower()
			#String to determine if to export txt.
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
				#Export txt file.

			elif export == "n":
				break
				#Don't export txt.

			else:
				print("\nTry again!\n")
		except ValueError as error:
			print("\nSomething has went wrong\n")
			if Debug == True:
				traceback.print_exc()
#Function for exporting TXT files of the generated chords.

#ExportMidi(GeneratedChords{List},MidiLengths{List})
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
					midi = DrumsGen(midi, track, bpm, Dur)
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
#Function for exporting Midi files of the generated chords.

#PianoGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List})
def PianoGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Piano"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 0
	volume = 100
	PianoTones = {
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
	for i in range(len(GeneratedChords)):
		pitch = PianoTones[GeneratedChords[i][0]][0]
		for x in range(0,len(GeneratedChords[i])):
			if PianoTones[GeneratedChords[i][x]][0] < pitch:
				pitch = (PianoTones[GeneratedChords[i][x]][0]) + 12
			elif PianoTones[GeneratedChords[i][x]][0] >= pitch:
				pitch =	(PianoTones[GeneratedChords[i][x]][0])
			else:
				print ("Something went terribly wrong")
			midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
	return midi
#Function for generating midi Piano.
#midi{MIDIObject} returned.

#GuitarGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List})
def GuitarGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Guitar"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 1
	volume = 100
	GuitarTones = {
	"E" : [40],
	"Fb": [40],
	"E#": [41],
	"F" : [41],
	"F#": [42],
	"Gb": [42],
	"G" : [43],
	"G#": [44],
	"Ab": [44],
	"A" : [45],
	"A#": [46],
	"Bb": [46],
	"B" : [47],
	"Cb": [47],
	"B#": [48],
	"C" : [48],
	"C#": [49],
	"Db": [49],
	"D" : [50],
	"D#": [51],
	"Eb": [51]
	}
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
	return midi
#Function for generating midi Guitar.
#midi{MIDIObject} returned.

#BassGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int},GeneratedChords{List})
def BassGen(midi, track, bpm, Dur, GeneratedChords):
	trackname = "Bass"
	time = 0
	midi.addTrackName(track, time, trackname)
	midi.addTempo(track, time, bpm)
	channel = 2
	volume = 100
	BassTones = {
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
	for i in range(len(GeneratedChords)):
		pitch = BassTones[GeneratedChords[i][0]][0]
		if BassTones[GeneratedChords[i][0]][0] < pitch:
			pitch = (BassTones[GeneratedChords[i][0]][0]) - 12
		elif BassTones[GeneratedChords[i][0]][0] >= pitch:
			pitch =	(BassTones[GeneratedChords[i][0]][0])
		else:
			print ("Something went terribly wrong")
		midi.addNote(track, channel, pitch, time, Dur[i], volume)
		time = time + Dur[i]
	return midi
#Function for generating midi Bass.
#midi{MIDIObject} returned.

#PianoGen(midi{MIDIObject},track{Int},bpm{Int},Dur{Int})
def DrumsGen(midi, track, bpm, Dur):
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
			#Snare
		if x%4 == 0:
			midi.addNote(track, channel, 36, x/2, .5, volume)
			#Kick
		if x%16 == 0:
			midi.addNote(track, channel, 49, x/2, 1, volume-25)
			#Crash
		midi.addNote(track, channel, 42, x/2, 1, volume-25)
	return midi
#Function for generating midi Drums.
#midi{MIDIObject} returned.

if (__name__ == "__main__"):
	main()
