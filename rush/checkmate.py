def checkmate(board):
    n = len(board)
    board = [list(row) for row in board]

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

    x, y = king_pos

    # Directions for Bishop and Queen (diagonals)
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Directions for Rook and Queen (straight lines)
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check for Pawns attacking
    pawn_dirs = [(-1, -1), (-1, 1)]  # Only from above (assuming enemy pawns move downward)
    for dx, dy in pawn_dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'P':
            print("Success")
            return

    # Check for Bishop or Queen
    for dx, dy in diagonals:
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < n:
            cell = board[nx][ny]
            if cell == '.':
                nx += dx
                ny += dy
                continue
            elif cell == 'B' or cell == 'Q':
                print("Success")
                return
            else:
                break

    # Check for Rook or Queen
    for dx, dy in straight:
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < n:
            cell = board[nx][ny]
            if cell == '.':
                nx += dx
                ny += dy
                continue
            elif cell == 'R' or cell == 'Q':
                print("Success")
                return
            else:
                break

    print("Fail")
