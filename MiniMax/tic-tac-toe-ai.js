const Move = (x, y) => {
    this.x = x;
    this.y = y;
}

const miniMax = (board, depth, isMax) => {

    let result = evaluateBoard(board);
    if (result === 1)
        return result;
    if (result === -1)
        return result;
    if (!isMoveLeft(board))
        return 0;

    if (isMax) {
        let best = 10000;
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                if (board[i][j] === '_') {
                    board[i][j] = 'x';
                    best = Math.max(best, miniMax(board, 0, !isMax));
                    board[i][j] = '_';
                }
            }

        }
        return best;
    }else {
        let best = -10000;
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                if (board[i][j] === '_') {
                    board[i][j] = 'x';
                    best = Math.min(best, miniMax(board, 0, !isMax));
                    board[i][j] = '_';
                }
            }

        }
        return best;
    }

}

const findBestMove = (board, player) => {
    let bestval = -10000;
    let bestMove = new Move(-1, -1);
    let i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (board[i][j] === '_') {
                board[i][j] = player ? 'x' : 'o';
                val = miniMax(board, 0, !player);
                board[i][j] = '_';
                if (val > bestval) {
                    bestval = val;
                    bestMove.x = i;
                    bestMove.y = j;
                }
            }
        }

    }

    return bestMove;

}