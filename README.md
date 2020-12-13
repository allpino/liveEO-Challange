# liveEO Challange
 
Once the app runs, it does the 3 parts of the assignment at once with different outputs. You can find these outputs in src\output folder.

The app does not require an additional library. Hence, there're no requirements.txt

In order to run the app, go to src folder and run main.py. It takes 2 parameters:

First one determines the number of pair, used in part 1 -→ Must be integer.
Second one determines the number of window, used in part 2 and 3 -→ Must be integer.

Example running command:

main.py 3 18


TESTING:

Since there's no straight forward way to compare results, I didn't make an unit test. However, I made parameters as inputs. This means that you can test the program with different parameters. For example, I tested it with different combinations:

main.py 1 18 -→ There will be at most 2 pairs in part 1.
main.py 3 1 -→ 1-day window gap, this is not possible therefore output will be empty for part 2 and 3.
main.py 3 6 -→ 6-day window gap, this is the minimum day required to have pairs for part 2 and 3. Hence, there will be some pairs.

Finally, in order to test correctness of my app, I used main.py 3 18 and compared outputs with given example outputs. Results were 100% exact. However, in magical value of the part 3 there were some small discrepancies due to precision and notation difference.


