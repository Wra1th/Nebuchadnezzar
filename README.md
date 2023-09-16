# Project "Nebuchadnezzar"
3301 Cicada | Liber Primus | Solving Tool GP_tool1.3

## Tutorial
# ![Screenshot 2023-09-16 162429](https://github.com/Wra1th/Nebuchadnezzar/assets/12640013/67c733b7-162e-486a-a331-1c3d169ffbde)
### All string inputs are CSV format
```
(2, 3, 5, 7, 11...)
(2,3,5,7,11...)
(A, B, C, D, E...)
(A,B,C,D,E,...)
```

This program does **NOT** work with runes. Only letters and numbers.


## Main Menu
  1. Key Shift
  2. Prime Values (needs revision)
  3. Count Elements
  4. String Cleaner
  5. Rolling Key
  6. Quit

### Key Shift
First accepts a user input for a character string to be shifted. **MUST BE LETTERS** Then asks for user for shift sequence. **CAN BE LETTERS OR NUMBERS**. 

> ![**Note**] <br>
> Length of string and shift sequence **MUST** be the same length.

example:<br>
```
Main Menu:
[1] Key Shift
[2] Prime Values
[3] Count Elements
[4] String Cleaner
[5] Rolling Key
[6] Quit

Enter the option number: 1
Enter a string to be shifted. (separated by commas): F, U, TH, O, R, C
Enter a shift sequence (characters or numbers, separated by commas): 2, 3, 5, 7, 1, 13
chars: ['f', 'u', 'th', 'o', 'r', 'c']
shift_seq: [2, 3, 5, 7, 1, 13]
results: TH, R, W, I, C, E
Return to menu? (y/n)

```
