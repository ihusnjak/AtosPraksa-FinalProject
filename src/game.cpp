#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/helper_functions.h"
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/random_player.h"
#include <memory>
#include <vector>
#include <iostream>

Game::Game(std::unique_ptr<Player>& player_one, std::unique_ptr<Player>& player_two){
    this->board = std::make_unique<Board>();

    if(player_one->get_symbol() == player_two->get_symbol()){
        throw std::runtime_error("We cannot have two X or two O players!");
    }

    if(player_two->get_symbol() == Player::PlayerSymbol::X){
        this->player_X = std::move(player_two);
        this->player_O = std::move(player_one);
    }else {
        this->player_X = std::move(player_one);
        this->player_O = std::move(player_two);
    }
}

Game::Game(){
    this->board = std::make_unique<Board>();
    this->player_X = std::make_unique<HumanPlayer>(Player::PlayerSymbol::X);
    this->player_O = std::make_unique<RandomPlayer>(Player::PlayerSymbol::O);
}

void Game::reset_game() {
    if(this->board){
        this->board->empty_board();
    }else{
        throw std::runtime_error(board_null_error_msg);
    }
}

Game::GameState Game::game_state(){
    GameState state = GameState::Ongoing;
    if(this->board){
        std::vector<int> board_v = this->board->get_board();

        state = decide_game_state(board_v);

    }else{
        throw std::runtime_error(board_null_error_msg);
    }
    return state;
}

Game::GameState Game::play(){
    GameState state = GameState::Ongoing;
    int input = 0;

    if(!this->board){
        throw std::runtime_error(board_null_error_msg);
    }

    std::cout << *(this->board) << std::endl;

    while(state == GameState::Ongoing){
        do{
            input = player_X->play(this->board);
        }while(!board->enter_input(input, Const::X_VALUE));

        std::cout << *(this->board) << std::endl;

        state = game_state();
        if(state != GameState::Ongoing){
            break;
        }

        do{
            input = player_O->play(this->board);
        }while(!board->enter_input(input, Const::O_VALUE));

        std::cout << *(this->board) << std::endl;
        state = game_state();
    }

    this->reset_game();

    return state;
}

bool operator==(const Game::GameState& gameState, const Player::PlayerSymbol& symbol){
    bool equals = false;

    bool X_played_and_won = (symbol == Player::PlayerSymbol::X && gameState == Game::GameState::XWon);
    bool O_played_and_won = (symbol == Player::PlayerSymbol::O && gameState == Game::GameState::OWon);

    equals = X_played_and_won || O_played_and_won;

    return equals;
}

int Game::make_move(int move) {
    //TODO IMPLEMENT MOVE BY MOVE GAME
    return 0;
}