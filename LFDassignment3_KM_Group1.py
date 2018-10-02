from sklearn import svm

# Load corpus from a file.
# Open the file "corpus_file", return a list of texts and another list
# of all labels. If use_sentiment is true then take the second word in
# line as label (positive or negative), otherwise use the first word as
# label (topics).
def read_corpus(corpus_file, use_sentiment):
    documents = []
    labels = []
    with open(corpus_file, encoding='utf-8') as f:
        for line in f:
            tokens = line.strip().split()

            documents.append(tokens[3:])

            if use_sentiment:
                # 2-class problem: positive vs negative
                labels.append(tokens[1])
            else:
                # 6-class problem: books, camera, dvd, health, music, software
                labels.append(tokens[0])

    return documents, labels


def main():
    pass


if __name__ == '__main__':
    main()
