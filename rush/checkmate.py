def checkmate(board_str):
    board = [list(row) for row in board_str.strip().split('\n')]
    n = len(board)

    # Find King position
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    if (
        is_threatened_by_pawn(board, king_pos) or
        is_threatened_by_bishop(board, king_pos) or
        is_threatened_by_rook(board, king_pos) or
        is_threatened_by_queen(board, king_pos)
    ):
        print("Success")
    else:
        print("Fail")


def is_threatened_by_pawn(board, king_pos):
    x, y = king_pos
    directions = [(-1, -1), (-1, 1)]  # enemy pawns move upward
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny] == 'P':
                return True
    return False


def is_threatened_by_bishop(board, king_pos):
    return check_directions(board, king_pos, [(-1,-1), (-1,1), (1,-1), (1,1)], ['B'])


def is_threatened_by_rook(board, king_pos):
    return check_directions(board, king_pos, [(-1,0), (1,0), (0,-1), (0,1)], ['R'])


def is_threatened_by_queen(board, king_pos):
    return check_directions(
        board,
        king_pos,
        [(-1,-1), (-1,1), (1,-1), (1,1), (-1,0), (1,0), (0,-1), (0,1)],
        ['Q']
    )


def check_directions(board, start, directions, threatening_pieces):
    n = len(board)
    for dx, dy in directions:
        x, y = start
        while True:
            x += dx
            y += dy
            if not (0 <= x < n and 0 <= y < n):
                break
            square = board[x][y]
            if square == '.':
                continue
            if square in threatening_pieces:
                return True
            break  # blocked by other piece
    return False
