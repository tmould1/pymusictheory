import unittest

import helpers

class TestUM(unittest.TestCase):
    def test_Get_Chord_Form_Index(self):
        self.assertEqual(1, helpers.GetChordFormIndex_Interal("min"))

    def test_Get_Scale_Form_Index(self):
        self.assertEqual(1, helpers.GetScaleFormIndex_Interal("min"))

    def test_C_Major_Scale(self):
        scale_notes = helpers.MakeScaleByName( "C", "Maj" )
        C_Maj = [ "C", "D", "E", "F", "G", "A", "B" ]
        self.assertListEqual(C_Maj, scale_notes)

    def test_F_Major_Scale(self):
        scale_notes = helpers.MakeScaleByName( "F", "Maj" )
        actual_scale = [ "F", "G", "A", "A#", "C", "D", "E" ]
        self.assertListEqual(actual_scale, scale_notes)

    def test_C_Major_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Maj" )
        C_Maj = [ "C", "E", "G" ]
        self.assertListEqual(C_Maj, chord_notes)

    def test_C_Minor_Scale(self):
        scale_notes = helpers.MakeScaleByName( "C", "min" )
        C_min = [ "C", "D", "D#", "F", "G", "A", "B" ]
        self.assertListEqual(C_min, scale_notes)

    def test_C_Minor_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "min" )
        C_min = [ "C", "D#", "G" ]
        self.assertListEqual(C_min, chord_notes)

    def test_C_Sus2_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Sus2" )
        actual_chord = [ "C", "D", "G" ]
        self.assertListEqual(actual_chord, chord_notes)

    def test_C_Sus4_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Sus4" )
        actual_chord = [ "C", "F", "G" ]
        self.assertListEqual(actual_chord, chord_notes)


    def test_C_Dim_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Dim" )
        actual_chord = [ "C", "D#", "F#" ]
        self.assertListEqual(actual_chord, chord_notes)


    def test_C_Maj7_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Maj7" )
        actual_chord = [ "C", "E", "G", "B" ]
        self.assertListEqual(actual_chord, chord_notes)


    def test_C_min7_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "min7" )
        actual_chord = [ "C", "D#", "G", "A#" ]
        self.assertListEqual(actual_chord, chord_notes)

    def test_C_Dom7_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Dom7" )
        actual_chord = [ "C", "E", "G", "A#" ]
        self.assertListEqual(actual_chord, chord_notes)

    def test_C_Aug_Chord(self):
        chord_notes = helpers.MakeChordByName( "C", "Aug" )
        actual_chord = [ "C", "E", "G#" ]
        self.assertListEqual(actual_chord, chord_notes)

    def test_Get_Root_Node_Index_A(self):
        rootNote = helpers.GetRootNodeIndex_Internal("A")
        actual_index = 0
        self.assertEqual(rootNote, actual_index)    
    
    def test_Get_Root_Node_Index_GSharp(self):
        rootNote = helpers.GetRootNodeIndex_Internal("G#")
        actual_index = 11
        self.assertEqual(rootNote, actual_index)

    def test_Apply_And_Return_Form(self):
        testForm = helpers.ApplyAndReturnForm_Internal(3, [ 4, 7 ])
        actualForm = [ "C", "E", "G"]
        self.assertListEqual(testForm, actualForm)
    