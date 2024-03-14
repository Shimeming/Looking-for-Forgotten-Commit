import util
import const
import time


def home():
    action = '0'
    while True:
        action = input('''
Please select an action you want to do.
  * 1)  Challenge 1
  * 2)  Challenge 2
  * 3)  Merge the two keys
  * Q)  Quit
Enter a number: ''')
        util.clear()
        
        if action == '1':
            pass
        if action == '2':
            pass
        if action == '3':
            util.clear()
            key1 = input('Please insert the first key obtained from Challenge 1: ')
            key2 = input('Please insert the first key obtained from Challenge 2: ')
            for i in range(6):
                print('Casting the flag' + (i%3+1)*'.' + '   ', end='\r')
                time.sleep(1)
            flag1 = util.unlock(key1, const.SLOT1)
            flag2 = util.unlock(key2, const.SLOT2)
            print()
            print('The flag is: ')
            print(f'{flag1}{flag2}')
        if action == 'Q':
            break
