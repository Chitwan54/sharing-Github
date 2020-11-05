#include <iostream>
using namespace std;
const unsigned int Sunday = 1;
// January = 1, February = 2, ..., December = 12
// returns 0 => Saturday, 1 => Sunday, 2 => Monday, ... 6 => Friday
unsigned int getWeekday(unsigned long long year, unsigned int month, unsigned int day)
{

  // January and February are counted as month 13 and 14 of the previous year
  if (month <= 2)
  {
    month += 12;
    year--;
  }

  return (day +
          13 * (month + 1) / 5 +
          year + year / 4 - year / 100 + year / 400)
         % 7;
}

int main()
{
  
  
    unsigned long long year1, year2;
    unsigned int month1, month2, day1, day2;
    //cin >> year1 >> month1 >> day1; // from
    //cin >> year2 >> month2 >> day2; // to
    year1 = 1901;
    month1 = 1;
    day1 = 1;
    year2 = 2000;
    day2 = 31;
    month2 = 12;

    // wrong input order ?
    if (year2 < year1 || (year2 == year1 && month2 < month1))
    {
      swap(year1,  year2);
      swap(month1, month2);
    }

    // jump forward to the first day of the month
    unsigned long long currentYear  = year1;
    unsigned int       currentMonth = month1;
    if (day1 > 1)
    {
      currentMonth++;

      // from December to January of next year
      if (currentMonth > 12)
      {
        currentMonth -= 12;
        currentYear++;
      }
    }

    // number of relevant Sundays
    unsigned int sum = 0;

    // same patterns every 2800 years
    while (currentYear + 2800 < year2)
    {
      currentYear += 2800;
      sum += 4816;         // there are 4816 Sundays on the first of a month in 2800 years
    }
    // note: a constant-time approach would be to use MOD ...
    //       but the while-loop is probably easier to understand

    // simple scan through all months
    while (currentMonth < month2 || currentYear < year2) // days already match, they are both 1
    {
      // count Sundays
      if (getWeekday(currentYear, currentMonth, 1) == Sunday)
        sum++;

      currentMonth++;

      // from December to January of next year
      if (currentMonth > 12)
      {
        currentMonth -= 12;
        currentYear++;
      }
    }
    // check last month, too
    if (getWeekday(currentYear, currentMonth, 1) == Sunday)
      sum++;

    cout << sum << endl;
  
  return 0;
}
