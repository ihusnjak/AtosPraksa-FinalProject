#pragma once

#include "Tic_Tac_Toe/game.h"
#include <vector>

Game::GameState winning_row(std::vector<int>& board);

Game::GameState winning_column(std::vector<int>& board);

Game::GameState winning_diagonal(std::vector<int>& board);

Game::GameState draw(std::vector<int>& board);

Game::GameState decide_game_state(std::vector<int>& board);