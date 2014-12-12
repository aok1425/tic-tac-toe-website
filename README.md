# Tic-tac-toe using Minimax
[https://blooming-cove-8013.herokuapp.com](https://blooming-cove-8013.herokuapp.com)

* Now with alpha-beta pruning and memoization!
* It doesn't choose the quickest way to win, but in those instances, it still wins. That's because when faced with multiple choices with the same eventual outcome, the program just chooses the most recent choice. It doesn't know how many steps it takes to get to the outcome.

## CSS
* Input `type = image` doesn’t allow you to change CSS, so have to use `type=button` ([link](http://stackoverflow.com/questions/195632/how-to-change-an-input-button-image-using-css))
* Using button, the circle has a background. if i play around w CSS more, i can remove that background, resize circle, and recenter it.

## Lessons learned
* Tests are my friend. When I was scared that a code change would break my function, having a test that I could easily call was very helpful, and sped up coding time significantly.
* When faced with a large, complex problem, find the simplest possible version of it. When my function works on that simple version, try it on increasingly more complex versions.

## Possible feature additions
* Can add feature to have computer go first
* To have the computer choose the fastest way to win, I could have it do the first winning set of moves that it sees. Implementing this is facilitated by the fact that there is only one win value, so the computer can stop at the first win it sees. I have already implemented this on my [non-node, non-memoization version of the algorithm](https://github.com/aok1425/tic-tac-toe).