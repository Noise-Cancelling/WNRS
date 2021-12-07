# WNRS

## Concept
Simple Python adaptation of the game "We're Not Really Strangers," with a single and two player mode.

Originally a game for 2-6 players, We're Not Really Starngers (WNRS) is a "question based" card game centered around deepening relationships (platonic or romantic). Players take turns asking each other questions, progressing through three different levels of questions culminating in both parties answering a final question together. 

This Python adaptation has two modes: a one player "Reflection" mode and a two player "Regular" mode. The one player mode has the player pull question from a bank of prompts, allowing them to self reflect by writing down their answers to a few prompts (separte word processor or pen/paper needed). Two player mode has players "draw cards" from a bank. After each player answers two prompts, players progress to the next "level" of questions. After they progress through all three, the final card is prompted for both players to answer.

## Areas of Improvement
Notable areas of improvement include, but are not limited to:

1. Accepting the input "one" or "two" when asking how many players the party has. I was debating accepting them, but I have not used the "try/except" loop yet, and this was an opportunity for me to do so.

2. Allowing more than two players in the "multiplayer mode." The original game allows up to 6 players, but it would require adding many more questions, for variety's sake.

3. If players want to play again, my program will take another random sample of the question banks. This includes the possibility that players receive a question they have seen before. My program could have something that asks the user if they have already got that question, and then pick another one instead.
