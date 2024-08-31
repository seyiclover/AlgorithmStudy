class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 행렬의 크기: m은 행의 수, n은 열의 수
        m, n = len(mat), len(mat[0])

        # 결과를 저장할 리스트
        result = []

        # 각 대각선을 임시로 저장할 리스트
        intermediate = []

        # 총 m + n - 1개의 대각선이 존재함
        for d in range(m + n - 1):
            # 새로운 대각선을 위해 임시 리스트 초기화
            intermediate.clear()
            
            # 대각선의 시작점 설정
            # r은 행의 인덱스, c는 열의 인덱스
            # 행 인덱스 r: d가 n보다 작은 경우 0에서 시작, 큰 경우 d-n+1에서 시작
            r = 0 if d < n else d - n + 1
            # 열 인덱스 c: d가 n보다 작은 경우 d에서 시작, 큰 경우 n-1에서 시작
            c = d if d < n else n - 1

            # 대각선의 요소를 추출하여 intermediate 리스트에 추가
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1  # 행 증가 (아래로 이동)
                c -= 1  # 열 감소 (왼쪽으로 이동)

            # 짝수 번째 대각선은 뒤집어서 추가, 홀수 번째 대각선은 그대로 추가
            if d % 2 == 0:
                result.extend(intermediate[::-1])  # 리스트를 뒤집어서 추가
            else:
                result.extend(intermediate)  # 그대로 추가

        # 최종 결과 반환
        return result
