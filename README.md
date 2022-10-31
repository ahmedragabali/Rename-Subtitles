# Rename Subtitles
Many TVs and media playing devices require the subtitle file to be named
exactly as the video file (execluding the extention) in order to be loaded
automatically. This is very easy for a movie file, you just have to rename 
one file. What about a season of a series!

This app takes the path to a season folder that have the video files and 
the subtitle files, then by a click of a button it matches and renames all
the subtitle files in the folder in a second.

## Restrictions
1. It doesn't take a whole series except if they are not in serparated folders.
2. Video files must be have one of these extentions only: (mp4, mkv, m4v)
3. Subtitle file must have (srt) extention
4. Video files and subtitle files must have this pattern (S__E__) in capital
    or in small letters anywhere in their name.

## Prerequisites
1. Install python 3.6
2. Create virtual environment
    ```
    <path>\python.exe -m venv .venv
    ```
3. Activate virtual environment .vnev (.venv/Scripts/activate.bat)
    ```
    .venv\Scripts\activate.bat
    ```
4. install fbs-tutorial package
    ```
    pip install fbs-tutorial
    ```


### Starting app
    fbs run

### Make portable app
    fbs freeze
 
### Make installer
    fbs freeze
    fbs installer
