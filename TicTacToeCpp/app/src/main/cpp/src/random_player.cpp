#include "Tic_Tac_Toe/random_player.h"
#include "Tic_Tac_Toe/constants.h"

int RandomPlayer::play(std::shared_ptr<Board> board) {
    int position = 1;

    if(distribution){
        position = (*distribution)(*generator);
    }

    return position;
}

RandomPlayer::RandomPlayer(Player::PlayerSymbol symbol):Player(symbol) {
    distribution = std::make_unique<std::uniform_int_distribution<int>>(Const::MIN_POSITION,Const::N_FIELDS);
    rd = std::make_unique<std::random_device>();
    generator = std::make_unique<std::mt19937>(rd->operator()());
}