def grading(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print(grading(int(input())))
