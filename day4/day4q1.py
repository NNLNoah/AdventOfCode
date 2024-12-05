# read file, treat like word search by converting to list of lists, iterate through each row,  each column,  each diagonal,
# and each reverse diagonal, and check if the word XMAS is in the list of lists

        
with open("day4/data.txt", 'r') as file:
    sum = 0
    rows = [row.strip() for row in file]  # Strip newline characters and store rows in a list

    # Count occurrences in rows
    for row in rows:
        row_upper = row.upper()
        sum += row_upper.count("XMAS")
        sum += row_upper.count("SAMX")  # Reverse of "XMAS"

    # Initialize column strings
    if rows:
        cols = ['' for _ in range(len(rows[0]))]
        for row in rows:
            for i in range(len(row)):
                cols[i] += row[i]

        # Count occurrences in columns
        for col in cols:
            col_upper = col.upper()
            sum += col_upper.count("XMAS")
            sum += col_upper.count("SAMX")

    # Diagonal logic
    n = len(rows)
    m = len(rows[0])

    # Top-left to bottom-right diagonals
    for d in range(n + m - 1):
        diag1 = ''  # Forward diagonal
        diag2 = ''  # Reverse diagonal
        for i in range(max(0, d - m + 1), min(d + 1, n)):
            j = d - i
            diag1 += rows[i][j]
            diag2 += rows[i][m - j - 1]
        diag1_upper = diag1.upper()
        diag2_upper = diag2.upper()
        sum += diag1_upper.count("XMAS")
        sum += diag1_upper.count("SAMX")
        sum += diag2_upper.count("XMAS")
        sum += diag2_upper.count("SAMX")

print(sum)
