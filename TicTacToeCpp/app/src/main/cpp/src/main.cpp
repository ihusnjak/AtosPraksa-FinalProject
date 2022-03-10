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
    try {
        std::unique_ptr<Player> player_one(new RandomPlayer(Player::PlayerSymbol::X));
        std::unique_ptr<Player> player_two(new MinMaxPlayer(Player::PlayerSymbol::O));
        std::unique_ptr<Game> game(new Game(player_one, player_two));

        Game::GameState state = game->play();

        if(state == Game::GameState::XWon) {
            std::cout << "The state is: X" << std::endl;
        }else if(state == Game::GameState::OWon){
            std::cout << "The state is: O" << std::endl;
        }else{
            std::cout << "It is draw." << std::endl;
        }
    }catch(std::exception& e){
        std::cout << e.what() << std::endl;
    }
    return 0;
}