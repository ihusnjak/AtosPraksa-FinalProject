#include <iostream>
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/random_player.h"
#include "Tic_Tac_Toe/minmax_player.h"
#include "Tic_Tac_Toe/q_player.h"
#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/game.h"
#include <vector>
#include <memory>

void train(int n){
    std::unique_ptr<Game> game(new Game());
    game->train_loop(n);
}

void play(int which_human){
    Player::PlayerSymbol one = Player::PlayerSymbol::X;
    Player::PlayerSymbol two = Player::PlayerSymbol::O;
    if(which_human == 1){
        Player::PlayerSymbol temp = two;
        two = one;
        one = temp;
    }
    std::unique_ptr<Player> player_one(new QPlayer(one));
    std::unique_ptr<Player> player_two(new HumanPlayer(two));
    std::unique_ptr<Game> game(new Game(player_one, player_two));

    Game::GameState state = game->play();

    if(state == Game::GameState::XWon) {
        std::cout << "The winner is: X" << std::endl;
    }else if(state == Game::GameState::OWon){
        std::cout << "The winner is: O" << std::endl;
    }else{
        std::cout << "It is draw." << std::endl;
    }
}

int main(){
    try {
        //train(20000);
        play(2);
    }catch(std::exception& e){
        std::cout << e.what() << std::endl;
    }
    return 0;
}