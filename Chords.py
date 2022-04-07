## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.

import random
import platform
import os
from datetime import datetime
from midiutil.MidiFile import MIDIFile
import traceback
from PianoGen import *
from GuitarGen import*
from BassGen import *
from DrumsGen import *
from migconfigure import *
#Import required configuration variables.
#Import required libraries.

def main():
	print ("\nProgram created by Dustin Morin for the purposes of generating chord(s) or single notes in a desired key.\n")
	print ("What's the tonic of the desired key?\n\nEx(C, Gb, A#, Random)\n")
	while True:
		try:
			Tonic = str(input(">")).capitalize()
			#Tonic is the root of the key or the 1 of the key.
			Tonic, FS = DetermineFS(Tonic)
			if FS != None:
				break
			else:
				raise ValueError
		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	print("\nWould you like the chords to be:\n \n1)Random Based On Scale \n2)Genre Based \n3)Manual Entry\n4)Output Scale Chords\n")
	while True:
		try:
			OpMode = int(input(">"))
			if OpMode == 4:
				(Mode) = ModeConfig(Tonic, FS)
				(UsedScale, Progression, Notes, Limit)=ScaleGen(Tonic, Mode, 7, FS, "y", True)
				Random = False
				Progression = []
				for i in range(len(UsedScale)+1):
					Progression.append(i)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(len(UsedScale), UsedScale, 4, Progression, Notes, Limit)
				Genre = None
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords, [], Genre)
				break
			elif OpMode == 3:
				Random = False
				(Mode) = ModeConfig(Tonic, FS)
				unused,unused,unused,unused,Genre = ChooseGenre(Tonic,FS)
				(UsedScale, Progression, Notes, Limit)=ScaleGen(Tonic, Mode, 7, FS, "y", True)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(7, UsedScale, 4, Progression, Notes, Limit)
				(Chords, GeneratedChords, MidiLengths, UsedScale, ScaleChords)=ManualConfig(UsedScale, Tonic, Mode, FS, ScaleChords, Notes)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords, MidiLengths, Genre)
				break
			elif OpMode == 2:
				Random = False
				(Mode, Number, StartTonic, Progression, Genre) = ChooseGenre(Tonic, FS)
				(ChordTones) = NumChordTones()
				(UsedScale, Progression, Notes, Limit) = ScaleGen(Tonic, Mode, Number, FS, StartTonic, Random, Progression)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords,[], Genre)
				break
			elif OpMode ==1:
				Random = True
				(Mode) = ModeConfig(Tonic, FS)
				(Number) = NumChords()
				(ChordTones) = NumChordTones()
				(StartTonic) = ProgressionStart()
				unused,unused,unused,unused,Genre = ChooseGenre(Tonic,FS)
				(UsedScale, Progression, Notes, Limit) =ScaleGen(Tonic, Mode, Number, FS, StartTonic, Random)
				(Chords, ScaleChords, GeneratedChords) = ChordGenPrep(Number, UsedScale, ChordTones, Progression, Notes, Limit)
				Output(Tonic, Mode, UsedScale, ScaleChords, Chords)
				Export(UsedScale, GeneratedChords, Chords, Tonic, Mode, ScaleChords,[], Genre)
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
	return(Tonic, FS)
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

#ChooseGenre(Tonic{String},FS{String})
def ChooseGenre(Tonic,FS):
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
				TempGenre = list(GenreList.keys())
				#Temp var so list(GenreList.keys()) doesn't need called multiple times.

				Genre = list(GenreList.keys())[Genre]

				for i in range (len(Progression)):
					Progression[i] = int(Progression[i]-1)
					#Change the scale degree into an index
				break

		except ValueError as error:
			print("\nTry again!\n")
			if Debug == True:
				traceback.print_exc()
	return (Mode,Number,StartTonic,Progression,Genre)
#Function used if Genre mode is selected in main().
#User chooses a genre based upon the nested Dict GenreList.
#A random progression is chosen from the Genres Dict.
#Mode{String},Number{Integer},StartTonic{String},Progression{List} returned to main() for use in subsequent functons.

