cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 14)

project("TicTacToe")

if(ANDROID)
	add_library(${PROJECT_NAME} SHARED ${CMAKE_SOURCE_DIR}/src/main.cpp ${CMAKE_SOURCE_DIR}/src/board.cpp ${CMAKE_SOURCE_DIR}/src/human_player.cpp ${CMAKE_SOURCE_DIR}/src/player.cpp ${CMAKE_SOURCE_DIR}/src/Qtable.cpp ${CMAKE_SOURCE_DIR}/src/game.cpp ${CMAKE_SOURCE_DIR}/src/helper_functions.cpp ${CMAKE_SOURCE_DIR}/src/random_player.cpp ${CMAKE_SOURCE_DIR}/src/minmax_player.cpp ${CMAKE_SOURCE_DIR}/src/q_player.cpp)
	
else()
	add_executable(${PROJECT_NAME} ${CMAKE_SOURCE_DIR}/src/main.cpp ${CMAKE_SOURCE_DIR}/src/board.cpp ${CMAKE_SOURCE_DIR}/src/human_player.cpp ${CMAKE_SOURCE_DIR}/src/player.cpp ${CMAKE_SOURCE_DIR}/src/Qtable.cpp ${CMAKE_SOURCE_DIR}/src/game.cpp ${CMAKE_SOURCE_DIR}/src/helper_functions.cpp ${CMAKE_SOURCE_DIR}/src/random_player.cpp ${CMAKE_SOURCE_DIR}/src/minmax_player.cpp ${CMAKE_SOURCE_DIR}/src/q_player.cpp)
endif()


target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)

