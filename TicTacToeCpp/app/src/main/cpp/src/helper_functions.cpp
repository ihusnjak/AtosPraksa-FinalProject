#include "Tic_Tac_Toe/helper_functions.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/game.h"
#include <algorithm>
#include <functional>
#include <cmath>

Game::GameState draw(std::vector<int>& board){
    Game::GameState winner = Game::GameState::Draw;
    bool is_full = true;
    if (std::find(board.begin(), board.end(), Const::EMPTY_VALUE) != board.end()) {
        is_full = false;
    }

    if(!is_full){
        winner = Game::GameState::Ongoing;
    }

    return winner;
}

Game::GameState winning_row(std::vector<int>& board){
    Game::GameState winner = Game::GameState::Ongoing;
    int temp = 0;
    for(int i = 0; i < Const::N_FIELDS; i+=Const::N_ROW_COLUMN){
        if (std::adjacent_find(board.begin()+i, board.begin()+i+Const::N_ROW_COLUMN, std::not_equal_to<>() ) == board.begin()+i+Const::N_ROW_COLUMN){
            temp = *(board.begin()+i);
            if(temp == Const::X_VALUE){
                winner = Game::GameState::XWon;
            }else if(temp == Const::O_VALUE){
                winner = Game::GameState::OWon;
            }
        }
    }
    return winner;
}

Game::GameState winning_column(std::vector<int>& board){
    std::vector<int> temp;
    //transpose the matrix and then find winning rows
    for(int n = 0; n<Const::N_FIELDS; n++) {
        int i = n / Const::N_ROW_COLUMN;
        int j = n % Const::N_ROW_COLUMN;
        temp.push_back(board[Const::N_ROW_COLUMN*j + i]);
    }
    return winning_row(temp);
}

Game::GameState winning_diagonal(std::vector<int>& board){
    Game::GameState winner = Game::GameState::Ongoing;
    int first_diagonal = 0;
    int second_diagonal = 0;

    for(int i = 0; i < Const::N_ROW_COLUMN; i++){
        first_diagonal += board.at(i*Const::N_ROW_COLUMN + i);
        second_diagonal += board.at((i+1)*Const::N_ROW_COLUMN-1 - i);
    }

    if(abs(second_diagonal) == Const::N_ROW_COLUMN){
        first_diagonal = second_diagonal;
    }

    switch(first_diagonal){
        case Const::N_ROW_COLUMN:
            winner = Game::GameState::XWon;
            break;
        case -Const::N_ROW_COLUMN:
            winner = Game::GameState::OWon;
            break;
        default:
            winner = Game::GameState::Ongoing;
            break;
    }

    return winner;
}

Game::GameState decide_game_state(std::vector<int>& board){
    Game::GameState winner = Game::GameState::Ongoing;
    std::vector<Game::GameState> possible_wins = {winning_row(board), winning_diagonal(board), winning_column(board), draw(board)};

    for(auto& win : possible_wins){
        if(win != Game::GameState::Ongoing){
            return win;
        }
    }

    return winner;
}