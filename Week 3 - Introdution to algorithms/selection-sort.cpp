#include <iostream>
#include <vector> // Include the vector header for using std::vector
#include <algorithm> // Include the algorithm header for using std::swap

int main() {
    // Write C++ code here
    std::cout << "Hello world!";
    std::vector<int> List = {6, 8, 19, 48, 9, 90}; // Use curly braces to initialize the vector
    int n = List.size(); // Store the size of the vector in 'n'
    int count_swap = 0;
    for (int i = 0; i < n - 1; i++) { // Declare 'i' and 'j' as int
        int min_index = i; // Initialize 'min_index' with 'i'
        for (int j = i + 1; j < n; j++) { // Add missing curly braces and semicolon
            if (List[j] < List[min_index]) {
                min_index = j;
            }
        }
        if (min_index != i){
        std::swap(List[i], List[min_index]); // Use std::swap to swap elements
        count_swap++;
        }
    }
    std::cout << "Sorted List: ";
    for (int i = 0; i < n; i++) {
        std::cout << List[i] << " "; // Print each element of the sorted list
    }
    std::cout << "Swap: ";
    std::cout << count_swap <<std::endl;
    return 0;
}

// output: Hello world!Sorted List: 6 8 9 19 48 90 Swap: 5