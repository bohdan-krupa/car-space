import argparse
from coordinates_generator import CoordinatesGenerator
from colors import COLOR_RED

def main():
    args = parse_args()
    image_file = args.image_file
    data_file = args.data_file

    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_RED)
            generator.generate()

def parse_args():
    parser = argparse.ArgumentParser(description='Create coordinates')

    parser.add_argument("--image",
                        dest="image_file",
                        required=True,
                        help="Image file to generate coordinates on")

    parser.add_argument("--data",
                        dest="data_file",
                        required=True,
                        help="Data file to be used with OpenCV")

    return parser.parse_args()


if __name__ == '__main__':
    main()