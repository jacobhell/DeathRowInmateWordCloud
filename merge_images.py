from os import listdir
from PIL import Image


def concatenate_images_h(image1, image2) :
    new_image = Image.new('RGB', (image1.width + image2.width, image2.height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    return new_image


def concatenate_images_v(image1, image2) :
    new_image = Image.new('RGB', (image1.width, image2.height + image1.height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, image1.height))
    return new_image


files = [int(file.rstrip('.png')) for file in listdir('figures/')]
files.sort()
files = [f'{file}.png' for file in files]

image = None
current_h_row = Image.open(f'figures/{files[0]}')

file_number_of_block = 1
files_added = 1
number_of_files = len(files)
for file in files[1:]:
    file_number_of_block += 1
    print(f'currently at file {file_number_of_block}')
    print('opening file ' + file)
    next_image = Image.open(f'figures/{file}')

    print('concatenating image')
    print(f'current hrw is none? {current_h_row is None}')
    if current_h_row is None:
        current_h_row = next_image
    else:
        current_h_row = concatenate_images_h(current_h_row, next_image)

    if file_number_of_block == 3:
        file_number_of_block = 0
        if image is None:
            image = current_h_row
        else:
            image = concatenate_images_v(image, current_h_row)

        print('setting current h row to none')
        current_h_row = None

    files_added += 1
    print(f'files_added:{files_added}')
    print(f'number_of_files:{number_of_files}')
    if number_of_files == files_added and current_h_row is not None:
        if image is None:
            image = current_h_row
        else:
            image = concatenate_images_v(image, current_h_row)

image.save('merged_image2.png', 'PNG')
