#pragma once

#include <string>

namespace Const{
    const std::string POLICY_PATH_X = R"(../policy_x.csv)";
    const std::string POLICY_PATH_O = R"(../policy_o.csv)";
    const int X_WON_SIGNAL = 1;
    const int O_WON_SIGNAL = 2;
    const int ONGOING_SIGNAL = 0;
    const int DRAW_SIGNAL = 3;
    const int ERROR_SIGNAL = -1;
    const int HUMAN_PLAYS_FIRST_SIGNAL = 1;
    const int HUMAN_PLAYS_SECOND_SIGNAL = 2;
    const float Q_WIN_REWARD = 1.0;
    const float Q_DRAW_REWARD = 0.5;
    const float Q_LOSE_REWARD = 0.0;
    const float Q_DEFAULT_VALUE = 0.0;
    const float Q_LEARNING_RATE = 0.9;
    const float Q_DISCOUNT_RATE = 0.95;
    const float CUTOFF_Q_VALUE = 0.0;
    const int N_ROW_COLUMN = 3;
    const int N_FIELDS = N_ROW_COLUMN * N_ROW_COLUMN;
    const int X_VALUE = 1;
    const int O_VALUE = -1;
    const int EMPTY_VALUE = 0;
    const int O_TABLE_VALUE = 2;
    const int MIN_POSITION = 1;
    const int MIN_MAX_REWARD = 10;
    const int MINIMIZER_MAX_VALUE = 1000;
    const int MAXIMIZER_MIN_VALUE = -MINIMIZER_MAX_VALUE;
}
