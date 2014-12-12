# Unbeatable Tic-Tac-Toe AI using Minimax
Because Tic-Tac-Toe has a finite, relatively small number of possiblities, a computer can compute each possibility and thus not lose.

Update (10/7/14): made `check_win()` recursive. more generalizable, but way slower. I can implement alpha-beta pruning to speed it up.

Update (12/11/14): added 'choose-first' pruning and alpha-beta pruning

## How to play
Open the directory containing the file in Terminal, then type `python game.py`.

### 'Choose-first' pruning
The nature of tic-tac-toe is that there are only 3 end-states: win, lose, or tie. All wins have the same value. Same with losses. (e.g. In football, I could win with 14 points, or I could win with 21 points. In tic-tac-toe, all wins have the same value.)

For the Minimax algorithm, this means that when it finds a win, it is extraneous to search further for more ways to win.

So, the way I implemented 'choose-first' pruning, if the computer finds a win (whose value equals the best possible outcome), it stops looking at the other board states.

If there were multiple win values, it would be less likely that when the computer finds a win, it would stop searching the other board states, because that win would not likely be the best possible outcome. 

If wins had different values, then the computer wouldn't prune as much as it does here, and the algorithm would behave more like regular Minimax instead of Minimax with pruning.

### Alpha-beta pruning
In regular alpha-beta pruning, a node/board state compares its values to those of the parent node. If these values are favorable, the computer doesn't need to look further for additional nodes and their values.

## My learning process
Thank goodness for the internet. A Google search turns up tic-tac-toe AI using Python, but I did not look at these sites. I did, however, [read a blog post on using an algorithm called Minimax for a game involving matches](http://callmesaint.com/python-minimax-tutorial/). I also watched a bunch of MIT OpenCourseWare videos on [Minimax](https://www.youtube.com/watch?v=STjW3eH0Cik), [alpha-beta pruning](https://www.youtube.com/watch?v=hM2EAvMkhtk), and [recursion in programming](https://www.youtube.com/watch?v=WbWb0u8bJrU).

I also watched some videos on [Depth-First](https://www.youtube.com/watch?v=AfSk24UTFS8) [Search](https://www.youtube.com/watch?v=zLZhSSXAwxI), but I did not need to use this technique.

Thank you internet!

## Stops and starts
I first started by writing out the Tic-Tac-Toe game from a Player's point-of-view (see `try1.py`). I neatly ordered various bits of code into classes. But when it came time to write my computer AI, my way of choosing the square to X or O became cumbersome.

I learned how to do Minimax by hand, which seemed intuitive enough. My plan was to write out the tree as an object, have it retain state throughout the game, and pare it down as the game progressed. This proved complicated (see `notes from first try.txt`)

I then realized that a path within the tree may be of variable length, if the win condition is met before all the moves are exhausted. This characteristic lends itself to using recursion.

I was overwhelmed by the complexity of creating the tree using recursion. So, I took a step back and really tried understanding the implementation of the algorithm [in the matches game](http://callmesaint.com/python-minimax-tutorial/).

I worked through that implementation of the algorithm by hand, effectively using paper and my brain as the interpreter. This helped a lot. I tried using [Philip Guo's interpreter visualizer](http://pythontutor.com/), but I didn't understand the visualization immediately and intuitively.

I then 'ported' the implementation of the algorithm from the matches game to work with Tic-Tac-Toe. I started with `move_helper()`, then wrote everything else to work with that.

Debugging was interesting. What helped most was to 'interpret' my function using paper and my brain, and also having a separate sheet of paper where I implemented the algorithm by hand.