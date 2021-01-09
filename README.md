# CS50x_DNA
A program that identifies a person based on their DNA. The program is based on Harvard's CS50's Introduction to Computer Science 2021 OpenCourseWare's problem set-6.

THe program takes a text file containing sequence of DNA and a CSV file containing Short Tandem Repeat (STR) counts for a list of individuals. For each of the STRs (from the first line of the CSV file), the program computes the longest run of consecutive repeats of the STR in the DNA sequence. If the STR counts match exactly with any of the individuals in the CSV file, the program prints out the name of the matching individual. If the STR counts do not match exactly for any individual, No Match is printed.

References:
1. https://www.edx.org/course/cs50s-introduction-to-computer-science
2. https://cs50.harvard.edu/x/2021/psets/6/dna/#:~:text=take%20a%20sequence%20of%20DNA%20and%20a%20CSV%20file%20containing%20STR%20counts%20for%20a%20list%20of%20individuals%20and%20then%20output%20to%20whom%20the%20DNA%20(most%20likely)%20belongs.
