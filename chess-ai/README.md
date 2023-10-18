# Chess AI

### Introduction


Welcome to my chesscomputer. This is my first big project using python. It works using the minimax algorithm, which simulates every position a certain depth into the future. Then it evaluates all moves, and when it is done, it returns the best move for the AI, if both players play optimally, at least according to its evaluation function.

The difficult thing about this project, is that it quickly evaluates millions of positions, and then when there is a bug, it could be countless of places it went wrong, and it's not always easy to find which edgecase came up. Therefore it is extremely important that everything is streamlined, and whenever you simulates moves in the future, everything must be put back to place in the position and state it was.

The fun thing about this project, is that it is heavily reliant on effeciency and fast code. As you code is ran millions of times over and over, small changes can have a big impact. The first prototype, could only search with a depth of 3, within an acceptabel timeframe on my device (1-5 secs). But as I continuously improved the search algorithm and the evaluation algorithm, I was able to improve the speed by 150x, which then allowed me to highten the depth to 5 and sometimes 6.
***
### AI


As I didn't want to spend time building a chess game from scratch, I found a chess game on Github, and implemented my own AI. My primary work is therefor in the Computer.py file, however I have tweaked the code in many places.
***
### Chess Piece


The ChessPiece class is an abstract class and it is used as a parent for every piece. It consists of a method for moves filtering (prevent illegal moves like exposing the king) and some methods to keep the previous state of the chess piece intact (required by the ai when calling unmake_move()). Every chess piece is equipped with a get_score() function that is used when evaluating the board. The scores are 10 points for the pawns, 20 for knights, 30 for bishops and rooks, 240 for the queen and 1000 for the king.
***
### Computer


The Computer class is a static class and it is used to get a move from the computer. There is a method that returns a random move and a method that returns an ai move using the minimax alogirthm.
***
### AI


The minimax algorithm starts by making every possible (valid) move, and for each one of those moves, it simulates the opponents move that it's in their best interest. Note that since the goal of the game is not to "eat" the king, but instead "trap" him, the computer assumes that the player can make illegal moves. This is a recursive algorithm that stops when there are no more moves available, or the board is terminal.
***
### Logging
By setting log=True in the board constructor parameters, the Logger.py script will produce a .txt file that contains the minimax tree of the current ai move decision. 
#### For example in the following state 

![Screenshot_1](https://user-images.githubusercontent.com/41242107/160127591-6a6e230d-197f-4f91-996e-e2458fc4ad6a.png)

#### The AI will evaluate higher these moves (depth=1)

![Screenshot_22](https://user-images.githubusercontent.com/41242107/160127841-130a9b12-2474-4bce-b399-d410e68217ca.png)

#### The following .txt file will be produced

![Screenshot_4](https://user-images.githubusercontent.com/41242107/160128011-16c2cee9-a9a2-4e33-8908-7b2100d3af63.png)

#### You can clearly see the evaluation of 240 points by killing the queen and the evaluation of 10 points by killing the pawn.
Make sure to open the .txt file using a jetbrains ide (i.e. pycharm) in order to view the board properly due to inconsistencies in the sizes of the unicode characters.

[Chess assets by John Pablok CC-BY-SA 3.0](https://opengameart.org/content/chess-pieces-and-board-squares)
