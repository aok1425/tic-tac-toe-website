<<<<<<< HEAD
# Tic-tac-toe using Minimax
[https://blooming-cove-8013.herokuapp.com](https://blooming-cove-8013.herokuapp.com)

* Now with alpha-beta pruning and memoization!
* It doesn't choose the quickest way to win, but in those instances, it still wins. That's because when faced with multiple choices with the same eventual outcome, the program just chooses the most recent choice. It doesn't know how many steps it takes to get to the outcome.

## CSS
* Input `type = image` doesn’t allow you to change CSS, so have to use type=button [http://stackoverflow.com/questions/195632/how-to-change-an-input-button-image-using-css](www.google.com)
* Using button, the circle has a background. if i play around w CSS more, i can remove that background, resize circle, and recenter it.

## Lessons learned
* Tests are my friend. When I was scared that a code change would break my function, having a test that I could easily call was very helpful, and sped up coding time significantly.
* When faced with a large, complex problem, find the simplest possible version of it. When my function works on that simple version, try it on increasingly more complex versions.

## Possible feature additions
* Can add feature to have computer go first
* To have the computer choose the fastest way to win, I could do 2 things:

  1. Keep track of the number of steps to reach each leaf node/final move. When the node/board state in question is faced with multiple next moves with the same end result, have it choose the next move with the fewest steps.

  2. Implement breadth-first search. Instead of going from left to right, breadth-first search would go from top to bottom.
=======
# Unbeatable Tic-Tac-Toe AI using Minimax

Because Tic-Tac-Toe has a finite, relatively small number of possiblities (9!, or 362,880), a computer can compute each possibility and thus not lose.

## How to play
Open the directory containing the file in Terminal, then type `python game.py`.

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

## Next steps
Implement alpha-beta pruning!
>>>>>>> 88f26b5bfc88e0631c7f56f7b3f4a6c605e6b21f
