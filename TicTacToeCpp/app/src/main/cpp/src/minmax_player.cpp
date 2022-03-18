#include "Tic_Tac_Toe/minmax_player.h"
#include "Tic_Tac_Toe/helper_functions.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/game.h"
#include <cmath>
#include <algorithm>

int MinMaxPlayer::evaluate(std::vector<int>& board) {
    Game::GameState winner = decide_game_state(board);
    int eval = 0;

    if(winner == this->symbol){
        eval = Const::MIN_MAX_REWARD;
    }else{
        eval = -Const::MIN_MAX_REWARD;
    }

    return eval;
}

int MinMaxPlayer::iterate(std::vector<int>& board, int score, int depth, bool is_max, const int move){
    for(int i = 0; i < board.size(); i++){
        if(board.at(i) == Const::EMPTY_VALUE){
            board.at(i) = move;

            if(is_max){
                score = std::max(score, minmax(board, depth+1, !is_max));
            }else{
                score = std::min(score, minmax(board, depth+1, !is_max));
            }


            board.at(i) = Const::EMPTY_VALUE;
        }
    }
    return score;
}

int MinMaxPlayer::minmax(std::vector<int>& board, int depth, bool is_max) {
    int score = evaluate(board);
    bool terminate = false;

    if(abs(score) == Const::MIN_MAX_REWARD){
        terminate = true;
    }else{
        if(decide_game_state(board) == Game::GameState::Draw){
            terminate = true;
        }
    }

    if(!terminate){
        if(is_max){
            score = Const::MAXIMIZER_MIN_VALUE;
            score = iterate(board, score, depth, is_max, Const::X_VALUE);
        }else{
            score = Const::MINIMIZER_MAX_VALUE;
            score = iterate(board, score, depth, is_max, Const::O_VALUE);
        }
    }

    return score;
}

int MinMaxPlayer::play(std::shared_ptr<Board> board) {
    int move = 0;
    int best_value = Const::MAXIMIZER_MIN_VALUE;
    int value = 0;
    std::vector<int> board_v = board->get_board();

    for(int i = 0; i < board_v.size(); i++){
        if(board_v.at(i) == Const::EMPTY_VALUE){
            board_v.at(i) = this->symbol == Player::PlayerSymbol::X ? Const::X_VALUE : Const::O_VALUE;

            value = minmax(board_v, 0, false);

            board_v.at(i) = Const::EMPTY_VALUE;

            if(value > best_value){
                best_value = value;
                move = i+1;
            }
        }
    }

    return move;
}

MinMaxPlayer::MinMaxPlayer(Player::PlayerSymbol symbol): Player(symbol){}