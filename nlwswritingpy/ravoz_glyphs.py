# This Python file uses the following encoding: utf-8
from glyph import *

consonants = {
    'm': (lambda painter,pos: ),
    'n': (lambda painter,pos: ),
    'ŋ': (lambda painter,pos: ),
    'b': (lambda painter,pos: ),
    'd': (lambda painter,pos: ),
    'p': (lambda painter,pos: ),
    't': (lambda painter,pos: ),
    's': (lambda painter,pos: ),
    'f': (lambda painter,pos: ),
    'š': (lambda painter,pos: ),
    'ž': (lambda painter,pos: ),
    'v': (lambda painter,pos: ),
    'z': (lambda painter,pos: ),
    'r': (lambda painter,pos: ),
    'l': (lambda painter,pos: ),
    'ř': (lambda painter,pos: ),
    'g': (lambda painter,pos: ),
    'k': (lambda painter,pos: ),
    'h': (lambda painter,pos: ),
    'x': (lambda painter,pos: )
}

class decoration(Glyph):
    def __init__(self,consonant,vowel):
        """
        decoration(consonant) creates the glyph [consonant](i|a|o)(v|f|ø)
        """
        def draw(painter,pos):
            if vowel is 'i' or vowel is 'a':
                #draw curl
                if vowel is 'i':
                    #draw triangle
                else:
                    #draw circle
                #draw consonant
            elif vowel is 'o':
                #draw V
                #draw consonant
            else:
                Error("Invalid Vowel!")
            return NotImplementedError("No glyph yet")
        super.__init__(consonant+vowel,draw,outgoing= )
