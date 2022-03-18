#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/constants.h"
#include <iostream>
#include <sstream>

int HumanPlayer::play(std::shared_ptr<Board> board) {
    int input;
    try{
        std::cin >> input;
    }catch (std::exception& e){
        throw std::runtime_error("Please enter an integer!");
    }

    if (input < 1 || input > Const::N_FIELDS){
        std::stringstream stream;
        stream << "Please input a number in range 1 to " << Const::N_FIELDS << " inclusive.";
        throw std::runtime_error(stream.str());
    }

    return input;
}

HumanPlayer::HumanPlayer(Player::PlayerSymbol symbol) : Player(symbol) {}

