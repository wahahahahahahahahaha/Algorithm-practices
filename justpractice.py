n, m = map(int, input().split())

required = set(map(int, input().split()))

students = {}

# 第一部分：记录学生选课
for _ in range(n):
    student_id, course_id = map(int, input().split())

    if student_id not in students:
        students[student_id] = set()

    students[student_id].add(course_id)


# 第二部分：找出符合条件的学生
result = []

for student_id, courses in students.items():

    # TODO 1：初始化判断标志
    flag=True
    # TODO 2：遍历所有必修课程，
    # 判断学生是否缺少某门必修课程
    for course in required:
        if course not in courses:
            flag=False
        break
    # TODO 3：如果符合要求，
    # 将学号添加到 result
    if flag:
        result.append(student_id)


# 第三部分：输出结果

# TODO 4：将 result 按升序排序
result.sort()
# TODO 5：如果 result 为空，输出 -1
# 否则逐行输出所有符合条件的学号
if result == None:
    print(-1)
else: 
    print(result)