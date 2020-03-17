# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

from graph import Graph

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


# connected - has edges, connected components
# array/2d - graph
# n,s,e,w - edges
# binary
# island/1 islands - connected components

# return 1 islands - number of connected components


width = len(isalnds[1])
height = len(isalnds)

def island_counter(islands):
  #create our Graph
  # Iterate through our islands list
  #for each element check to see if there 
  for row in islands:
    for col in islands:
      space = islands[row][col]
      

def check_neighbors(row, col):
  # Check the left
  left_idx = col - 1
  if left_idx >= 0 and islands[row][left_idx] == 1:
    # Add to the stack/queue
    pass
  # Check the right
  right_idx = col + 1
  if right_idx < width and islands[row][right_idx] == 1:
    # Add to the stack/queue
    pass
  # Check top
  top_idx = row - 1
  if top_idx >= 0 and islands[top_idx][col] == 1:
    # Add to the stack/queue
    pass
  # Check bottom
  bot_idx = row + 1
  if bot_idx < height and islands[bot_idx][col] == 1:
    # Add to the stack/queue
    pass