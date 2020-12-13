import csv
import datetime
import sys

""" 
    I have used this tutorial for CSV part(s).
    https://realpython.com/python-csv/
"""

# Helper class to hold Image values
class Image:
    date = None
    magical_value = None

    def __init__(self, date, magical_value):
        self.magical_value = float(magical_value)
        self.date = date


# Helper function for part 1
def get_closest_pairs(num_of_pairs, date):
    # First find given date
    index = 0
    for index, image in enumerate(images):
        if image.date == date:
            break
    else:
        index = -1

    # If given date DNE raise Error.
    # In theory, this should not happen at all since we're iterating already existing list
    if index == -1:
        raise ValueError("Given date does not exist in input file")

    """for i in range(1, num_of_pairs+1):
        if index - i >= 0:
            print(images[index - i].date, " - ", date)"""

    with open('output/3-pairs-output.csv', mode='a+', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(1, num_of_pairs + 1):
            if index + i < len(images):
                # print(date + "," + images[index + i].date)
                csv_writer.writerow([date, images[index + i].date])


# Helper function for part 2
def get_pairs_in_window(window, date):
    # First find given date
    index = 0
    for index, image in enumerate(images):
        if image.date == date:
            break
    else:
        index = -1

    # If given date DNE raise Error.
    # In theory, this should not happen at all since we're iterating already existing list
    if index == -1:
        raise ValueError("Given date does not exist in input file")

    with open('output/18-day-pair.csv', mode='a+', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        selected_date = datetime.date.fromisoformat(date)
        # This selects the closest next date and substracts two days to see if its within window
        while index + 1 < len(images):
            next_date = datetime.date.fromisoformat(images[index + 1].date)
            if (next_date - selected_date).days <= window:
                # print(date + "," + images[index+1].date)
                csv_writer.writerow([date, images[index + 1].date])
            index += 1


# Helper function for part 3
def get_pairs_in_window_with_threshold(window, date):
    # First find given date
    index = 0
    for index, image in enumerate(images):
        if image.date == date:
            break
    else:
        index = -1

    # If given date DNE raise Error.
    # In theory, this should not happen at all since we're iterating already existing list
    if index == -1:
        raise ValueError("Given date does not exist in input file")

    with open('output/18-day-pair-with-threshold.csv', mode='a+', newline='') as output:

        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        base_index = index

        selected_date = datetime.date.fromisoformat(date)
        # This selects the closest next date and substracts two days to see if its within window
        while index + 1 < len(images):
            next_date = datetime.date.fromisoformat(images[index + 1].date)
            rating = (images[base_index].magical_value * images[index + 1].magical_value) % 16
            if (next_date - selected_date).days <= window and rating >= 8:
                # print(date + "," + images[index+1].date)
                csv_writer.writerow([date, images[index + 1].date, "{:.5E}".format(rating)])
            index += 1


if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError("Invalid input parameters. Please write num_of_pairs and window value")
    elif not sys.argv[1].isnumeric():
        raise ValueError("Invalid num of pairs parameter, it should be integer")
    elif not sys.argv[2].isnumeric():
        raise ValueError("Invalid window parameter, it should be integer")

    _NUM_OF_PAIRS = int(sys.argv[1])
    _WINDOW = int(sys.argv[2])

    images = []  # I will use this list to store given image data.

    # I will read the input and store it in a list. Each value will be Image object
    with open('input/input_list.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row_num = 0
        for row in csv_reader:
            image = Image(date=row["Date"], magical_value=row["Magic Value"])
            images.append(image)
            row_num = row_num + 1

    # Then I will sort this list based on Image's Date field.
    images.sort(key=lambda img: img.date)

    # Part 1
    # Ready the output file with correct headers
    with open('output/3-pairs-output.csv', mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Date A", "Date B"])

    for img in images:
        get_closest_pairs(_NUM_OF_PAIRS, img.date)

    # Part 2
    # Ready the output file with correct headers
    with open('output/18-day-pair.csv', mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Date A", "Date B"])

    for img in images:
        get_pairs_in_window(_WINDOW, img.date)

    # Part 3
    # Ready the output file with correct headers
    with open('output/18-day-pair-with-threshold.csv', mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Date A", "Date B", "Magic Value"])

    for img in images:
        get_pairs_in_window_with_threshold(_WINDOW, img.date)
