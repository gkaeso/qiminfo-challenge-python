QimInfo Challenge
-----------------

Python solution to the QimInfo challenge.

_______________

## Objective

For a given list of coins displaying either heads or tails,
the program must return the minimum number of swaps to make
in order to have the longest possible head / tails sequence.

The input coin sequence will be a list of zeros and ones.

    eg. [0, 1, 0, 1, 1]

There are two possible ways of swapping the coins:
    
    eg. [0, 1, 0, 1, 0] (swapped only one coin, the last one)
    or  [1, 0, 1, 0 ,1] (swapped all coins excet the last one)

The program should thus return: 

    1

Only one swap is needed to make it the longest possible.

_______________

## Usage

Requires Python 3.9.


List input is given directly in the main function.

_______________

## License

This repository uses the [MIT License](/LICENSE).
