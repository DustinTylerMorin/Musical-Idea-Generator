# Musical-Idea-Generator
Simple python program to generate musical ideas.\n
Choose a tonic for your key, scale, and the number of notes/chords you'd like to generate.\n
This can be used for the creations of chord progressions, riffs and/or melodies.\n
This program simply gives the user notes in a key in a random order and selection to spark new musical ideas.\n
Other modes of operation exist for more control over the randomness if you have a starting point already.\n
Major/Minor/Harmonic Major/Harmonic Minor/Melodic Minor/Major Pentatonic/Minor Pentatonic/Whole Tone/Chromatic are currently working along with the corresponding modes for each scale.\n
Output can be read from terminal or output to a file in the current working directory at Your-CWD/Music/Your-output-file.mid/.txt.\n
Both .txt and .mid are currently supported outputs to save ideas produced by the program.\n
Written 100% in python3.\n

#Modes of operation:
###Random Based On Scale
Choose a tonic/starting note by choice or random, choose a scale/mode by choice or random, and you're off to the races.
###Genre Based
Choose a genre and a preset chord progression will be used that is associated with that genre of music.
###Manual Entry
Complete control over which chords can be added and what scales/keys to be used. Chord substitutions possible.
###Output Scale Chords
Choose a tonic/starting note by choice or random, choose a scale/mode by choice or random, and the chords associated with that tonic and mode will be produced.


**Requirements**
python3,
pip package midiutil
