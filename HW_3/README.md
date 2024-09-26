# Python Homework №3

This repository contains solutions to the third homework assignment, which consists of two programming tasks written in Python. All tasks are located in separate files. The solutions are implemented with custom logic without using any unnecessary external libraries.

## [Task 01: Text Compression](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_3/Task_01.py)
The program reads a `.txt` file and processes it by splitting the text into words and non-letter elements. The words are counted, sorted by their frequency of occurrence, and then the text is compressed by replacing words with their reverse order of frequency.

- **Input**: A `.txt` file (e.g., [`Input.txt`](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_3/Input.txt)).
- **Output**: 
  - A CSV file (`output.csv`) containing words with their frequency, length, and index.
  - A compressed version of the text (`Compressed_input.txt`).

### Key Steps:
1. Read and preprocess the text from the input file.
2. Count the occurrence of each word and prepare the sorted list.
3. Output the results to a CSV file and compress the text by replacing words according to their frequency order.

## [Task 02: JSON Data Sorting and Grouping](https://github.com/naumovakotya/Python_Programming_School/blob/main/HW_3/Task_02.py)
This program works with a JSON file containing user data (e.g., `example.json`). It offers functionality to sort and group the data based on various parameters such as username, ID, roles, and companies. Additionally, it checks whether a specific role is associated with a given user.

- **Input**: A JSON file with user information (e.g., `example.json`).
- **Output**: Sorted and grouped data displayed in the terminal, along with role-checking results.

### Key Functions:
1. Sort by login or ID.
2. Group users by role or company.
3. Check if a user has a specific role.


