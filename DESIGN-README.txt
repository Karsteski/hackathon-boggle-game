# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:22:58 2021

@author: X
"""

----DESIGN IDEAS-----

Karsteski, your code should use mine. It should instantiate my Boggle class
and it should call the members to alter the state to advance the game.

Basically,

def render_player_word_search():
    code here that pulls out
    boggle.g
    to put letters on the buttons
    and 
    boggle.pnames and boggle.scores
    to render the names and running score

boggle.process_player_wordlists()

def render_round_victory_screen():
    stuff
    
repeat a few times then

def render_game_victor_screen():
    maybe ask the to play again
    
alternating back and forth between your functions and mine

Alternatively, you could insert calls to your render functions into my code,
basically swapping out the print statements.

But that's a bad idea. Sure it may be tempting to use my game logic that
determines the round winners, but that was just silly 5 minute code to get a
testable proof of concept.

If you embed gui functions into the Boggle class, it's gonna get disorganized.
Sure, we may need to modify the Boggle class in case there's something I hadn't
thought of, but alterations should be done conservatively.

The main design principle should be:

Provide a graphical interface for the user to select his desired input, then
pass that input to the game logic, let that change the state, and then render
new visuals as appropriate.

To that end, since you're using like a game engine that basically renders every
microsecond, what you're gonna want to do is have separate modes.

The "game loop" or the "render loop" will display the visual elements, buttons
and text, over and over again, (and the mouse will be able to drag and drop
paths) but that will only be until the round is over (or the intermission is
over) and then a different game loop mode will be loaded for the user.