T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)]

    num = 1
    y, x = 0, 0 # 현재 위치
    dir = 0 # 0:우,1:하,2:좌,3:상

    # 우->하->좌->상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while num <= n*n:

        # 1. 정상범위 2.다른 숫자 저장되어있지 않으면 -> 저장
        if 0 <= y < n and 0 <= x < n and board[y][x] == 0:
            board[y][x] = num
            num += 1
            
        # 이동한 위치가 좌표 범위 넘어가면
        else:
            # 이동했던 위치 이전으로 돌리기
            y -= dy[dir]
            x -= dx[dir]

            # 방향 변경
            dir = (dir + 1) % 4
        
        # 다음으로 좌표 이동
        y += dy[dir]
        x += dx[dir]

    print(f'#{tc}')
    for row in board:
        print(*row)
