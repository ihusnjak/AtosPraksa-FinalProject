#pragma once

#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/constants.h"

class MinMaxPlayer: public Player{
    private:
        int evaluate(std::vector<int>& board);
        int iterate(std::vector<int>& board, int score, int depth, bool is_max, const int move);
        int minmax(std::vector<int>& board, int depth, bool is_max);
    public:
        explicit MinMaxPlayer(Player::PlayerSymbol symbol);

        int play(std::shared_ptr<Board> board) override;
};