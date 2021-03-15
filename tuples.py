#!/usr/bin/env python 3.7

# tuples are immutable

point = (2.0, 3.0)
# point [0] = 1 - DOES NOT WORK 

point_3d = point + (4.0,) # must add comma to distinguish between tuple and float/int

# point_3d >>> (2.0, 3.0, 4.0)

x, y, z = point_3d

# x =2.0 , y=3.0, 4.0
# python 2.0 can use tuples to formate strings ...


#
