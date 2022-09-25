from exif import Image
from datetime import datetime
from datetime import timedelta

from pathlib import Path

# As 'time_difference' it is meant the time difference (in minutes) between
# time of capture and EXIF data datetime_original

# For example:
# If photo was captured at 12:35:00, but EXIF data shows 12:10:00
# 'time_difference' is -25

# Enter camera data (enter as many cameras as you want)
# Remember, each camera needs to have corresponding time_difference
CAMERAS = {
    # if you don't know your camera model, use check_camera_model() to check
    'model': ['Camera model 1', 'Camera model 2'],

    # in minutes
    'time_difference': [-35, -47]
}

# Datetime format usually used by cameras, change if needed
DATETIME_FORMAT = '%Y:%m:%d %H:%M:%S'

# Relative or absolute path to directory, where photos are stored (Script traverse subdirectories too)
DIRECTORY_PATH = 'CHANGE IT'

# Extension to look for
IMAGE_EXTENSION = 'jpg'


def check_camera_model(filepath):
    image_to_check = Image(filepath)
    if image_to_check.has_exif:
        print(image_to_check.model)
    else:
        print("This image does not have exif data")


if __name__ == '__main__':

    if len(CAMERAS['model']) != len(CAMERAS['time_difference']):
        print('Number of cameras and time_differences does not match. Entered %d cameras and %d time_differences'
              % (len(CAMERAS['model']), len(CAMERAS['time_difference'])))
        exit()

    for path in Path(DIRECTORY_PATH).rglob('*' + IMAGE_EXTENSION):

        current_image = Image(path)

        if current_image.model in CAMERAS['model']:
            model_index = CAMERAS['model'].index(current_image.model)

            datetime_original = datetime.strptime(current_image.get('datetime_original'), DATETIME_FORMAT)
            new_datetime_original = datetime_original - timedelta(minutes=CAMERAS['time_difference'][model_index])

            # Update exif data
            current_image.set('datetime_original', new_datetime_original.strftime(DATETIME_FORMAT))

            # Saves exif data back into original file
            with open(path, 'wb') as modified_image:
                modified_image.write(current_image.get_file())