#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/helper_functions.h"
#include <memory>
#include <vector>
#include <iostream>

Game::Game(std::unique_ptr<Player>& player_one, std::unique_ptr<Player>& player_two){
    this->board = std::make_unique<Board>();
    this->player_one = std::move(player_one);
    this->player_two = std::move(player_two);
}

void Game::reset_game() {
    if(this->board){
        this->board->empty_board();
    }else{
        throw std::runtime_error(board_null_error_msg);
    }
}

Winner Game::game_end(){
    Winner winner = Winner::Ongoing;
    if(this->board){
        std::vector<int> board_v = this->board->get_board();

        winner = decide_winner(board_v);

    }else{
        throw std::runtime_error(board_null_error_msg);
    }
    return winner;
}

Winner Game::play(){
    Winner winner = Winner::Ongoing;
    int input = 0;

    if(!this->board){
        throw std::runtime_error(board_null_error_msg);
    }

    std::cout << *(this->board) << std::endl;

    while(winner == Winner::Ongoing){
        do{
            input = player_one->play(this->board);
        }while(!board->enter_input(input, Const::X_VALUE));

        std::cout << *(this->board) << std::endl;

        winner = game_end();
        if(winner != Winner::Ongoing){
            break;
        }

        do{
            input = player_two->play(this->board);
        }while(!board->enter_input(input, Const::O_VALUE));

        std::cout << *(this->board) << std::endl;
        winner = game_end();
    }

    this->reset_game();

    return winner;
}