#ManualConfig(UsedScale{List},Tonic{String},Mode{String},FS{String},ScaleChords{List},Notes{List},Random{Boolean})
def ManualConfig(UsedScale, Tonic, Mode, FS, ScaleChords,Notes):
	print ("\nScale Used:\n\n",Tonic,Mode,"\n\n",UsedScale,"\n")
	print ("Chords Avaliable:\n\n",ScaleChords,"\n")
	print ("Enter Chords 1 by 1 in this format:\n\nNote,ChordTones,Midi Length,Modifier(s),Alt Scale Tonic,Alt Scale Number(Optional)\n\nEx)>"+Tonic+",4,4,sus2,add11,"+Tonic+",1""\n\n"+Tonic+"sus2add11\n\nType 'r' to remove a chord, and 'q' to quit and lock in your progression.\n")

	Modifiers = ["sus2","sus4","6","9","11","13","add9","add11","add13", "m6", "5", "none" ]
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
				if len(ChordInputList) > 0:
					break
					#Exit manual entry.

				else:
					raise ValueError
					#There are no inputs, try again!

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
					if (ChordInput[0].capitalize() in UsedScale) == False:
						raise ValueError
						#Ensure note is actually in scale and wasn't meant to be substitution.

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
				Tonic, FS = DetermineFS(Tonic)
				Notes = ChosenNotes
				#Ensure FS is default to selected Scale.
				try:
					if (ChordInputList[i][-1] in Modes):
						#If substitution exists.
						TempAltTonic = AltTonic.pop(0)
						TempAltMode = AltMode.pop(0)
						#Temp Alts.
						TempAltTonic, FS = DetermineFS(TempAltTonic)
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
		(ScaleChords)=ChordGen(z, Temp, ScaleChordsGen, UsedScale, ChordTones, [])
		#Generate chords that are in the scale.
	Chords = ChordName(GeneratedChords, Notes, Modifier, UsedScale)
	ScaleChords = ChordName(ScaleChordsGen, Notes, Modifier, UsedScale)
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

#IntervalChecker(Interval1{String},Interval2{String},UsedScale{List},Notes{List})
def IntervalChecker(Interval1, Interval2, UsedScale, Notes):
	TempUsed = UsedScale[UsedScale.index(Interval1):]

	for i in range (len(UsedScale[0:UsedScale.index(Interval1)])):
		TempUsed.append(UsedScale[i])

	TempNotes = Notes[Notes.index(Interval1):]

	for i in range (len(Notes[0:Notes.index(Interval1)])):
		TempNotes.append(Notes[i])

	ScaleDistance=TempUsed.index(Interval2) - TempUsed.index(Interval1)

	IntervalDistance=TempNotes.index(Interval2) - TempNotes.index(Interval1)
	return(ScaleDistance, IntervalDistance)
#Function for checking distance between IntervalDistance
#Returns ScaleDistance{Int},IntervalDistance{Int}

#Modify(i{Int},GeneratedChords{List},UsedScale{List},Modifier{List})
def Modify(i, GeneratedChords, UsedScale, Modifier):
	Modifier = str(Modifier[0:])
	#Convert Modifier from a list to a string.

	if ("sus2" in Modifier) and (len(GeneratedChords[i]) >= 2):
		GeneratedChords[i][1] = (UsedScale[1])

	if ("sus4" in Modifier) and (len(GeneratedChords[i]) >= 2):
		GeneratedChords[i][1] = (UsedScale[3])

	if ("5" in Modifier) and (len(GeneratedChords[i]) >= 2):
		Temp = str(GeneratedChords[i][0])
		GeneratedChords[i] = []
		GeneratedChords[i] = [Temp]
		GeneratedChords[i].append(UsedScale[4])

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

