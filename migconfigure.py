## Program created for generating musical ideas.
## Program created by Dustin Morin.
##GPL-3.0-or-later.
#musical-idea-generator Configuration File

#Configuration.
Debug = True
#Debug messages will print when issues occur.
Piano = [True,"Lead"] #Rhythm or Lead
Guitar = [True,"Lead"] #Rhythm or Lead
Bass = [True,"Advanced"] #Basic or Advanced
Drums = [True,"Rock"] # Pop, Rock, Blues, Metal, Country, Punk ***Genre configuration does not overwrite user input genre, Used for development reasons***
#Enable(True)/Disable(False) each instrument in Midi output files. Options for how the instruments act.
#Configuration.

AllNotes = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]
NotesSharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NotesFlat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
NotesAltSharp = ["A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#", "F#", "G", "G#"]
NotesAltFlat = ["A", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb", "F", "Gb", "G", "Ab"]
#Lists of notes to be used for Scale/Note/Chord Generation.

Scale = {
"Major": [0,2,2,1,2,2,2], "Dorian": [0,2,1,2,2,2,1], "Phrygian": [0,1,2,2,2,1,2],
"Lydian": [0,2,2,2,1,2,2], "Mixolydian": [0,2,2,1,2,2,1], "Minor": [0,2,1,2,2,1,2],
"Locrian": [0,1,2,2,1,2,2],

"Major Pentatonic": [0,2,2,3,2], "Minor Pentatonic": [0,3,2,2,3], "Blues Minor Pentatonic": [0,3,2,3,2],
"Suspended Pentatonic":[0,2,3,2,3], "Blues Hexatonic": [0,3,2,1,1,3],

"Harmonic Major": [0,2,2,1,2,1,3], "Dorian b5": [0,2,1,2,1,3,1],"Phrygian b4": [0,1,2,1,3,1,2],
"Lydian b3": [0,2,1,3,1,2,2], "Mixolydian b2": [0,1,3,1,2,2,1], "Lydian Augmented #2": [0,3,1,2,2,1,2],
"Locrian bb7": [0,1,2,2,1,2,1],

"Harmonic Minor": [0,2,1,2,2,1,3], "Locrian 6": [0,1,2,2,1,3,1], "Ionian #5": [0,2,2,1,3,1,2],
"Dorian #4": [0,2,1,3,1,2,1], "Phrygian Dominant": [0,1,3,1,2,1,2], "Lydian #2": [0,3,1,2,1,2,2],
"Super Locrian bb7": [0,1,2,1,2,2,1],

"Melodic Minor": [0,2,1,2,2,2,2], "Dorian b2": [0,1,2,2,2,2,1], "Lydian Augmented": [0,2,2,2,2,1,2],
"Lydian Dominant": [0,2,2,2,1,2,1], "Mixolydian b6": [0,2,2,1,2,1,2], "Locrian #2": [0,2,1,2,1,2,2],
"Super Locrian": [0,1,2,1,2,2,2],

"Double Harmonic Major":[0,1,3,1,2,1,3], "Lydian #2 #6":[0,3,1,2,1,3,1], "Ultraphrygian":[0,1,2,1,3,1,1],
"Harmonic Minor #4":[0,2,1,3,1,1,3], "Mixolydian b2 b5":[0,1,3,1,1,3,1], "Ionian Augmented #2":[0,3,1,1,3,1,2],
"Locrian bb3 bb7":[0,1,1,3,1,2,1],

"Whole Tone": [0,2,2,2,2,2], "Chromatic": [0,1,1,1,1,1,1,1,1,1,1,1], "Random": []
}
#Dict of possible scales. Numbers represent the number of steps between notes.
#For ex, 2 will move 2 keys on a piano or 2 frets on a guitar ie. A -> B, D# -> F.
#Custom scales can be added by follwing the format and adding the scale anywhere before "Random".

Modes = list(Scale.keys())
#List of Modes/Scales derived from the dict of possible scales.

TimeSignatures = ["4/4", "3/4", "2/4", "6/8", "9/8", "5/4"]
#List of possible time signatures.
Accents = {
"4/4":["Kick",0,"Snare",2], "3/4":["Kick",0,1,"Snare",2],
"2/4":["Kick",0,"Snare",1], "6/8":["Kick",0,1,"Snare",3],
"9/8":["Kick",0,3,7,"Snare",4,8], "5/4":["Kick",0,2,"Snare",1,3]
}
#Index of where the kick/snare accents are in each time signature

GenreList = {
	"Pop" : {
	"1" : ["Major",1,5,6,4], "2" : ["Major",5,6,4,1], "3" : ["Major",1,4,5],
	"4" : ["Major",1,6,4,5], "5" : ["Major",6,4,1,5], "6" : ["Major",1,4,6,5],
	"7" : ["Major",1,6,3,7], "8" : ["Major",2,5,1], "9" : ["Major",1,5,4]
	},

	"Rock" : {
	"1" : ["Major",1,5,6,4], "2" : ["Major",1,4,5], "3" : ["Major",4,6,1,5],
	"4" : ["Minor",1,4,7], "5" : ["Major",1,5,6,3,4,1,4,5], "6" : ["Major",2,4,5],
	"7" : ["Major",5,4,1], "8" : ["Major",2,1,5,7], "9" : ["Mixolydian",1,7],
	"10": ["Mixolydian",1,7,4,1], "11": ["Mixolydian",1,7,4,5,1], "12": ["Major",2,1,4,5],
	"13": ["Phrygian",1,3,5,4,6], "14": ["Lydian",1,6,2,3,6,2,1], "15": ["Harmonic Major",1,4,5],
	"16": ["Harmonic Major",1,2,4,5], "17": ["Harmonic Major",1,3,5,4], "18": ["Minor",1,6,7],
	"19": ["Minor",1,6,3,7], "20": ["Minor",1,4,1,6,5,1], "21": ["Minor",6,7,1],
	"22": ["Minor",1,7,6,5], "22": ["Minor",1,4,3,6], "23": ["Major",1,2,5,1],
	"24": ["Minor",1,2,5,1], "25": ["Minor",3,2,1,6], "26": ["Minor",1,5,6,7]
	},

	"Metal" : {
	"1" : ["Minor",6,4,1,3], "2" : ["Minor",1,1,6,5], "3" : ["Harmonic Minor",1,7,6,5],
	"4" : ["Minor",1,1,6,7], "5" : ["Minor",6,6,1,7], "6" : ["Minor",3,2,1,6],
	"7" : ["Minor",1,6,3,7]
	},

	"Blues" : {
	"1" : ["Major",1,1,1,1,4,4,1,1,5,4,1,5], "2" : ["Major",1,1,1,1,4,4,1,1,5,5,1,1],
	"3" : ["Major",1,4,1,1,4,4,1,1,5,4,1,5], "4" : ["Major",1,1,1,1,4,4,1,1,5,4,1,4,1,5],
	"5" : ["Major",1,1,1,1,4,4,1,1,5,6,1,5], "6" : ["Minor",1,4,1,6,5,1],
	"7" : ["Major",6,2,6,4,3], "8" : ["Major",6,1,7], "9" : ["Major",6,6,1,1,7,7]
	},

	"Country" : {
	"1" : ["Major",1,4,5], "2" : ["Major",1,5,4], "3" : ["Major",1,5,6,4],
	"4" : ["Major",1,6,5,4], "5" : ["Major",6,5,4], "6" : ["Major",6,1,5,4],
	"7" : ["Major",6,2,5,1,4], "8" : ["Major",1,6,2,5], "9" : ["Major",1,6,2,5,1],
	"10" : ["Major",1,1,4,5]
	},

	"Punk" : {
	"1" : ["Major",1,4,5,], "2" : ["Major",1,5,6,4], "3" : ["Major",1,6,3,7],
	"4" : ["Major",1,6,3,7], "5" : ["Major",4,1,5,6]
	},

	"Stoner Rock" : {
	"1" : ["Dorian",1,7,1,6,7,3,4], "2" : ["Minor",1,7,1,5,3,4], "3" : ["Dorian",1,7,1,7,6,5,3]
	}

}
#Nested Dicts of preset chord progressions for a few genres.
#For each genre the progressions are given an index, a Scale/Mode, and a list of scale degree(s).
#For ex) "Pop" : {"1" : ["Major",1,5,6,4]} would mean a major scale, in the specified keys using scale degrees 1,5,6,and 4.
#If C was chosen as the tonic, this would be a progression of C, G, A, F.
#Custom progressions/genres can be added by follwing the above format
