import csv


class Image:
    date = None
    magical_value = None

    def __init__(self, date, magical_value):
        self.magical_value = magical_value
        self.date = date


# Writer function for part 1
def get_closest_pairs(num_of_pairs, date):

    # First find given date
    index = 0
    for index, image in enumerate(images):
        if image.date == date:
            break
    else:
        index = -1

    # If given date DNE raise Error. In theory, this should not happen at all since we're iterating already existing list
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


if __name__ == '__main__':

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
        get_closest_pairs(3, img.date)

    
