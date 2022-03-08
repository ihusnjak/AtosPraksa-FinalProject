#pragma once
#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/player.h"
#include <string>
#include <memory>

class Game{
    private:
        const std::string board_null_error_msg = "FATAL ERROR. The board is null.";
        std::shared_ptr<Board> board = nullptr;
        std::unique_ptr<Player> player_one = nullptr;
        std::unique_ptr<Player> player_two = nullptr;

    public:
        Game(std::unique_ptr<Player>& player_one, std::unique_ptr<Player>& player_two);

        void reset_game();

        Winner game_end();

        Winner play();

};