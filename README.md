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