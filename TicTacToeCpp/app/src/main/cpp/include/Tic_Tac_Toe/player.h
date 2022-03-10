#pragma once

#include "Tic_Tac_Toe/board.h"
#include <memory>

class Player{
    public:
        enum class PlayerSymbol{
            X, O
        };

    protected:
        PlayerSymbol symbol;

    public:
        explicit Player(PlayerSymbol symbol);

        virtual int play(std::shared_ptr<Board> board)=0;

        PlayerSymbol get_symbol();
};