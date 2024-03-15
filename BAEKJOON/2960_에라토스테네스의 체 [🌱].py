# 백준 2960 에라토스테네스의 체 
# 에라토스테네스의 체 : 소수 찾는 알고리즘
# -🌱 풀이 참고 🌱-

N, K = map(int,input().split())

# 2부터 N의 지움여부: arr[2] ~ arr[N]
arr = [False] * (N+1) # 지우지 않은 수: False, 지운 수 : True

cnt = 0
for i in range(2, N+1): # 2 ~ N 까지에 대해
    if arr[i] == False: # i가 지우지 않은 숫자면 
        # 자신을 포함한 배수에 True로 변경(값 지움)
        for j in range(i, N+1, i): 
            if arr[j] == False:
                arr[j] = True
                cnt += 1 # 값 지울 때마다 +1
                if cnt == K: # K번째에 지워진 숫자 출력
                    print(j)