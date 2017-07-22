/**
 * 
 * @param {* a 2-d array representation of 3x3 board} board 
 */
const evaluateBoard = (board) => {
    for(let i=0;i<3;i++){
        if(board[i][0]===board[i][1]&&board[i][0]===board[i][2]){
            if(board[i][0]==='o')
                return 10;
            else if(board[i][0]==='x')
                return -10;
        }
    }
    for(let i=0;i<3;i++){
        if(board[0][i]===board[1][i]&&board[0][i]===board[2][i]){
            if(board[i][0]==='o')
                return 10;
            else if(board[i][0]==='x')
                return -10;
        }
    }
    if(board[0][0]===board[1][1] && board[0][0]===board[2][2]){
            if(board[0][0]==='o')
                return 10;
            else if(board[0][0]==='x')
                return -10;
    }

    if(board[0][2]===board[1][1] && board[0][2]===board[2][0]){
            if(board[0][2]==='o')
                return 10;
            else if(board[0][2]==='x')
                return -10;
    }
    return 0;
}

const test = () => {
    const board = [
        ['x','_','x'],
        ['_','x','o'],
        ['_','_','x']
    ]
    console.log(evaluateBoard(board));
}

test();
module.exports  = evaluateBoard;