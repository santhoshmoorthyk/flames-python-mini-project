Project Overview:

This project implements the FLAMES relationship logic using Python. The program takes two names, removes matching characters, counts the remaining letters, and determines the final FLAMES outcome. It is designed as a simple Python mini project to demonstrate string manipulation, loops, and basic algorithm implementation.

Key Features:
Input Processing:

The program normalizes the input by converting names to lowercase, removing spaces, and converting them into lists for comparison.

Character Elimination Logic:

Common characters between the two names are removed, and the remaining character count is used as the basis for FLAMES elimination.

FLAMES Algorithm:

A cycle-based elimination is applied on the letters F, L, A, M, E, S until one result remains. The logic is implemented using list operations and modular indexing.

No External Libraries:

The entire project uses only Python’s built-in functions and follows a straightforward script structure.

Technical Aspects:

Uses Python string methods such as lower(), replace(), and list operations.

Implements a stepwise reduction approach to remove matching characters.

Uses index-based circular elimination for the FLAMES sequence.

Maintains a clean and minimal code style suitable for beginners studying Python fundamentals.
