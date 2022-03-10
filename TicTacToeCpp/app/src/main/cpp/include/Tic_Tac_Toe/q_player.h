#pragma once

#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/Qtable.h"
#include <memory>

class QPlayer: public Player{
    private:
        std::shared_ptr<QTable> table;
    public:
        QPlayer(Player::PlayerSymbol symbol);
        int play(std::shared_ptr<Board> board) override;
};