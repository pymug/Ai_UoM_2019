import os
import sys
import json

# Constants
CURRENT_FOLDER = os.path.dirname(__file__)

DATA_FOLDER = os.path.join(
    CURRENT_FOLDER, 'aclImdb_v1', 'aclImdb'
)
TEST_NEG_FOLDER = os.path.join(DATA_FOLDER, 'test', 'neg')
TRAIN_NEG_FOLDER = os.path.join(DATA_FOLDER, 'train', 'neg')

TEST_POS_FOLDER = os.path.join(DATA_FOLDER, 'test', 'pos')
TRAIN_POS_FOLDER = os.path.join(DATA_FOLDER, 'train', 'pos')

TEST_DATASET_FOLDERS = (
    (TEST_NEG_FOLDER, 0),
    (TEST_POS_FOLDER, 1),
)

TRAIN_DATASET_FOLDERS = (
    (TRAIN_NEG_FOLDER, 0),
    (TRAIN_POS_FOLDER, 1),
)


class Collector(set):
    """
    Class in charge of collecting movie reviews from
    the IMDB data set from https://ai.stanford.edu/~amaas/data/sentiment/

    Warnings:
        Download & Unzip the data before calling the script.
        https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
        The `aclImdb_v1` folder should be unzipped at root location.

    Notes:
        A set will eliminate duplicated reviews
    """
    _review_count = 500
    _dump_file = os.path.join(CURRENT_FOLDER, 'movie_reviews_{}.json')

    def _read_reviews(self, folders):
        """
        Read reviews from the file system

        Args:
            folders (tuple): The list of data folders
        """
        for (folder, sentiment) in folders:
            counter = 0
            for review_file in os.listdir(folder):
                with open(os.path.join(folder, review_file)) as fd:
                    self.add((fd.read(), sentiment,))
                    counter += 1

                if counter == self._review_count:
                    break

    def _read(self):
        """
        Template method to read the training & testing data sets
        from the file system
        """
        self._read_reviews(TEST_DATASET_FOLDERS)
        self._read_reviews(TRAIN_DATASET_FOLDERS)

    def _write_reviews(self, data, typ, reviews_count):
        """
        Write the reviews to JSON format to ease data manipulation (pandas)

        Args:
            data (list): A list of reviews
            typ (str): Training or Testing reviews
            reviews_count (int): The overall count of reviews
        """
        data_file = self._dump_file.format(typ)
        with open(data_file, 'w') as fd:
            json.dump(data, fd, indent=4)

        print('{:d}/{:d} testing reviews written to {}'.format(
            len(data), reviews_count, os.path.basename(data_file)
        ))

    def _write(self):
        """
        Template method to write the training & testing data sets
        to the file system as JSON files:

            - movie_reviews_test.json
            - movie_reviews_train.json
        """
        reviews = list(self)
        reviews_count = len(reviews)
        pos = int(abs(self._review_count))
        train, test = reviews[:pos], reviews[pos:]

        self._write_reviews(test, 'test', reviews_count)
        self._write_reviews(train, 'train', reviews_count)

    def collect(self):
        """
        Collect all reviews from the file system (FS) &
        Dump it into JSON representation back to the FS

        Returns:
            int: The status code
        """
        status_code = 0
        try:
            self._read()
            self._write()
        except (OSError, IOError, FileNotFoundError, TypeError, ValueError) as error:
            status_code = -1
            if hasattr(error, 'code'):
                status_code = error.code
            if hasattr(error, 'errno'):
                status_code = error.errno
            print('Error while collecting movie reviews!', file=sys.stderr)
            print(str(error), file=sys.stderr)
        return status_code


def main():
    """
    Entry point

    Collect all reviews from the file system (FS) &
    Dump it into JSON representation back to the FS

    Returns:
        int: The status code
    """
    collector = Collector()
    return collector.collect()


if __name__ == '__main__':
    sys.exit(main())
