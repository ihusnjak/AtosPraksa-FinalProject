#include <iostream>
#include "Tic_Tac_Toe/board.h"
#include <string>
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/random_player.h"
#include "Tic_Tac_Toe/minmax_player.h"
#include "Tic_Tac_Toe/q_player.h"
#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/constants.h"
#include "Tic_Tac_Toe/Qtable.h"
#include <vector>
#include <memory>

int main(){
    std::unique_ptr<Player> pl1(new RandomPlayer());
    std::unique_ptr<Player> pl2(new MinMaxPlayer(Winner::SecondPlayer));
    std::unique_ptr<Game> game(new Game(pl1, pl2));

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