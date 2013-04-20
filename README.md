Hackerrank-Circles
==================

SignalFire University Hacker Olympics Circles Problem

Bayar is currently at the bottom wall of the rectangular shaped room. And there are several detectors in the room. Each of them covers circle area. His goal is to reach the top wall of the room without getting caught. This is not always possible, so he wants to remove some of the detectors in order to achieve his goal. Find minimum number of detectors you need to remove.
Each circle can be described by its position of the center and its radius.
Note: Not actual layout of the room. There are a lot more detectors. Origin for the room is in the bottom left corner with the coordinate (0,0).

Input:
First line indicates how many tests there are. For each test first line contains three space separated integers (W, H, N). First two integers are width and height of the room respectively, and third integer is number of detectors in the room. Next N lines will represent detectors. Each line contains three space separated integers (X, Y, R). X and Y are coordinate of the detector and R is the radius of the detector.

Output:
For each test you must output one line containing the minimum number of circles need to be removed.

Constraints:
Number of tests <= 10
Number of circles per test <= 100
W, H <= 1000
X, Y <= W, H

Sample Input

3
3 3 2
0 1 1
3 1 2
5 5 2
1 1 1
4 1 1
5 5 4
1 1 1
2 1 1
3 1 1
4 1 1

Sample Output
1
0
1

Scoring
The more testcases you pass the higher your score will be. This will depend on the efficiency of your algorithm.