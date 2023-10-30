# 풀이 참고..

N = int(input())  # 보드의 크기
board = [list(map(int, input().split())) for _ in range(N)]  # 보드 상태

# 동적 프로그래밍 테이블 초기화
# dp[i][r][c]는 파이프 방향 i (0: 가로, 1: 대각선, 2: 세로)으로 위치 (r, c)에 파이프를 놓을 수 있는 경우의 수를 저장
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

# 1행 초기화 - 파이프를 이동시키는 경우, 가로 방향의 파이프만 가능
dp[0][0][1] = 1
for i in range(2, N):
    # (3) 과정: 1행에서 파이프를 이동시킬 때, 현재 칸의 왼쪽이 비어있을 때만 경우의 수를 누적
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

# 나머지 행, 열 처리
for r in range(1, N):
    for c in range(1, N):
        # 대각선 파이프 추가 과정
        if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
            # (5) 과정: 대각선 파이프를 추가할 때, 현재 칸과 그 주변 두 칸이 모두 비어 있어야
            # 이전 행의 대각선, 가로, 세로 파이프의 경우의 수를 합산하여 현재 위치의 대각선 파이프 경우의 수를 계산
            dp[1][r][c] = dp[0][r - 1][c - 1] + \
                dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        # 가로, 세로 파이프 추가 과정
        if board[r][c] == 0:
            # (4) 과정: 가로 파이프를 추가할 때, 현재 칸의 왼쪽 칸의 가로 파이프와 대각선 파이프의 경우의 수를 합산
            dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]

            # (4) 과정: 세로 파이프를 추가할 때, 현재 칸의 위쪽 칸의 세로 파이프와 대각선 파이프의 경우의 수를 합산
            dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

# 최종 결과 출력 - 모든 경우의 수를 합산하여 출력
print(sum(dp[i][N - 1][N - 1] for i in range(3)))


# # 0 → ─, 1 → /, 2 → |

# def solution():

#     # 1행 미리 처리하기 → (3) 과정
#     dp[0][0][1] = 1
#     for i in range(2, N):
#         if board[0][i] == 0:
#             dp[0][0][i] = dp[0][0][i - 1]

#     # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
#     for r in range(1, N):
#         for c in range(1, N):
#             # (5) 과정
#             # 대각선 파이프를 추가하는 과정
#             if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
#                 dp[1][r][c] = dp[0][r - 1][c - 1] + \
#                     dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

#             # 가로, 세로 파이프를 추가하는 과정
#             if board[r][c] == 0:
#                 dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
#                 dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

#     # 최종 결과 출력
#     print(sum(dp[i][N - 1][N - 1] for i in range(3)))


# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# solution()
