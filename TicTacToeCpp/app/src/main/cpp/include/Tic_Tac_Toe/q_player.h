#pragma once

#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/Qtable.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/random_player.h"
#include <memory>
#include <vector>
#include <string>

class QPlayer: public Player{
    private:
        std::shared_ptr<QTable> table;
        std::shared_ptr<std::vector<int>> game_history;
        std::shared_ptr<std::vector<float>> empty_Qvalues_template = std::make_shared<std::vector<float>>(Const::N_FIELDS, Const::Q_DEFAULT_VALUE);
        std::unique_ptr<RandomPlayer> helper_random_player;
    public:
        explicit QPlayer(Player::PlayerSymbol symbol);

        int play(std::shared_ptr<Board> board) override;

        int train(std::shared_ptr<Board> board);

        void update_table(std::shared_ptr<Board> board);

        std::string policy_filename();

        void save_table();

        void load_table();
};