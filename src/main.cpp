#include <iostream>
#include "Tic_Tac_Toe/board.h"
#include <string>
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/constants.h"
#include <vector>

int main(){
    Player* pl1 = new HumanPlayer();
    Player* pl2 = new HumanPlayer();
    Game* game = new Game(pl1, pl2);
    try {
        Winner winner = game->play();
        if(winner == Winner::FirstPlayer) {
            std::cout << "The winner is: X" << std::endl;
        }else if(winner == Winner::SecondPlayer){
            std::cout << "The winner is: O" << std::endl;
        }else{
            std::cout << "It is draw." << std::endl;
        }
    }catch(std::exception& e){
        std::cout << e.what() << std::endl;
    }

    return 0;
}