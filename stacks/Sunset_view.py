#Compute Buidings with a SunSet View
"""
Time Complexity O(n) and Space O(n)
"""


import collections
from typing import Iterator, List

"""
East --> West
Building's height in List from East --> West
"""
def examine_buildings_with_subset(sequence: Iterator[int])->List[int]:
    
    SunSet_buildings=[]
    h_idx = -1 #height index
    i=0
    while i<len(sequence) and h_idx<len(sequence):
        while SunSet_buildings and SunSet_buildings[-1] <= sequence[i] and h_idx>=0:
            SunSet_buildings.pop()
            h_idx-=1
        
        SunSet_buildings.append(sequence[i])
        h_idx+=1
        i+=1
    
    #Return Height SunSet_buildings from East to West and len() returns the number of buildings
    return SunSet_buildings


"""
To return the positions of the building means we also need to index
"""
def examine_buildings_with_subset_idx(sequence: Iterator[int])->List[int]: 
    building_with_height = collections.namedtuple('BuildingWithHeight',
                                                  ('id', 'height'))
    SunSet_buildings: List[building_with_height] = []
    h_idx = -1 #height index
    i=0
    while i<len(sequence) and h_idx<len(sequence):
        while SunSet_buildings and SunSet_buildings[-1].height <= sequence[i] and h_idx>=0:
            SunSet_buildings.pop()
            h_idx-=1    
        
        SunSet_buildings.append(building_with_height(i, sequence[i]))
        h_idx+=1
        i+=1
    
    #Return SunSet_buildings indices from East to West 
    return [s.id for s in SunSet_buildings]

print("Building positions/ids: ",examine_buildings_with_subset_idx([3,2,5,4,6,3,2]))

print("Building heights: ",examine_buildings_with_subset([3,2,5,4,6,3,2]))

"""
West --> East
Building's height in List from West --> East
Sun is on the left
"""
def examine_buildings_with_subset_left(sequence: Iterator[int])->List[int]: 
    building_with_height = collections.namedtuple('BuildingWithHeight',
                                                  ('id', 'height'))
    
    SunSet_buildings: List[building_with_height] = []
    SunSet_buildings.append(building_with_height(0,sequence[0]))
    h_idx = 1 #height index
    i=1
    while i<len(sequence):
        while SunSet_buildings[-1].height < sequence[i] and h_idx>=0:
            SunSet_buildings.append(building_with_height(i,sequence[i]))
            h_idx+=1
        i+=1
    
    #Return SunSet_buildings indices from West to East (left to right) 
    return [s.id for s in SunSet_buildings]

print("Building positions/ids",examine_buildings_with_subset_left([7,4,8,2,9]))
print("Building positions/ids",examine_buildings_with_subset_left([2,3,4,5]))
