import numpy as np


def num_letters(num_rows, num_columns):
    return 2 * num_rows + 2 * num_columns - 4


assert num_letters(3, 4) == 10
assert num_letters(13, 4) == 30
assert num_letters(4, 4) == 12
assert num_letters(6, 4) == 16
assert num_letters(6, 7) == 22

print("Checking assertions.")

filename = "loop4.csv"

data = np.loadtxt(
    filename,
    delimiter=",",
    dtype=str,
    encoding="utf-8-sig"
)

data = np.char.strip(data)

rows, columns = data.shape

words = []

for column in range(columns):
    words.append(data[0, column])

for column in range(columns - 1, -1, -1):
    words.append(data[rows - 1, column])

for row in range(1, rows - 1):
    words.append(data[row, columns - 1])

for row in range(rows - 2, 0, -1):
    words.append(data[row, 0])

print("\nLetters:")
print(words)

assert len(words) == num_letters(rows, columns)

two_letter_words = []

for column in range(columns - 1):
    word = data[0, column] + data[0, column + 1]
    two_letter_words.append(word)

for column in range(columns - 1, 0, -1):
    word = data[rows - 1, column] + data[rows - 1, column - 1]
    two_letter_words.append(word)

for row in range(rows - 1):
    word = data[row, columns - 1] + data[row + 1, columns - 1]
    two_letter_words.append(word)

for row in range(rows - 1, 0, -1):
    word = data[row, 0] + data[row - 1, 0]
    two_letter_words.append(word)

print("\nTwo-character words:")
print(two_letter_words)

assert len(two_letter_words) == num_letters(rows, columns)
