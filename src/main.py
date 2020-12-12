import csv


class Image:
    date = None
    magical_value = None

    def __init__(self, date, magical_value):
        self.magical_value = magical_value
        self.date = date


def get_closest_pairs(num_of_pairs, date):
    index = 0
    for index, image in enumerate(images):
        if image.date == date:
            break
    else:
        index = -1

    if index == -1:
        raise ValueError("Given date does not exist in input file")

    for i in range(1, num_of_pairs+1):
        if index - i >= 0:
            print(images[index - i].date, " - ", date)

    for i in range(1, num_of_pairs+1):
        if index + i <= len(images):
            print(date, " - ", images[index + i].date)


if __name__ == '__main__':

    images = []  # I will use this hashMap to store given image data.

    with open('input/input_list.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row_num = 0
        for row in csv_reader:
            if row_num != 0:
                image = Image(date=row["Date"], magical_value=row["Magic Value"])
                images.append(image)
            row_num = row_num + 1
    images.sort(key=lambda img: img.date)

    get_closest_pairs(3, "2016-02-14")


