# Problem: Write a Python function that reads data from a text file, counts the occurrences of each word, and returns a dictionary with word frequencies.

# Proposed solution


def word_frequency(filename):
    word_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count


# Test the function with a text file
filename = "sample.txt"
word_freq = word_frequency(filename)
print("Word frequency:", word_freq)
