# Number to Words
A clean and modular Python project that converts non-negative integers into their English word representation.  
This repository provides two different __recursive__ solutions, demonstrating alternative approaches to solving the same problem with clean architecture and reusable constants.


## Features
* Convert numbers into English words
* Handles:
    - Units (0–19)
    - Tens (20–90)
    - Hundreds
    - Thousands
    - Millions
    - Billions
* Two independent implementations
* Recursive design
* Built-in test cases
* Clean project structure using constants modules 


## Project Structure
```
Num2Word/
│
├── src/
│   ├── solution_1/
│   │   ├── constants.py
│   │   └── main.py
│   │
│   ├── solution_2/
│   │   ├── constant.py
│   │   └── main.py
│
└── README.md
```


## Solution 1 – Pivot Iteration Strategy
__Approach__  
* Iterates through large number pivots (Billion, Million, Thousand, Hundred).
* Recursively converts the quotient.
* Processes tens and units separately.
* Builds the result string step-by-step.

__Key Idea__  
Sort pivots in descending order and reduce the number progressively. 
```
for pivot in sorted(ABOVE_100.keys(), reverse=True):
    if num >= pivot:
        count = num // pivot
        result += num_to_words(count) + " " + ABOVE_100[pivot] + " "
        num %= pivot
```


## Solution 2 – Dynamic Pivot Selection
__Approach__  
* Handles small numbers (< 20, < 100) directly.
* Dynamically selects the largest valid pivot using:
```
pivot = max([key for key in ABOVE_100 if key <= num])
```
* Recursively breaks the number into:
    - Left part (quotient)
    - Pivot word
    - Remaining part (modulus)

__Key Idea__  
Use divide-and-conquer logic to recursively decompose the number.  


## Running Tests
Each solution includes built-in test cases.  
To run:
```
python src/solution_1/main.py
```
or 
```
python src/solution_2/main.py
```
If successful:
```
All tests passed!
```


## Solution Comparison

| Feature        | Solution 1                 | Solution 2               |
| -------------- | -------------------------- | ------------------------ |
| Pivot Handling | Iterative over sorted keys | Dynamic pivot selection  |
| Code Style     | Stepwise building          | Divide-and-conquer       |
| Readability    | Explicit logic flow        | Compact recursive design |
| Performance    | Efficient                  | Efficient                |


## Requirements
Python 3.10+  
No external dependencies required.