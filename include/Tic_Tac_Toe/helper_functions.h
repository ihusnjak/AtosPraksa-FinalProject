#pragma once

#include "Tic_Tac_Toe/constants.h"
#include <vector>

Winner winning_row(std::vector<int>& board);

Winner winning_column(std::vector<int>& board);

Winner winning_diagonal(std::vector<int>& board);

Winner draw(std::vector<int>& board);

Winner decide_winner(std::vector<int>& board);