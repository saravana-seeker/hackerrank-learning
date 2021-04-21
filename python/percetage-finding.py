if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    out=student_marks[query_name]
    sumof=0
    for i in out:
        sumof=sumof+i
        avg=sumof/len(out)
    print('%.2f' % avg)
   

    