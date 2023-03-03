def main():
    input_file = 'data.txt'
    output_file = 'wordset.txt'
    six_letter_words = []
    
    with open(input_file, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 6:
                six_letter_words.append(word)
    with open(output_file, "w") as f:
        for word in six_letter_words:
            f.write(word + "\n")
    pass

if __name__ == "__main__":
    main()
