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
        std::unique_ptr<Player> player_X = nullptr;
        std::unique_ptr<Player> player_O = nullptr;

    public:

        enum class GameState{
            Draw, Ongoing, XWon, OWon
        };

        Game();

        Game(std::unique_ptr<Player>& player_one, std::unique_ptr<Player>& player_two);

        void reset_game();

        GameState game_state();

        GameState play();

        friend bool operator==(const Game::GameState& gameState, const Player::PlayerSymbol& symbol);

        int make_move(int move);
};