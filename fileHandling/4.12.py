def process_books():
    file = open("books.csv", "r", encoding="utf-8")

    header = file.readline() 

    for line in file:
        line = line.strip()
        parts = line.split(",")

        title = parts[0]
        author = parts[1]
        genre = parts[2]
        year = parts[3]

        if genre == "Fantasy":
            out = "books_fantasy.txt"
        elif genre == "Historical":
            out = "books_historical.txt"
        elif genre == "Romance":
            out = "books_romance.txt"
        elif genre == "Classic":
            out = "books_classic.txt"
        else:
            continue

        out_file = open(out, "a", encoding="utf-8")
        out_file.write(title + ", " + author + ", " + year + "\n")
        out_file.close()

    file.close()


process_books()