"""There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

 

Example 1:

Input: seats = [3,1,5], students = [2,7,4]
Output: 4
Explanation: The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

"""

class Solution(object):
    def minMovesToSeat(self, seats, students):

        max_val = max(max(seats),max(students))

        count_seat = [0] * (max_val+1)
        count_student = [0] * (max_val+1)

        for i in seats:
            count_seat [i] += 1
        for j in students:
            count_student [j] += 1

        res = i = j = 0
        remaining_students = len(students)
        # print(count_seat,count_student)
        while remaining_students > 0:
            if count_seat[i] == 0:
                i+=1
            if count_student[j] == 0:
                j+=1
            if count_seat[i] and count_student[j]:
                res += abs(i-j)
                remaining_students -= 1
                count_seat[i] -= 1
                count_student[j] -= 1
                # print(res,remaining_students,count_seat,count_student)
        return res

obj = Solution()

print(obj.minMovesToSeat(seats = [3,1,5], students = [2,7,4]))