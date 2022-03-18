#include "Tic_Tac_Toe/Qtable.h"
#include "Tic_Tac_Toe/constants.h"
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <sstream>
#include <fstream>
#include <iterator>

bool QTable::key_exists(int key) {
    bool exists = false;
    if (std::find(keys.begin(), keys.end(), key) != keys.end()) {
        exists = true;
    }

    return exists;
}

void QTable::add_key_value(int key, std::vector<float>& values){
    if(values.size() == Const::N_FIELDS) {
        if(key_exists(key)){
            //update if already exists
            auto it = std::find(keys.begin(), keys.end(), key);
            int idx = it - keys.begin();
            std::copy(values.begin(), values.end(), this->values.begin() + idx*Const::N_FIELDS);

        }else{
            //append if it is a new one
            this->keys.push_back(key);
            this->values.insert(std::end(this->values), std::begin(values), std::end(values));
        }
    }else{
            throw std::runtime_error(size_error);
        }
}

std::shared_ptr<std::vector<float>> QTable::get_values(int key) {
    std::shared_ptr<std::vector<float>> values = nullptr;

    if(key_exists(key)){
        auto it = std::find(keys.begin(), keys.end(), key);
        int idx = it - keys.begin();
        auto start = this->values.begin() + idx*Const::N_FIELDS;
        auto end = start + Const::N_FIELDS;
        values = std::make_shared<std::vector<float>>(Const::N_FIELDS);
        std::copy(start, end, values->begin());
    }

    return values;
}

std::shared_ptr<std::string> QTable::values_to_string(const std::vector<float>& values){
    std::shared_ptr<std::string> result = std::make_shared<std::string>();

    if(values.size() == Const::N_FIELDS) {
        std::ostringstream oss;
        std::copy(values.begin(), values.end() - 1, std::ostream_iterator<float>(oss, ","));
        oss << values.back();

        *result = oss.str();
    }else{
        throw std::runtime_error(size_error);
    }
    return result;
}

void QTable::save_table(const std::string& filename){
    std::ofstream file;
    file.open(filename);

    if(!file){
        throw std::runtime_error("File could not be opened.");
    }
    for(auto&key : keys){
        file << key << "," << *values_to_string(*get_values(key)) << "\n";
    }
    file.close();
}

void QTable::load_table(const std::string &filename) {
    std::string line;
    std::string substring;

    std::stringstream stream;

    std::vector<std::string> substrings;
    std::vector<float> values;

    int key;

    std::ifstream file;
    file.open(filename);

    if(!file){
        throw std::runtime_error("File could not be opened.");
    }

    while (getline(file, line)) {
        stream = std::stringstream(line);
        while(stream.good()){
            getline(stream, substring, ',');
            substrings.push_back(substring);
        }

        std::transform(substrings.begin()+1, substrings.end(), std::back_inserter(values),
                       [](const std::string& str) { return std::stof(str); });

        key = std::stoi(substrings.at(0));

        add_key_value(key, values);

        substrings.clear();
        values.clear();
    }
    file.close();
}

QTable::QTable() {}