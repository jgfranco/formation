
'''
Today, you will be given the problem to collect keys.

You are moving out the office and need to collect everyone's keys before they leave. Unfortunately, everyone has different schedules so you can't just collect all the keys at once. You want to visit the office as few times as possible to collect everyone's keys.

Given a [[Int]] representing people's schedules, return the least number of times you'll need to visit to collect keys.
 

EXAMPLE(S)
[[10, 16], [2, 8], [1, 6], [7, 12]]

Should return 2. You could visit at 6 and then at 10 to collect all the keys.
 

FUNCTION SIGNATURE
func minVisits(schedule: [[Int]]) -> Int

[1, 6] 
  [2, 8] 
      [7,12]
         [10, 16]

prev end time: 6
ret 2

time complexity: o(n)
space complexity: o(1)

psuedo code:

def minVisits(schedule):
    prev_endtime
    ret = 1
    sort schedue by end time

    for range i+1 in schedules:
        if prev_end_time < schedules[i][0]:
            ret += 1
            prev_endtime = scheules[i][1]
        else:
    
    return ret

ret: 2
prev_endtime = 12

'''

def minVisits(schedule):
    schedule = sorted(schedule, key=lambda x: x[-1])
    ret = 1
    prev_endtime = schedule[0][1]

    #for i in range(1, )
    for i in range(1,len(schedule)):
        if prev_endtime < schedule[i][0]:
            ret+= 1
            prev_endtime = schedule[i][1]
        
    return ret

schedule = [[10,16],[2,8],[1,6],[7,12]]
#[[10, 16], [2, 8], [1, 6], [7, 12]] => 2
#[[1, 6], [2, 8], [7, 12], [14, 16], [21, 25]] => 4
schedule2 = [[1, 6], [2, 8], [7, 12], [14, 16], [21, 25]]
print(minVisits(schedule2))


# Formation's solution 
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