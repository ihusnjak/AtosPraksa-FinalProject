#pragma once

#include <vector>
#include <memory>
#include <string>

class QTable{
    private:
        //keys contain integer representation of the board
        std::vector<int> keys;
        //values are logically a matrix where every "row" has the length of number of playable fields
        //those values represent Q values for each possible action
        std::vector<float> values;

        const std::string size_error = "Value vector must contain exactly as many values as the game has fields.";
    public:
        QTable();

        bool key_exists(int key);

        void add_key_value(int key, std::vector<float>& values);

        std::shared_ptr<std::vector<float>> get_values(int key);

        std::shared_ptr<std::string> values_to_string(const std::vector<float>& values);

        void save_table(const std::string& filename);

        void load_table(const std::string& filename);
};