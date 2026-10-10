Generate a subtitle file (SRT) for any video 

## Requirements

Worder requires [fast-whisper](https://github.com/SYSTRAN/faster-whisper) to transcribe the video file to generate timestamps and text.

```
pip install fast-whisper
```

## Usage 

First, you need to install Worder to get started: 

```
pip install worder
```

After successfully installing worder, you can use it as such: 

```
worder video.mp4
```

The command above will generate a SRT file with the same name as the given video at the same directory.
