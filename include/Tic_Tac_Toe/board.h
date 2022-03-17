#pragma once

#include <vector>
#include <string>
#include <ostream>

class Board{
    private:
        std::vector<int> board;
    public:
        Board();

        explicit Board(std::string& board_s);

        std::string to_string();

        int to_table_value();

        void empty_board();

        std::vector<int> get_board();

        bool is_valid(int position);

        bool enter_input(int position, int input);

        bool is_empty();

        friend std::ostream& operator<<(std::ostream& os, Board& board);
};