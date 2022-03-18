#include <iostream>
#include "Tic_Tac_Toe/human_player.h"
#include "Tic_Tac_Toe/random_player.h"
#include "Tic_Tac_Toe/minmax_player.h"
#include "Tic_Tac_Toe/q_player.h"
#include "Tic_Tac_Toe/player.h"
#include "Tic_Tac_Toe/game.h"
#include "Tic_Tac_Toe/board.h"
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

int make_move(std::string& board_input, int human_turn, int move){
    std::unique_ptr<Game> game(new Game(board_input));
    return game->make_move(human_turn, move);
}

int main(){
    try {
        //train(20000);
        //play(1);
        std::string board_input = "000000000";
        //JUST CHANGE HUMAN_TURN AND START
        //first input as O will be ignored but must be from 1 to 9
        //you wont see the board on first move, it is empty btw so pick a number from 1 to 9
        int human_turn = 1;

        int move = 0;
        int result = 0;
        int machine_move = 0;
        int winner = 0;
        bool first = true;
        while(true){
            std::cin >> move;
            result = make_move(board_input, human_turn, move);

            //machine(Q learning bot) move can be easily gotten as:
            machine_move = result%10;
            //winner can be easily gotten as:
            winner = result/10;

            if(winner > 0){
                if(winner == 1){
                    std::cout << "Winner is: X" << std::endl;
                }
                if(winner == 2){
                    std::cout << "Winner is: O" << std::endl;
                }
                if(winner == 3){
                    std::cout << "Draw." << std::endl;
                }
                break;
            }

            if(machine_move > 0 && machine_move < 10){
                if(human_turn == 2 && first){
                    first = false;
                }else {
                    board_input[move - 1] = human_turn + '0';
                }
                board_input[machine_move-1] = human_turn == 2? '1' : '2';
            }

        }

    }catch(std::exception& e){
        std::cout << e.what() << std::endl;
    }
    return 0;
}