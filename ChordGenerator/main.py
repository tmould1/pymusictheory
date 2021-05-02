import helpers


print('Random Chords')
for i in range(5):
    chordNotes, chordRoot, chordName = helpers.GenerateRandomChord()
    print(chordRoot + chordName + ": ", *chordNotes, ' ') 


print('Random Scales')
for i in range(5):
    scaleNotes, scaleRoot, scaleName = helpers.GenerateRandomScale()
    print(scaleRoot + scaleName + ": ", *scaleNotes, ' ') 
