# ESCHER part

This part is mostly about Matrix, geometry and math.

## History
>A total of 15 puzzles left in due time by Lord Escher, separate you from the biggest treasure on this and all nearby islands.
>Do you have enough courage and wits to go the whole way and not give up? 
>Many have attempted to do this, but very few have managed. One thing’s for sure, none of those who went on this trip have returned the same.

## Tasks
1. [**Compass, Map and Spyglass**](./3_pathfinding.py) - task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass), ('M' - map), ('S' - spyglass) from your starting position. So the result will be the sum of distance from Y to C, from Y to M and from Y to S (not Y-C-M-S).
>Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction). Your starting position is 'Y'.
2. [**The Stone Wall**](./4_find_thinnest_column.py) - task is to find the index of the place where the wall is the narrowest (as shown at the picture below). The width of the wall is the height of the columns of the array (multiline string). If there are several such places, return the index of leftmost. Index starts from 0. 
3. [**Wild Dogs**](./5_geometry.py) - As input you’ll be given the coordinates of the dogs. Your task is to find the distance to the nearest point from which you can kill the maximum number of animals with one shot (any number of dogs on the same line can be killed with one shot).
Your starting position is the point (0, 0).
If the calculated distance is an integer, returned it as int, otherwise it rounded to 2 decimal places.
*It can not be situation when a few dogs on the line is behind your back (dog dog you dog) - there no such situation in the tests.*
$$![example of geometry map](../media/escher_1.png)$$