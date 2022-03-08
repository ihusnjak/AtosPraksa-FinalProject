#include "Tic_Tac_Toe/q_player.h"

int QPlayer::play(std::shared_ptr<Board> board){
    //TODO: IMPLEMENT Q LEARNING
    return 0;
}

QPlayer::QPlayer():Player() {
    table = std::make_shared<QTable>();
}