#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/helper_functions.h"
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/random_player.h"
#include "Tic_Tac_Toe/q_player.h"
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
    this->helper_random_player = std::make_unique<RandomPlayer>(Player::PlayerSymbol::X);
}

Game::Game(std::string &board_s) {
    this->board = std::make_unique<Board>(board_s);
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

int Game::make_move(int human_turn, int position) {
    int result;
    int machine_move = 0;
    Game::GameState state;

    Player::PlayerSymbol machine_symbol;
    int first_move, second_move;

    if(human_turn == Const::HUMAN_PLAYS_FIRST_SIGNAL){
        machine_symbol = Player::PlayerSymbol::O;
        first_move = Const::X_VALUE;
        second_move = Const::O_VALUE;
    }else{
        machine_symbol = Player::PlayerSymbol::X;
        first_move = Const::O_VALUE;
        second_move = Const::X_VALUE;
    }

    std::unique_ptr<Player> Qplayer(new QPlayer(machine_symbol));

    state = game_state();

    if(!board->is_valid(position)){
        result = Const::ERROR_SIGNAL;

    }else if(state == GameState::Ongoing){

        if(human_turn == Const::HUMAN_PLAYS_FIRST_SIGNAL || !board->is_empty()) {
            board->enter_input(position, first_move);
        }

        state = game_state();

        if(state == GameState::Ongoing){
            machine_move = Qplayer->play(board);
            board->enter_input(machine_move, second_move);
        }
    }

    if(result != Const::ERROR_SIGNAL){
        state = game_state();

        switch (state) {
            case GameState::XWon:
                result = Const::X_WON_SIGNAL;
                break;
            case GameState::OWon:
                result = Const::O_WON_SIGNAL;
                break;
            case GameState::Draw:
                result = Const::DRAW_SIGNAL;
                break;
            default:
                result = Const::ONGOING_SIGNAL;
                break;
        }

        result = result * (Const::N_FIELDS+1) + machine_move;

    }

    std::cout << board->to_string() << std::endl;

    return result;
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

void Game::train_Qplayer_X() {
    if(!q_player_train_X){
        q_player_train_X = std::make_unique<QPlayer>(Player::PlayerSymbol::X);
    }

    GameState state = GameState::Ongoing;
    int input = 0;

    if(!this->board){
        throw std::runtime_error(board_null_error_msg);
    }

    while(state == GameState::Ongoing){
        do{
            input = q_player_train_X->train(this->board);
        }while(!board->enter_input(input, Const::X_VALUE));

        state = game_state();
        if(state != GameState::Ongoing){
            break;
        }

        do{
            input = helper_random_player->play(this->board);
        }while(!board->enter_input(input, Const::O_VALUE));

        state = game_state();
    }

    q_player_train_X->update_table(board);

    this->reset_game();
}

void Game::train_Qplayer_O() {
    if(!q_player_train_O){
        q_player_train_O = std::make_unique<QPlayer>(Player::PlayerSymbol::O);
    }

    GameState state = GameState::Ongoing;
    int input = 0;

    if(!this->board){
        throw std::runtime_error(board_null_error_msg);
    }

    while(state == GameState::Ongoing){
        do{
            input = helper_random_player->play(this->board);
        }while(!board->enter_input(input, Const::X_VALUE));

        state = game_state();
        if(state != GameState::Ongoing){
            break;
        }

        do{
            input = q_player_train_O->train(this->board);
        }while(!board->enter_input(input, Const::O_VALUE));

        state = game_state();
    }

    q_player_train_O->update_table(board);

    this->reset_game();
}

void Game::train_loop(int n) {
    for(int i = 0; i < n; i++){
        train_Qplayer_X();
        train_Qplayer_O();
    }
    q_player_train_X->save_table();
    q_player_train_O->save_table();
}
