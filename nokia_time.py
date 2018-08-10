"""[summary]
to find the time taken for typing the text
[description]
You may be already familiar with the working of the keypad, however if you're not we shall see a few examples.

To type "b", we need to press "2" twice. To type "?" we need to press "1" thrice. To type "5" we need to press "5" four times. To type "0" we need to press "0" twice.

I hope that it's clear how the keypad is being used.

Now Roy has lot of text messages and they are pretty lengthy. So he devised a mechanical-hand-robot (with only 1 finger) which does the typing job. One drawback of this robot is its typing speed. It takes 1 second for single press of any button. Also it takes 1 second to move from one key to another. Initial position of the hand-robot is at key 1.

So if its supposed to type "hack" it will take 1 second to move from key 1 to key 4 and then 2 seconds to type "h".
Now again 1 second to move from key 4 to key 2 and then 1 second to type "a".
Since "c" is present at the same key as "a" movement time is 0. So it simply takes 3 seconds to type "c".
Finally it moves from key 2 to key 5 in 1 second and then 2 seconds to type "k". So in total it took 1+2+1+1+3+1+2= 11 seconds to type "hack".

Input:
First line contains T - number of test cases.
Each of next T lines contain a string S - the message Roy needs to send.
Each string is terminated by a newline escape sequence \n.

Output:
For each test case output the time taken by the hand-robot to type down the message.

SAMPLE INPUT 
3
hack
5!
i_?_u

SAMPLE OUTPUT 
11
10
15
"""

#nokia keybord as list of lists
list1 = [
    ['.',',','?','!','1'],
    ['a','b','c','2'],
    ['d','e','f','3'],
    ['g','h','i','4'],
    ['j','k','l','5'],
    ['m','n','o','6'],
    ['p','q','r','s','7'],
    ['t','u','v','8'],
    ['w','x','y','z','9'],
    ['_','0']
    ]

# function to calcultae the time taken

def time_taken(ip1):
        tt = 0
        clist = [0]
        for c in ip1
            
            for each in list1:
                if c in each:
                    if(list1.index(each) != clist[-1]):
                        tt = tt+1
                    i = each.index(c)
                    tt = tt + i + 1
                    clist.append(list1.index(each))
        print(tt)

i = int(input())
for test in range(i):
    ip1 = list(input())
    time_taken(ip1)

