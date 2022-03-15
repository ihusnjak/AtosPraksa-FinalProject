#include "Tic_Tac_Toe/q_player.h"
#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/helper_functions.h"
#include <memory>
#include <vector>
#include <algorithm>
#include <string>

int QPlayer::play(std::shared_ptr<Board> board){
    int board_value, move;
    float max = -1.0;

    board_value = board->to_table_value();

    if(!table->key_exists(board_value)){
        table->add_key_value(board_value, *empty_Qvalues_template);

    }
    std::shared_ptr<std::vector<float>> Qvalues = table->get_values(board_value);

    for (int i = 1; i <= Const::N_FIELDS; i++) {
        if (board->is_valid(i) && Qvalues->at(i - 1) > max) {
            max = Qvalues->at(i - 1);

            //if QPlayer is not sure about his move, play something random
            if(max > Const::CUTOFF_Q_VALUE){
                move = i;
            }else{
                do {
                    move = helper_random_player->play(board);
                }while(!board->is_valid(move));
            }
        }
    }

    return move;
}

int QPlayer::train(std::shared_ptr<Board> board) {
    int board_value, move;
    board_value = board->to_table_value();

    move = play(board);

    game_history->push_back(board_value);
    game_history->push_back(move);

    return move;
}

void QPlayer::update_table(std::shared_ptr<Board> board) {
    float reward, max = -1;
    std::vector<int> board_v;
    Game::GameState state;
    std::shared_ptr<std::vector<float>> Qvalues;
    int board_value, Q_index;

    board_v = board->get_board();
    state = decide_game_state(board_v);

    if(state == Game::GameState::Draw){
        reward = Const::Q_DRAW_REWARD;
    }else if(state == symbol){
        reward = Const::Q_WIN_REWARD;
    }else{
        reward = Const::Q_LOSE_REWARD;
    }

    for(int i = game_history->size() - 1; i > 1 ; i-=2){
        board_value = game_history->at(i-1);
        Q_index = game_history->at(i) - 1;
        Qvalues = table->get_values(board_value);
        if(max < 0){
            Qvalues->at(Q_index) = reward;
        }else{
            Qvalues->at(Q_index) = (1-Const::Q_LEARNING_RATE)*Qvalues->at(Q_index) +
                                            Const::Q_LEARNING_RATE*Const::Q_DISCOUNT_RATE*max;
        }

        table->add_key_value(board_value, *Qvalues);

        max = *std::max_element(Qvalues->begin(), Qvalues->end());
    }

    game_history->clear();
}

std::string QPlayer::policy_filename() {
    std::string filename;
    if(symbol == Player::PlayerSymbol::X){
        filename = Const::POLICY_PATH_X;
    }else{
        filename = Const::POLICY_PATH_O;
    }

    return filename;
}

void QPlayer::save_table() {
    table->save_table(policy_filename());
}

void QPlayer::load_table() {
    table->load_table(policy_filename());
}

QPlayer::QPlayer(Player::PlayerSymbol symbol):Player(symbol) {
    table = std::make_shared<QTable>();
    try{
        load_table();
    }catch(std::exception& e){}
    game_history = std::make_shared<std::vector<int>>();
    helper_random_player = std::make_unique<RandomPlayer>(symbol);
}