#include "Tic_Tac_Toe/human_player.h"
#include <iostream>

int HumanPlayer::play() {
    int input;
    try{
        std::cin >> input;
    }catch (std::exception& e){
        throw std::runtime_error("Please enter an integer!");
    }

    if (input < 1 || input > 9){
        throw std::runtime_error("Please input a number in range 1 to 9 inclusive.");
    }

    return input;
}

HumanPlayer::HumanPlayer() : Player() {}

