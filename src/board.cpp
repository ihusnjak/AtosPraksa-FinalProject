#include "Tic_Tac_Toe/board.h"
#include "Tic_Tac_Toe/constants.h"
#include <string>
#include <vector>
#include <iostream>
#include <cmath>

void Board::empty_board(){
    std::fill_n(board.begin(), Const::N_FIELDS, Const::EMPTY_VALUE);
}

Board::Board(){
    for(int i = 0; i < Const::N_FIELDS; i++){
        board.push_back(Const::EMPTY_VALUE);
    }
}

std::string Board::to_string(){
    std::string board_s = "";
    int elem = 0;

    for(int i = 0; i < board.size(); i++)
    {
        elem = board.at(i);

        switch(elem){
            case Const::X_VALUE:
                board_s += "|X|";
                break;
            case Const::O_VALUE:
                board_s += "|O|";
                break;
            default:
                board_s += "| |";
                break;
        }

        if((i+1) % Const::N_ROW_COLUMN == 0){
            board_s += "\n";
        }
    }

    return board_s;
}

int Board::to_table_value(){
    int board_table_value = 0;
    for(auto& elem: board){
        board_table_value *= 10;
        board_table_value += elem;
    }
    return board_table_value;
}

std::vector<int> Board::get_board(){
    return board;
}

bool Board::is_valid(int position){
    bool valid_position = position <= Const::N_FIELDS && position > 0;
    if(valid_position){
        valid_position = board.at(position-1) == 0;
    }
    return valid_position;
}

bool Board::enter_input(int position, int input) {
    bool valid = true;
    bool valid_input = input == Const::X_VALUE || input == Const::O_VALUE;
    if(is_valid(position) && valid_input){
        board.at((position-1)) = input;
    }else{
        valid = false;
    }
    return valid;
}

std::ostream& operator<<(std::ostream& os, Board& board){
    os << board.to_string() << std::endl;
    return os;
}