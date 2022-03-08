#pragma once
#include "Tic_Tac_Toe/board.h"
#include <memory>

class Player{
    public:
        explicit Player();

        virtual int play(std::shared_ptr<Board> board)=0;
};