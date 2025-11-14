


   

          
  

def final_dominos_state(dominosRow: list[str]):
  
    def helper(start, end):

        if dominosRow[start] == "R" and dominosRow[end] == "L":
            while start < end:
                dominosRow[start] = "R"
                dominosRow[end] = "L"
                start +=1
                end -=1
        elif dominosRow[start] == "R" and dominosRow[end] == "R":
            while start < end:
                dominosRow[start] = "R"
                start +=1

        elif dominosRow[start] == "L" and dominosRow[end] == "L":
            while start < end:
                dominosRow[start] = "L"
                start +=1

    if len(dominosRow)<2: return dominosRow

    dominosRow = ['L'] + dominosRow + ['R']

    slow = 0
    fast = 1

    while fast < len(dominosRow):
        while dominosRow[fast] == ".": 
            fast += 1

        helper(slow, fast)

        slow = fast
        fast += 1
    
    return dominosRow[1:len(dominosRow)-1]




print(final_dominos_state(['.']) == ['.'])
print(final_dominos_state(['R']) == ['R']) 
print(final_dominos_state(['L']) == ['L']) 
print(final_dominos_state(['.', 'L', '.', 'R', '.']) == ['L', 'L', '.', 'R', 'R']) # ['L', 'L', '.', 'R', 'R']
print(final_dominos_state(['.', 'R', '.', '.', 'L', '.']) == ['.', 'R', 'R', 'L', 'L', '.'])  
print(final_dominos_state(['.', 'R', '.', 'L', '.', 'L', '.', 'R', '.']) == ['.', 'R', '.', 'L', 'L', 'L', '.', 'R', 'R'])
print(final_dominos_state(['.', 'R', '.', '.', '.', 'L', '.']) == ['.', 'R', 'R', '.', 'L', 'L', '.']) 
print(final_dominos_state(['R', '.', '.', '.', '.', '.', '.', '.']) == ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'])
print(final_dominos_state(['L', '.', '.', '.', '.', '.', '.', '.']) == ['L', '.', '.', '.', '.', '.', '.', '.'])
print(final_dominos_state(['.', '.', '.', '.', '.', '.', '.', 'R']) == ['.', '.', '.', '.', '.', '.', '.', 'R'])
print(final_dominos_state(['.', '.', '.', '.', '.', '.', '.', 'L']) == ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'])
print(final_dominos_state(['.', '.', '.', '.', '.', '.', '.']) == ['.', '.', '.', '.', '.', '.', '.'])
print(final_dominos_state(['.', 'L', '.', '.', '.', 'R', '.']) == ['L', 'L', '.', '.', '.', 'R', 'R'])
print(final_dominos_state(['.', 'R', '.', '.', '.', '.', 'L', '.']) == ['.', 'R', 'R', 'R', 'L', 'L', 'L', '.'])
print(final_dominos_state(['.', 'L', '.', '.', '.', '.', 'R', '.']) == ['L', 'L', '.', '.', '.', '.', 'R', 'R'])