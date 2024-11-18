x=int(input())
attendence=input().replace(" ", "")
max_absent_days = len(max(attendence.split('1'), key=len))
print(max_absent_days)
