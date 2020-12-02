#  Variables
sequence = [0, 1]
usrInput = 0

#  Gets all the Fibonacci sequence numbers up to 1597, the first value in the sequence > 1000
for i in range(1, 18):
    sequence.append(sequence[i-1] + sequence[i])

#  Get user input and validate it
while usrInput < 1 or usrInput > 1000:
    usrInput = int(input("Enter a number between 1 and 1000: "))

if usrInput in sequence:  # Check if number is valid in sequence
    print(f"{usrInput} is a valid Fibonacci number")
    sequenceFiltered = [i for i in sequence if i >= usrInput]  # Creates a new list that has only values >= usrInput
    print(sequenceFiltered)
else:
    print(f"{usrInput} is not a valid Fibonacci number")