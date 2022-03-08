#pragma once

enum class Winner{
    Draw, Ongoing, FirstPlayer, SecondPlayer
};

namespace Const{
    const int N_ROW_COLUMN = 3;
    const int N_FIELDS = N_ROW_COLUMN * N_ROW_COLUMN;
    const int X_VALUE = 1;
    const int O_VALUE = -1;
    const int EMPTY_VALUE = 0;
};