def solution(brown, yellow):
    total = brown + yellow
    for row in range(1, total + 1):
        if (total % row) == 0:
            column = total // row
            # 왜 4를 더해줄까?
            # 2 * row + 2 * column을 하게 되면 약 끝 모서리 쪽이 겹치게 되는데 이 네 부분을 +4를 해줘야 같다.
            if (column >= row) and (2 * row + 2 * column) == brown + 4:
                return [column, row]
