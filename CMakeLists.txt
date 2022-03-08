cmake_minimum_required(VERSION 3.21)
set(CMAKE_CXX_STANDARD 14)

project(Tic_Tac_Toe)

add_executable(Tic_Tac_Toe src/main.cpp src/board.cpp src/human_player.cpp src/player.cpp src/Qtable.cpp src/game.cpp src/helper_functions.cpp)

target_include_directories(Tic_Tac_Toe PUBLIC include/)

