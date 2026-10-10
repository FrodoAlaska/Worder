from faster_whisper import WhisperModel 
import time

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

# Create the model 

start = time.perf_counter()

print("[INFO]: Creating the model...")
model = WhisperModel("small", device="cpu", compute_type="int8")
print("[INFO]: Successfully created the model...\n")

# Transcribe the file 

print("\n[INFO]: Transcribing the video...")
video_path     = "assets/video.mp4" # @TODO
segments, info = model.transcribe(video_path)
print("[INFO]: Finished transcribing the video...\n")

# Create the SRT file

print("\n[INFO]: Writing the SRT file...")
write_srt(segments, "assets/video.srt")
print("[INFO]: Successfully created the SRT file!\n")

# Print useful info

elapsed = time.perf_counter() - start 
print(f"\n[INFO]: Transcribing took {elapsed:0.4f}s")
