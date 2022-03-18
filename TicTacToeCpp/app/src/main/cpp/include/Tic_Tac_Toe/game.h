#pragma once

#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/q_player.h"
#include <string>
#include <memory>

class Game{
    private:
        const std::string board_null_error_msg = "FATAL ERROR. The board is null.";
        std::shared_ptr<Board> board = nullptr;
        std::unique_ptr<Player> player_X = nullptr;
        std::unique_ptr<Player> player_O = nullptr;
        std::unique_ptr<QPlayer> q_player_train_X = nullptr;
        std::unique_ptr<QPlayer> q_player_train_O = nullptr;
        std::unique_ptr<RandomPlayer> helper_random_player = nullptr;

    public:

        enum class GameState{
            Draw, Ongoing, XWon, OWon
        };

        Game();

        explicit Game(std::unique_ptr<Player>& player_one, std::unique_ptr<Player>& player_two);

        explicit Game(std::string& board_s);

        void reset_game();

        GameState game_state();

        GameState play();

        int make_move(int human_turn, int position);

        friend bool operator==(const Game::GameState& gameState, const Player::PlayerSymbol& symbol);

        void train_Qplayer_X();

        void train_Qplayer_O();

        void train_loop(int n);
};