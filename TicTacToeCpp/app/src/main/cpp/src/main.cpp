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
#include <jni.h>

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

extern "C" JNIEXPORT jint JNICALL
Java_hr_atos_praksa_tictactoecpp_GameBoardActivity_makeMoveJNI(
        JNIEnv* env,
        jobject /* this */,
        jstring board_input,
        jint human_turn,
        jint move) {
    const char* convertedBoardInputChar = env->GetStringUTFChars(board_input, NULL);
    std::string convertedBoardInputString = convertedBoardInputChar;
    int newBoard = make_move(convertedBoardInputString, human_turn, move);
    return newBoard;
}


int main(){
    try {
        //train(20000);
        //play(1);
        std::string board_input = "110220110";
        int human_turn = 1;
        int move = 9;
        std:: cout << make_move(board_input, human_turn, move) << std::endl;

    }catch(std::exception& e){
        std::cout << e.what() << std::endl;
    }
    return 0;
}