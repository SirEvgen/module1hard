grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades0 = round(sum(grades[0]) / len(grades[0]))
grades1 = round(sum(grades[1]) / len(grades[1]))
grades2 = round(sum(grades[2]) / len(grades[2]))
grades3 = round(sum(grades[3]) / len(grades[3]))
grades4 = round(sum(grades[4]) / len(grades[4]))
grades_sum = [[grades0], [grades1],[grades2],[grades3],[grades4]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'])
ball = ([students[0], grades_sum[0]], [students[1], grades_sum[1]], [students[2], grades_sum[2]], [students[3], grades_sum[3]],[students[4], grades_sum[4]])
ball = sorted(ball)
ball = dict(ball)
print(ball)
# В задании не было сказано округлять, но я подумал, что так будет красивее
