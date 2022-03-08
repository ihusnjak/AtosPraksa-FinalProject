#pragma once

#include "player.h"

class HumanPlayer: public Player{
    public:
        explicit HumanPlayer();
        int play() override;
};