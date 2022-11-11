# CS111, lecture 27 -- Python tracing, debugging, and dataclasses

def sum_list(nums: list) -> float:
    running_total = 0   # set up name in directory with value 0
    for num in nums:  # num is a new name to refer to list elts in turn
        # add each num to running_total in turn
        running_total = running_total + num
    return(running_total)

# to see how the code runs, you can put a breakpoint (red dot) next
# to the next line then debug the file. VSCode will stop before it
# runs the next line. You can then use the debugger controls to
# step through the function and watch (a) how the directory updates
# and (b) the order in which the lines are executed
result1 = sum_list([9, 4, 1, 8])

# write a function that takes a list of strings and counts how many
# contain the letter 'z' 
# in Python, can write strings as "z" or 'z'
def count_zs(words: list) -> int:
    '''return number of words containing z'''
    # set up a running total with the answer if the list is empty
    running_total = 0
    # use for to go through the list, updating the total as needed
    for w in words:
        if 'z' in w:
            running_total = running_total + 1
        # no else needed because don't want to change running_total in that case
    return(running_total)

# instead of counting z-words, let's gather up a list of them
def get_z_words(words: list) -> list:
    ''' return list of words containing z'''
    # set up a running list with the answer if the list is empty
    z_words = []  # [] is empty list
    # use for to go through the list, updating the answer list as needed
    for w in words:
        if 'z' in w:
            z_words.append(w)  # add w to the list of z_words
    return(z_words)

# For more practice with seeing how code runs and the directory changes,
# try stepping through (with the debugger) the following computation

get_z_words(["bear", "pizza", "zebra", "coffee"])

# to check your understanding of return and indentation, change the
# indentation of the return(z_words) at the end of get_z_words and
# see how that changes the result

# --------------------------------------------------------------------

# want to make a data block for Ed post, each with the name of
# the poster, the number of likes, and the post content

from dataclasses import dataclass
@dataclass
class Post:
    by: str
    num_likes: int
    content: str

p1 = Post("andrew", 0, "project out")

# in the debugging console, we ran the following line several times
# to see how the number of likes in p1 changes
#    p1.num_likes = p1.num_likes + 1
# if you reload the file, p1 resets to its original value

# a line in case you want a place to put a breakpoint for entering
# the debugging console
pass