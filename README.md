# Deep Dives in Testing

This repo contains some code I generated for lesson challenges while teaching loops and exceptions in Python. Testing beginner code is an unusual case, since quite often one's tests need to inspect the structure of the code itself, as well as it's output. 

For instance, testing whether or not a student has used the correct type of loop to solve a challenge is a case that would seldom come up in a production environment. It turns out that Python makes this easy though!

There are three useful snippets of code to be found in `src.py`:

1. `uses_statement()`, which tests accepts a function and a statment (from the `ast` library!) and checks whether or not the function contains an instance of that statement.
1. `uses_nesting()`, which tests accepts a function and a statment (from the `ast` library!) and checks whether or not the function contains **nested instances** of that statement.
1. `BreakingMock()`, which will deliver a specified list of outputs in order, and then generate an exception. This is useful for checking whether or not a given loop terminates when it should. I originally created this mock to check whether or not students had chosen correct boolean expressions for their `while` loops, but in fact it is useful in a number of applications! An example is included here, in which a `BreakingMock` tests whether or not a simple guessing game has been correctly coded to quit on command.