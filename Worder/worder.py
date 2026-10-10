from faster_whisper import WhisperModel 
from pathlib        import Path

import time
import sys
import argparse as ap

### Functions ### 

def format_time(secs):
    hours    = int(secs / 3600)
    minutes  = int((secs % 3600) // 60)
    seconds  = int(secs % 60) 
    mseconds = int((secs % 1 ) * 1000)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{mseconds:03d}"

def write_srt(segments, path):
    print("[INFO]: Transcribing lines...")
    with open(path, "w", encoding="utf-8") as file: 
        for i, seg in enumerate(segments, start=1):
            file.write(f"{i}\n")
            file.write(f"{format_time(seg.start)} --> {format_time(seg.end)}\n")
            file.write(f"{seg.text.strip()}\n\n")

### Functions ### 

### Main ###

def main():
    # Parse the CLI arguments 

    video_path  = ""
    output_path = ""

    parser = ap.ArgumentParser(prog="worder", description="Generate subtitles from videos", usage="%(prog)s \"path/to/video.mp4\"")
    parser.add_argument("path", type=str, help="The path to the video")

    # Use the arguments 
    args = parser.parse_args()

    # Make sure that there are actually arguments

    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Check for the other arguments

    if not args.path:
        print("[ERROR]: Invalid path!")
        return

    # Use the given path 

    video_path  = args.path 
    output_path = str(Path(video_path).with_suffix(".srt"))

    # Create the model 

    start = time.perf_counter()

    print("[INFO]: Creating the model...")
    model = WhisperModel("small", device="cpu", compute_type="int8")
    print("[INFO]: Successfully created the model...\n")

    # Transcribe the file 

    print("\n[INFO]: Transcribing the video...")
    segments, info = model.transcribe(video_path, task="translate")
    print("[INFO]: Finished transcribing the video...\n")

    # Create the SRT file

    print("\n[INFO]: Writing the SRT file...")
    write_srt(segments, output_path)
    print("[INFO]: Successfully created the SRT file!\n")

    # Print useful info

    elapsed = time.perf_counter() - start 
    print(f"\n[INFO]: Transcribing took {elapsed:0.4f}s")

### Main ### 
