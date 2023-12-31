# Project "Nebuchadnezzar"

![William_Blake_-_Nebuchadnezzar_(Tate_Britain)](https://github.com/Wra1th/Nebuchadnezzar/assets/12640013/9c40de66-82d7-4b74-a2a2-5bda52d2db24)

## 3301 Cicada | Liber Primus | Solving Tool | GP_tool
# ![Screenshot 2023-09-16 162429](https://github.com/Wra1th/Nebuchadnezzar/assets/12640013/67c733b7-162e-486a-a331-1c3d169ffbde)

> [!NOTE]
> This program does **NOT** work with runes. Only letters and numbers. All string inputs are CSV format.

example:
```
input:
(2, 3, 5, 7, 11, ...)
(2,3,5,7,11,...)
(A, B, C, D, E, ...)
(A,B,C,D,E,...)
```
## Tutorial
Main Menu
1. Key Shift
2. Prime Values (needs revision)
3. Count Elements
4. String Cleaner
5. Rolling Key
6. Quit

### 1. Key Shift
+ First accepts a user input for a character string to be shifted. **MUST BE LETTERS** Then asks for user for shift sequence. **CAN BE LETTERS OR NUMBERS**. 

> [!Note]
> Length of string and shift sequence **MUST** be the same length.

<br>

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
### 2. Prime Value
{to be revised}

### 3. Count Elements
+ Counts the elements  within the string provided by the user.

example:<br>
```
Main Menu:
[1] Key Shift
[2] Prime Values
[3] Count Elements
[4] String Cleaner
[5] Rolling Key
[6] Quit

Enter the option number: 3
Enter one or more characters to check (separated by commas): F, U, TH, O, R, C, A, B, C, D, E
There are 11 elements in the input.
Return to menu? (y/n)
```

### 4. String Cleaner
+ Takes commas and whitespace out of input string.

example:
```
Main Menu:
[1] Key Shift
[2] Prime Values
[3] Count Elements
[4] String Cleaner
[5] Rolling Key
[6] Quit

Enter the option number: 4
Enter a string: A, N, E, N, D, W, I, TH, I, N, TH, E, D, E, E, P, W, E, B, TH, E, R, E, E, X, I, S, T, S, A, P, A, G, E, TH, A, T, H, A, S, H, E, S, T, O, I, T, I, S, TH, E, D, U, T, Y, O, F, E, U, E, R, Y, P, I, L, G, R, I, M, T, O, S, E, E, C, O, U, T, TH, I, S, P, A, G, E
Cleaned String: ANENDWITHINTHEDEEPWEBTHEREEXISTSAPAGETHATHASHESTOITISTHEDUTYOFEUERYPILGRIMTOSEECOUTTHISPAGE
Return to menu? (y/n)
```



to be continued...
