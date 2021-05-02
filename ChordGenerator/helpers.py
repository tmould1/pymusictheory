import random

# Public API
def GenerateRandomScale():
    scaleRoot = random.choice(westernNotes)
    scaleId = random.randrange(len(scaleTypes))
    return [ MakeScale_Interal( scaleRoot, scaleTypes[scaleId] ), scaleRoot, scaleNames[scaleId] ]

def GenerateRandomChord():
    chordRoot = random.choice(westernNotes)
    chordId = random.randrange(len(chordTypes))
    return [ MakeChord_Interal( chordRoot, chordTypes[chordId] ), chordRoot, chordNames[chordId] ]

def MakeScaleByName( rootNote, scaleFormName ):    
    return MakeScale_Interal( rootNote, scaleTypes[GetScaleFormIndex_Interal(scaleFormName.lower())] )

def MakeChordByName( rootNote, chordFormName ):    
    return MakeChord_Interal( rootNote, chordTypes[GetChordFormIndex_Interal(chordFormName.lower())] )

# Interal functions
def MakeScale_Interal( root, scaleForm ):
    rootNoteIndex = 0
    for i in range(len(westernNotes)):
        note = westernNotes[i]
        if( note == root ):
            rootNodeIndex = i
            break

    scaleNotes = []
    scaleNotes.append(westernNotes[rootNodeIndex])

    numberOfNotes = len(westernNotes)
    nextIndex = rootNodeIndex
    for i in range(len(scaleForm)):
        nextIndex = (rootNodeIndex + scaleForm[i]) % numberOfNotes
        scaleNotes.append(westernNotes[nextIndex])
    
    return scaleNotes

def GetChordFormIndex_Interal( chordName ):
    for i in range(len(chordNames)):
        if( chordNames[i].lower() == chordName ):
            return i

def MakeChord_Interal( root, chordForm ):
    rootNoteIndex = 0
    for i in range(len(westernNotes)):
        note = westernNotes[i]
        if( note == root ):
            rootNodeIndex = i
            break

    chordNotes = []
    chordNotes.append(westernNotes[rootNodeIndex])

    numberOfNotes = len(westernNotes)
    nextIndex = rootNodeIndex
    for i in range(len(chordForm)):
        nextIndex = (rootNodeIndex + chordForm[i]) % numberOfNotes
        chordNotes.append(westernNotes[nextIndex])
    return chordNotes

def GetScaleFormIndex_Interal( scaleName ):
    for i in range(len(scaleNames)):
        if( scaleNames[i].lower() == scaleName ):
            return i

#Data
westernNotes = [
    "A", "A#",
    "B",
    "C", "C#",
    "D", "D#",
    "E",
    "F", "F#",
    "G", "G#",
]

scaleNames = [ "Maj", "min" ]
majorScale = [ 2, 4, 5, 7, 9, 11 ]
minorScale = [ 2, 3, 5, 7, 9, 11 ]
scaleTypes = [ majorScale, minorScale ]


chordNames = [ "Maj", "min", "dim", "Maj7", "min7", "dom7", "sus2", "sus4", "aug" ]
majorChord  = [ 4, 7 ]
minorChord  = [ 3, 7 ]
dimChord    = [ 3, 6 ]
maj7Chord   = [ 4, 7, 11 ]
min7Chord   = [ 3, 7, 10 ]
dom7Chord   = [ 4, 7, 10 ]
sus2Chord   = [ 2, 7 ]
sus4Chord   = [ 5, 7 ]
augChord    = [ 4, 8 ]
chordTypes = [ majorChord, minorChord, dimChord, maj7Chord, min7Chord, dom7Chord, sus2Chord, sus4Chord, augChord ]
