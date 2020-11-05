#include <iostream>
using namespace std;
// Steps are explained in comments.
//1) Create a function for calculating the prodcut.
int pythagorean_triplet() // No arguments because we are not providing any input.
{   int a,b,c; // Declaring 4 variables : 3 numbers (Pythagorean Triplets) and 1 for storing the result.
    int product;
    // Since a<b<c, we iterate our variables from 1 to 1000 because their sum is 1000 and it is obvious that individual variable will not exceed 1000.
    for(a = 1 ; a<=1000 ; a++)
    {
        for(b = a+1 ; b<=1000 ; b++)
        {
              c = 1000 - a - b; // Here we could have run a similar loop but to optimise our code we will use the given condition, i.e a+b+c = 1000.
              if(a*a + b*b == c*c) // If the numbers are Pythagorean Triplets we calculate the product.
               {
                   product = a*b*c; 
               }
        }
    }
    return product; // Return the answer.
}
int main() {
    cout<<"Product of pythagorean triplet a,b,c is: "<<pythagorean_triplet(); // Calling the function in the main function.
    return 0;
   
}
