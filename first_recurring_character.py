# Find the first recurring character in an array
# Given an array = [2,5,1,2,3,5,1,2,4]
# Return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# Return 1

# Given an array = [2,3,4,5]
# Return None

    # CITATION: https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12314730#questions/9591304
    # CITATION: by user Jake
    # //Naive solution 
    # //Time Complexity: O(n^2)
    # const FirstRecurringChar = (array) => {
    #   //Loop throuh array outer array to increment index by 1 and inner array to decrement index by 1
    #   for (let i=1;i<array.length;i++)
    #   {
    #     for (let j=i-1;j>=0;j--)
    #     {
    #       if (array[i] === array[j])
    #         return array[i]
    #     }
    #   }
    #   return undefined
    # }
     
    # FirstRecurringChar([2,3,4,5])

def first_recurring_character(arr):
    history = {}

    # loop through all the characters in 'arr'
    for i in range(0, len(arr)):
        # check if key in history
        if arr[i] in history:
            # if it IS in history, we have found a recurring character - so return
            return arr[i]
        else:
            # if it is NOT in history, add it
            history[arr[i]] = i

    # we have not found anything, thus return 'None'
    return None

    

print(first_recurring_character([2,5,1,2,3,5,1,2,4]))

print(first_recurring_character([2,1,1,2,3,5,1,2,4]))

print(first_recurring_character([2,3,4,5]))

print(first_recurring_character([2]))