#ChordName(GeneratedChords{List},Notes{List},Modifier{List},UsedScale{List})
def ChordName(GeneratedChords, Notes, Modifier, UsedScale):
	Chords = []
	#List for chord names when the name is complete.

	try:
		for i in range(len(GeneratedChords)):
			name = []
			if len(GeneratedChords[i]) >= 1:
				Interval1 = GeneratedChords[i][0]
				name.append(Interval1)
			if len(GeneratedChords[i]) >= 2:
				Interval2 = GeneratedChords[i][1]
				ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
				if IntervalDistance ==  5:
					name[0]=(name[0]+"sus4")
				elif IntervalDistance ==  4:
					name[0]=(name[0]+"Maj")
				elif IntervalDistance ==  3:
					name[0]=(name[0]+"m")
				elif IntervalDistance ==  2:
					name[0]=(name[0]+"sus2")

			if len(GeneratedChords[i]) >= 3:
				Interval2 = GeneratedChords[i][2]
				ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
				if IntervalDistance ==  8:
					name[0]=(name[0]+"#5")
				elif IntervalDistance ==  7:
					pass
				elif IntervalDistance ==  6:
					name[0]=(name[0]+"b5")

			if len(GeneratedChords[i]) >= 4:
				Interval2 = GeneratedChords[i][3]
				ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
				if IntervalDistance ==  11:
					name[0]=(name[0]+"7")
				if IntervalDistance ==  10:
					name[0]=(name[0]+"b7")
				if IntervalDistance ==  9 and ("13" not in str(Modifier[0])):
					print (Modifier)
					name[0]=(name[0]+"6")
				if IntervalDistance ==  8 and ("13" not in str(Modifier[0])):
					print (Modifier)
					name[0]=(name[0]+"6")

			if len(GeneratedChords[i]) >= 4:
				for x in range(3,len(GeneratedChords[i])):
					Interval2 = GeneratedChords[i][x]
					ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
					if IntervalDistance ==  2:
						break
				if "Majb7" in name[0] and IntervalDistance ==  2:
					name[0]=(name[0]+"9")
				elif ("sus2" not in name[0]) and  IntervalDistance ==  2:
					name[0]=(name[0]+"add9")

			if len(GeneratedChords[i]) >= 4 :
				for x in range(3,len(GeneratedChords[i])):
					Interval2 = GeneratedChords[i][x]
					ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
					if IntervalDistance ==  5:
						break

				if "Majb7" in name[0] and IntervalDistance ==  5:
					name[0]=(name[0]+"11")
				elif ("sus4" not in name[0]) and IntervalDistance ==  5:
					name[0]=(name[0]+"add11")

			if len(GeneratedChords[i]) >=4 :
				for x in range(3,len(GeneratedChords[i])):
					Interval2 = GeneratedChords[i][x]
					ScaleDistance, IntervalDistance = IntervalChecker(Interval1, Interval2, UsedScale, Notes)
					if (IntervalDistance == 8 or IntervalDistance == 9):
						break
				if "Majb7" in name[0] and (IntervalDistance == 8 or IntervalDistance == 9):
					name[0]=(name[0]+"13")
				elif ("6" not in name[0]) and (IntervalDistance == 8 or IntervalDistance == 9):
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
			if "711" in name:
				name = name.replace("711","7/11")
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
def Export(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,MidiLengths = [],Genre = None):
	ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,Genre)
	ExportMidi(GeneratedChords,MidiLengths,UsedScale,Genre)
#Function for Exporting Txt and/or Midi files.
#Pass values to ExportTxt and ExportMidi

#ExportTxt(UsedScale{List},GeneratedChords{List},Chords{List},Tonic{String},Mode{String},ScaleChords{List})
def ExportTxt(UsedScale,GeneratedChords,Chords,Tonic,Mode,ScaleChords,Genre):
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
					file.write("\n\nGenre Chosen:\n\n")
					file.write("%s" % Genre)
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
def ExportMidi(GeneratedChords, MidiLengths, UsedScale, Genre):
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
								if RanDur == "f":
									print ("\nHow many beats (Quarter Notes) would you like each chord to last?\n")
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
						Durations = [1,2,4,6,8]
						for i in range(len(GeneratedChords)):
							Dur.append(Durations[random.randint(0,2)])
						break
					elif RanDur == "Manual":
						break
					else:
						print("\nSomething has went wrong\n")
					DurLen = 0
					for i in range(len(Dur)+1):
						Durlen += Dur[i]
					if Durlen%4 != 0:
						Temp = Durlen%4
						Dur[-1] = Dur[-1] + Temp
					#Ensure 4/4 for now

				if Genre == None:
					print("\nWhat genre of music would you like?\n")
					TempGenre = list(GenreList.keys())
					for i in range(len(TempGenre)):
						print((str(i+1)+") " + str(TempGenre[i])))
					print()
					while True:
						try:
							Genre = int(input(">"))
							if Genre in range(1,len(TempGenre)+1):
								Genre = TempGenre[Genre-1]
								break
							else:
								raise ValueError
						except ValueError as error:
							print("\nTry again!\n")
							if Debug == True:
								traceback.print_exc()
				else:
					pass
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
				if Piano[0] == True:
					numtracks += 1
					if Piano[1] == "Lead":
						numtracks += 1
				if Guitar[0] == True:
					numtracks += 1
					if Guitar[1] == "Lead":
						numtracks += 1
				if Bass[0] == True:
					numtracks += 1
				if Drums[0] == True:
					numtracks += 1
				midi = MIDIFile(numtracks)
				track = 0
				if Piano[0] == True:
					midi = PianoGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre)
					track += 1
					if Piano[1] == "Lead":
						track += 1
				if Guitar[0] == True:
					midi =	GuitarGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre)
					track += 1
					if Guitar[1] == "Lead":
						track += 1
				if Bass[0] == True:
					midi = BassGen(midi, track, bpm, Dur, GeneratedChords, UsedScale, Genre)
					track += 1
				if Drums[0] == True:
					midi = DrumsGen(midi, track, bpm, Dur, Genre)
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
#Returns GeneratedChords{List}

if (__name__ == "__main__"):
	main()
