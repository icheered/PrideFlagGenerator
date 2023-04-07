import csv
from PIL import Image, ImageDraw

def read_config_file(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        flag_definitions = []
        for row in reader:
            if not row:
                continue
            flag_def = (row[0], int(row[1]), row[2])
            flag_definitions.append(flag_def)
        
        result = []

        for item in flag_definitions:
            existing_item = next((i for i in result if i['name'] == item[0]), None)
            if existing_item is None:
                existing_item = {"name": item[0], "portions": [], "colors": []}
                result.append(existing_item)
            existing_item["portions"].append(item[1])
            existing_item["colors"].append(item[2])

        return result


def generate_flag(name: str, portions: list, colors: list, width: int, height: int):
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    total_portions = sum(portions)
    current_height = 0

    for portion, color in zip(portions, colors):
        portion_height = int(height * (portion / total_portions))
        draw.rectangle([(0, current_height), (width, current_height + portion_height)], fill=color)
        current_height += portion_height

    image.save(f'flags/{name}.png')
   


def main():
    config_file = "flags.csv"
    flag_definitions = read_config_file(config_file)

    width = 100
    height = 255
    for flag_definition in flag_definitions:
        generate_flag(flag_definition["name"], flag_definition["portions"], colors=flag_definition["colors"], width=width, height=height)


if __name__ == "__main__":
    main()