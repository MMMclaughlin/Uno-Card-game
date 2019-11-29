# CHANGELOG

* v1.1.0 [2019-11-08]: Added a SmartAI computer opponent.
  Added strategy players.SmartAI
  None of the bugs have been fixed.

* v1.1.0 [2019-10-25]: First major release.
  This version is known to contain some bugs.
  
 v1.1.1 [2019-11-20]: Fixed out of range error with itterating between player selection in switch.py's run round function.
  
  v1.1.2 [2019-11-23]: Fixed the Pick up card function.The function now correctly Loops up to N+1 so that each player  
  Picks up 7 cards instead of 6.
  
  v1.1.3 [2019-11-23]: Deck size was 4 cards to big due to duplication of A in the card list inside the cards.py file.
  
  v1.1.4 [2019-11-23]: Changed discard function to use "or" instead of "and" for suit or value matching check
  
  v1.1.5 [2019-11-23]:Fixed the use of Jpip in the cards.py file for the Jack card. Switched to J
  
  v1.1.6 [2019-11-23]:Fixed ace discard test which was discarding a K instead of a A. I have kept this with a not   
  statement as a check that it is specifically working for ace and not a broken discard.
  
  v1.1.7 [2019-11-23]:Fixed the condition which was checking for 4 rather than 2 for setting pick up 2 to true.
  
  v1.1.8 [2019-11-23]:Fixed game direction change which was multiplying by 1 instead of -1
  
  v1.1.9 [2019-11-23]: Fixed hand size normalising function which had the idx on the wrong side of the colon
  
  v1.1.10 [2019-11-23]:Fixed the flags  for discarding 2,4 and 8 to reset once used. 
  
  v1.1.11 [2019-11-23]:Fixed the discard-able check which allowed any card to be discarded.
  
  v1.1.12 [2019-11-26]:Fixed so the question of whether AI players should be added is not shown when the game is already  
  full. 
  
  v1.1.13 [2019-11-26]: Fixed so that discarding 8 actually skips a players turn 
  
  v1.1.14 [2019-11-26]: Updated and fixed docstrings with Parameters and returns
  
  v1.1.15 [2019-11-27]: Created a new test for a player not being able to play until the discard pile is shuffled back in.
  
  v1.1.16 [2019-11-27]:Removed Dorothy from the list of AI player names as there is never a case where all 4 ai players
  are needed.
  v1.1.17 [2019-11-29]:Normalised hand sizes passed the test but the actual interface was incorrect