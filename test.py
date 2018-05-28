import math
class PIECES:
    X = 1
    O = -1
    N = 0
class MOVES:
    ILLEGAL = 0
    COMPLETE = 2


def move(piece, inner_i, inner_j, i, j, entire_board):

    # Current board is one of the 9 inner boards.
    current_board = entire_board[3*i + j]

    # check if the move made is illegal
    if current_board.place(piece, inner_i, inner_j) == MOVES.ILLEGAL:
        return MOVES.ILLEGAL

    else:
        # The entire board is inactive after a move is made
        for zi in range(0,3):
            for zj in range(0,3):
                entire_board[3*zi + zj].active = False

        # If the future tile is captured by either X or O (1 or -1) assign all uncaptured tiles to active tiles
        if entire_board[3*inner_i + inner_j].captured:
            for z in range(0,9):
                if not entire_board[z].captured:
                    entire_board[z].active = True
        # future tile is the new active tile
        else:

            entire_board[3*inner_i + inner_j].active = True

        # Calculate if the entire board is captured by any piece
        c = False
        c += entire_board[0 + j].captured == entire_board[3 + j].captured == entire_board[6 + j].captured
        c += entire_board[3*i].captured == entire_board[3*i + 1].captured == entire_board[3*i + 2].captured
        c += entire_board[0].captured == entire_board[4].captured == entire_board[7].captured
        c += entire_board[6].captured == entire_board[4].captured == entire_board[2].captured

        # return the piece that captures it if board is won
        if c:
            return piece
        # default : return signal that a move was completed
        return MOVES.COMPLETE


class Board:
    # b.place(PIECES.X, 0, 0) places a piece in 'b' in top left corner
    def place(self, piece, i, j):
        # if the current board is active and the position in the board is vacant, proceed
        if self.active and self.board[3*i + j] == PIECES.N:

            # place the piece
            self.board[3*i + j] = piece

            # check if board is captured
            c = False
            c += self.board[0 + j] == self.board[3 + j] == self.board[6 + j]
            c += self.board[3*i] == self.board[3*i + 1] == self.board[3*i + 2]
            c += self.board[0] == self.board[4] == self.board[7]
            c += self.board[6] == self.board[4] == self.board[2]

            # switch captured status of board
            if c:
                self.captured = piece
                self.active = False
            return MOVES.COMPLETE
        # the board is inactive, disallow move
        return MOVES.ILLEGAL

    # copy constructor, alternatively use 'copy.deepcopy' library
    def copy(self):
        return Board(self.active, self.board, self.captured)

    # initialize board
    def __init__(self, active = True, board = 9 * [PIECES.N], captured = PIECES.N):
        self.active = active
        self.board = list(board)
        self.captured = captured


def display(entire_board):
    print " _____________________________"
    # iterate 9 rows, cols
    for row in range(0,9):
        cur = ""
        for col in range(0,9):

            # find position of inner box accordingly
            i = int(row/3)
            j = int(col/3)
            inneri = row%3
            innerj = col%3

            current_piece = entire_board[i*3 + j].board[inneri*3 + innerj]
            current_active = entire_board[i*3 + j].active

            if col == 0:
                cur += "|"
            cur += {
            PIECES.X : {False : " X ", True : " X "},
            PIECES.O : {False : " O ", True : " O "},
            PIECES.N : {False : " _ ", True : "|_|"}
            }[current_piece][current_active]
            if col%3 == 2:
                cur += "|"
        print cur
        if row%3 == 2:
            print "|_________|_________|_________|"


def viable_boards(entire_board):
    temp_list = []
    for b in entire_board:
        if b.active:
            temp_list.append(b)

def test_move(i, j, board, it):
    cur_piece = {0 : PIECES.X, 1: PIECES.O}[it[1]%2]
    move(cur_piece, i%3, j%3, int(i/3), int(j/3), board)
    it[1] += 1
    display(board)

boards = [Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board()]
#def ALPHA_BETA_AI(entire_board):
#    for vboard in viable_boards(entire_board):
it = {1:0}
# sample run
test_move(4,4,boards,it)
test_move(4,5,boards,it)
test_move(4,7,boards,it)
test_move(3,3,boards,it)
test_move(1,1,boards,it)
test_move(5,4,boards,it)
test_move(7,4,boards,it)
test_move(4,3,boards,it)
test_move(4,1,boards,it)
test_move(5,3,boards,it)
test_move(7,1,boards,it)
