# About this project

On July 2021, as I was having dinner with some dear friends, we were discussing how nice and useful it is to know about data structures and algorithms. As it happenned, we were all developers and as the dinner went on we agreed that it would be fun to start a coding community where we could work on coding challenges, share our results, discuss, teach and feedback each other. In this repository I will be uploading and updating my solutions to such exercises, implemented with Python. 

The added challenge on each of these exercises was to try to arrive at a solution that was as small as possible in time and space complexity. On each code file there are comments specifying my estimations on this matter. 

## Installation

Clone this repository, configure a virtual environment inside the cloned directory, install the required packages specified in the requirements.txt file and install setup.py with the following commands on your terminal.

```
$ git clone https://github.com/cemar-ortiz/coding_challenges
$ cd coding_challenges
$ python 3 -m venv venv
$ source venv/bin/activate
$ pip install -e .
$ pip install -r requirements.txt
```


## Testing the solutions

In the `tests` directory you can find the test files used to develop each of the solutions. To use pytest to test the solutions you need to make sure you followed the above installation instructions before (pytest won't be able to import the challenges module if you don't)

Tests can be run using pytest with:

```
$ pytest tests/<test_x.py>
```

Replace `test_x.py` with the test you're interested in running.

## Sources used for the challenges

- McDowell, G. L. (2015). Cracking the coding interview: 189 programming questions and solutions (p. 687). CareerCup, LLC.
