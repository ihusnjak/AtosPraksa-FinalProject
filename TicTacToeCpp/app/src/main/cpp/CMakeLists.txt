cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 14)

project(Tic_Tac_Toe)



find_library(
        log-lib
        log )

add_library(Tic_Tac_Toe src/main.cpp src/board.cpp src/human_player.cpp src/player.cpp src/Qtable.cpp src/game.cpp src/helper_functions.cpp src/random_player.cpp src/minmax_player.cpp src/q_player.cpp)

target_include_directories(Tic_Tac_Toe PUBLIC include/)

target_link_libraries(
        Tic_Tac_Toe

        ${log-lib} )

