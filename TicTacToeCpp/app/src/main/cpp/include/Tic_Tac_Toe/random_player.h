#pragma once

#include "Tic_Tac_Toe/player.h"
#include <random>
#include <memory>

class RandomPlayer: public Player{
    private:
        std::unique_ptr<std::random_device> rd = nullptr;
        std::unique_ptr<std::mt19937> generator = nullptr;
        std::unique_ptr<std::uniform_int_distribution<int>> distribution = nullptr;
    public:
        explicit RandomPlayer(Player::PlayerSymbol symbol);

        int play(std::shared_ptr<Board> board) override;
};