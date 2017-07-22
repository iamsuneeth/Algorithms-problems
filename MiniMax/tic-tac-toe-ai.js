function Move(x,y){
	this.row = x, 
    this.col = y;
};

const player = 'o', opponent = 'x';


const isMovesLeft = (board) => {
	for (let i = 0; i<3; i++)
		for (let j = 0; j<3; j++)
			if (board[i][j]=='_')
				return true;
	return false;
}

const isMovesLeft2 = (board) => {
	for (let i = 0; i<9; i++){
		if (board[i]=='_')
			return true;
	}		
	return false;
}

const evaluate = (b) =>{
	for (let row = 0; row<3; row++)
	{
		if (b[row][0]==b[row][1] &&
			b[row][1]==b[row][2])
		{
			if (b[row][0]==player)
				return +10;
			else if (b[row][0]==opponent)
				return -10;
		}
	}

	for (let col = 0; col<3; col++)
	{
		if (b[0][col]==b[1][col] &&
			b[1][col]==b[2][col])
		{
			if (b[0][col]==player)
				return +10;

			else if (b[0][col]==opponent)
				return -10;
		}
	}

	if (b[0][0]==b[1][1] && b[1][1]==b[2][2])
	{
		if (b[0][0]==player)
			return +10;
		else if (b[0][0]==opponent)
			return -10;
	}

	if (b[0][2]==b[1][1] && b[1][1]==b[2][0])
	{
		if (b[0][2]==player)
			return +10;
		else if (b[0][2]==opponent)
			return -10;
	}

	return 0;
}

const printBoard = (board) => {
	for(let i=0;i<9;i+=3){
		console.log(`${board[i]} ${board[i+1]} ${board[i+2]}`);
	}
	console.log('\n');
}

const evaluate2 = (b) =>{
	for (let row = 0; row<9; row+=3)
	{
		if (b[row]==b[row+1] &&
			b[row+1]==b[row+2])
		{
			if (b[row]==player)
				return +10;
			else if (b[row]==opponent)
				return -10;
		}
	}

	for (let col = 0; col<3; col++)
	{
		if (b[col]==b[col+3] &&
			b[col+3]==b[col+6])
		{
			if (b[col]==player)
				return +10;

			else if (b[col]==opponent)
				return -10;
		}
	}

	if (b[0]==b[4] && b[4]==b[8])
	{
		if (b[0]==player)
			return +10;
		else if (b[0]==opponent)
			return -10;
	}

	if (b[2]==b[4] && b[4]==b[6])
	{
		if (b[2]==player)
			return +10;
		else if (b[2]==opponent)
			return -10;
	}

	return 0;
}

const minimax = (board , depth, isMax) => {
	let score = evaluate(board);

	if (score == 10)
		return score;

	if (score == -10)
		return score;

	if (isMovesLeft(board)==false)
		return 0;

	if (isMax)
	{
		let best = -1000;

		for (let i = 0; i<3; i++)
		{
			for (let j = 0; j<3; j++)
			{
				if (board[i][j]=='_')
				{
					board[i][j] = player;


					best = Math.max( best,
						minimax(board, depth+1, !isMax) );

					board[i][j] = '_';
				}
			}
		}
		return best;
	}

	else
	{
		let best = 1000;

		// Traverse all cells
		for (let i = 0; i<3; i++)
		{
			for (let j = 0; j<3; j++)
			{

				if (board[i][j]=='_')
				{
					board[i][j] = opponent;

					best = Math.min(best,
						minimax(board, depth+1, !isMax));
					board[i][j] = '_';
				}
			}
		}
		return best;
	}
}



const minimax2 = (board , depth, isMax) => {
	let score = evaluate2(board);

	if (score == 10)
		return score;

	if (score == -10)
		return score;

	if (isMovesLeft2(board)==false)
		return 0;

	if (isMax)
	{
		let best = -1000;

		for (let i = 0; i<9; i++)
		{
				if (board[i]=='_')
				{
					board[i] = player;


					best = Math.max( best,
						minimax2(board, depth+1, !isMax) );

					board[i] = '_';
				}

		}
		return best;
	}

	else
	{
		let best = 1000;

		for (let i = 0; i<9; i++)
		{


				if (board[i]=='_')
				{
					board[i] = opponent;

					best = Math.min(best,
						minimax2(board, depth+1, !isMax));
					board[i] = '_';
				}
		}
		return best;
	}
}

const findBestMove = (board) =>{
	let bestVal = -1000;
	let bestMove = new Move(-1,-1);

	for (let i = 0; i<3; i++)
	{
		for (let j = 0; j<3; j++)
		{
			if (board[i][j]=='_')
			{
				board[i][j] = player;

				let moveVal = minimax(board, 0, false);

				board[i][j] = '_';

				if (moveVal > bestVal)
				{
					bestMove.row = i;
					bestMove.col = j;
					bestVal = moveVal;
				}
			}
		}
	}


	return bestMove;
}

const findBestMove2 = (board) =>{
	let bestVal = -1000;
	let bestMove = -1;

	for (let i = 0; i<9; i++)
	{

			if (board[i]=='_')
			{
				board[i] = player;

				let moveVal = minimax2(board, 0, false);

				board[i]= '_';

				if (moveVal > bestVal)
				{
					bestMove = i
					bestVal = moveVal;
				}
			}

	}


	return bestMove;
}


const test = () => {
    const board = [['x','_','_'],
                   ['_','_','_'],
                   ['_','_','_']];
	const board2 = ['x','_','_',
                   '_','_','_',
                   '_','_','_'];
    console.log(findBestMove(board));
	console.log(findBestMove2(board2));
}

test();