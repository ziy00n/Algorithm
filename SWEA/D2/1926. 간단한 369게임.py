n = int(input())

# 받은 n을 1부터 나열
# 3,6,9 가 들어갈 땐 - 로 표시
# 35 -> '-' , 36 -> '--'

for i in range(1, n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        clap_cnt = str(i).count('3') +  str(i).count('6') + str(i).count('9')
        print('-' * clap_cnt, end =' ')
    else:
        print(i, end =' ')