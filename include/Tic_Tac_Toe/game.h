#pragma once
#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/constants.h"
#include "player.h"
#include <string>

class Game{
    private:
        const std::string board_null_error_msg = "FATAL ERROR. The board is null.";
        Board* board = nullptr;
        Player* player_one = nullptr;
        Player* player_two = nullptr;

    public:
        Game(Player* player_one, Player* player_two);

        void reset_game();

        Winner game_end();

        Winner play();

};