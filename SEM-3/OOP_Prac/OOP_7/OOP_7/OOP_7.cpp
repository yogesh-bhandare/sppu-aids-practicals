//Yogesh Bhandare SE AIDS 22506
//Write a program in C++ to use map associative container.The keys will be the names of states
//and the values will be the populations of the states.When the program runs, the user is
//prompted to type the name of a state.The program then looks in the map, using the state name
//as an index and returns the population of the state.

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    // Define a map to store state populations
    map<string, long long> statePopulations;

    // Populate the map with state populations
    statePopulations["Utter Pradesh"] = 199812341; 
    statePopulations["Bihar"] = 104099452;
    statePopulations["Maharashtra"] = 112374333;
    statePopulations["West Bengal"] = 91276115;
    statePopulations["Madhya Pradesh"] = 72626809;
    statePopulations["Tamil Nadu"] = 68548437;
    statePopulations["Rajasthan"] = 61095297;
    statePopulations["Karnataka"] = 60439692;
    statePopulations["Gujarat"] = 49577103;
    statePopulations["Andhra Pradesh"] = 41974219;
    statePopulations["Odisha"] = 35003674;
    statePopulations["Telangana"] = 33406061;
    statePopulations["Kerala"] = 32988134;
    statePopulations["Jharkhand"] = 31205576;
    statePopulations["Assam"] = 27743338;
    statePopulations["Punjab"] = 25545198;
    statePopulations["Chhattisgarh"] = 25351462;
    statePopulations["Haryana"] = 21477737;
    statePopulations["NCT of Delhi"] = 16787941;
    statePopulations["Jammu and Kashmir"] = 12267032;
    statePopulations["Uttarakhand"] = 10086292;
    statePopulations["Himachal Pradesh"] = 6864602;
    statePopulations["Tripura"] = 3673917;
    statePopulations["Meghalaya"] = 2966889;
    statePopulations["Manipur"] = 2570390;
    statePopulations["Nagaland"] = 1978502;
    statePopulations["Goa"] = 1458545;
    statePopulations["Arunachal Pradesh"] = 1383727;
    statePopulations["Puducherry"] = 1247953;
    statePopulations["Mizoram"] = 1097206;
    statePopulations["Chandigarh"] = 1055450;
    statePopulations["Sikkim"] = 610577;
    statePopulations["Dadra and Nagar Haveli and Daman and Diu"] = 585764;
    statePopulations["Andaman and Nicobar Islands"] = 380581;
    statePopulations["Ladakh"] = 274000;
    statePopulations["Lakshadweep"] = 64473;
    

    // Prompt the user to enter the name of a state
    cout << "Enter the name of a state: ";
    string inputState;
    getline(cin, inputState);

    // Look up the population of the entered state in the map
    auto it = statePopulations.find(inputState);

    // Check if the state is found in the map
    if (it != statePopulations.end()) {
        cout << "Population of " << inputState << ": " << it->second << endl;
    }
    else {
        cout << "State not found in the map." << endl;
    }

    return 0;
}
