# EXIF data synchronizer

Script written in purpose of synchronization order of photos from multiple cameras captured with timestamps different from it should be. 

## Usage
First of all, enter valid information into `CAMERAS`, `DIRECTORY_PATH` and `IMAGE_EXTENSION` variables.

### Camera models and time difference
If you struggle to find your camera model signature, use `check_camera_model()` function.

As `'time_difference'` it is meant the time difference (**in minutes**) between time of capture and EXIF datetime_original.

**For example:**
If photo was captured at ***12:35:00***, but EXIF data shows ***12:10:00***
`'time_difference'` is **-25**.

**REMEMBER** - each camera needs to have corresponding time_difference.

After entering all needed data, just run the script.