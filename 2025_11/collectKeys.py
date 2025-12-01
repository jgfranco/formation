# /*
# '''
# Today, you will be given the problem to collect keys.

# You are moving out the office and need to collect everyone's keys before they leave. Unfortunately, everyone has different schedules so you can't just collect all the keys at once. You want to visit the office as few times as possible to collect everyone's keys.

# Given a [[Int]] representing people's schedules, return the least number of times you'll need to visit to collect keys.
 

# EXAMPLE(S)
# [[10, 16], [2, 8], [1, 6], [7, 12]]

# Should return 2. You could visit at 6 and then at 10 to collect all the keys.
 
# 24hr time 
'''
  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
                    ____________________ 
    ____________                
  __________ 
              ____________________
            *.       *

bucket 1
10 - 12

bucket 2
2 - 6


    entrance  = 7
    exit = 12


visits = 2
   
                            t
# [[1, 6], [2, 8] [7, 12], [10, 16]]            $  

    if entrance is  -1:
        increment visits
        entrance = entrance t
        exit = exit of t
        continue


    if entrance of t is smaller thant prev exit 
         continue
    else: # reset (start a new bucket)
        increment visits
        entrance = entrance t
        exit = exit of t
        continue

    
    max of both entrances (prv an curr)
    min of both exits 

    r
return visits


sort by entrance 

traverse schedules



return the number of bucket
'''
# FUNCTION SIGNATURE
# func minVisits(schedule: [[Int]]) -> Int
# '''
# */
# /*
# '''
# Today, you will be given the problem to collect keys.

# You are moving out the office and need to collect everyone's keys before they leave. Unfortunately, everyone has different schedules so you can't just collect all the keys at once. You want to visit the office as few times as possible to collect everyone's keys.

# Given a [[Int]] representing people's schedules, return the least number of times you'll need to visit to collect keys.
 

# EXAMPLE(S)
# [[10, 16], [2, 8], [1, 6], [7, 12]]

# Should return 2. You could visit at 6 and then at 10 to collect all the keys.
 

# FUNCTION SIGNATURE
# func minVisits(schedule: [[Int]]) -> Int
# '''
# */

def minVisits(schedule):

    entrance = -1
    exit = -1
    visits = 0
    # sort

    schedule = sorted(schedule, key = lambda x:x[0])

    #print(schedule)


    for ent, ex in schedule:

        if entrance == -1 or ent > exit:
            visits += 1
            entrance = ent 
            exit = ex
        else:
            entrance = max(entrance, ent)
            exit = min(exit, ex)

    
    return visits

print(minVisits([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(minVisits([[10, 16], [2, 8], [1, 6]]))

print(minVisits([[1, 6], [2, 8], [7, 12], [14, 16], [21, 25]]))


"""

[[10, 16], [2, 8], [1, 6], [7, 12]] => 2
[[1, 6], [2, 8], [7, 12], [14, 16], [21, 25]] => 4

"""



def collect_keys(schedules):
    # sort the schedules in ascending order by the start time
    schedules.sort(key=lambda x: x[0])

    # initialize the number of visits to the office
    num_visits = 0

    # initialize the end time of the previous schedule
    prev_end = 0

    # for each schedule
    for schedule in schedules:
        # if the start time of the schedule is before the end time of the previous schedule, then we don't need to visit the office again
        if schedule[0] <= prev_end:
            continue

        # otherwise, we need to visit the office again
        num_visits += 1

        # update the end time of the previous schedule
        prev_end = schedule[1]

    # return the total number of visits to the office
    return num_visits