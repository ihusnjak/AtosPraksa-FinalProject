#include "Tic_Tac_Toe/player.h"

Player::PlayerSymbol Player::get_symbol(){
    return this->symbol;
}

Player::Player(Player::PlayerSymbol symbol) {
    this->symbol = symbol;
}
