#pragma once

#include "Tic_Tac_Toe/player.h"

class HumanPlayer: public Player{
    public:
        explicit HumanPlayer();
        int play(std::shared_ptr<Board> board) override;
};