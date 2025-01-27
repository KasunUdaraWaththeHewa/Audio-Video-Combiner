from moviepy import VideoFileClip, AudioFileClip
import os


def combine_audio_video(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all files in the source folder
    all_files = sorted(os.listdir(source_folder))

    # Separate video and audio files
    video_files = [f for f in all_files if not f.endswith("-audio.mp4")]
    audio_files = [f for f in all_files if f.endswith("-audio.mp4")]

    for video in video_files:
        # Match the corresponding audio file
        # Remove the resolution and frame rate part in parentheses
        base_name = video.rsplit(" (", 1)[0]
        audio = f"{base_name}-audio.mp4"  # Construct the expected audio filename
        video_path = os.path.join(source_folder, video)
        audio_path = os.path.join(source_folder, audio)

        # Skip if audio file is not found
        if not os.path.exists(audio_path):
            print(f"Audio file not found for {video}. Skipping...")
            continue

        output_path = os.path.join(output_folder, video)

        try:
            # Load video and audio clips
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            # Set the audio to the video
            video_with_audio = video_clip.with_audio(audio_clip)

            # Export the combined video
            video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

            print(f"Successfully processed: {output_path}")

        except Exception as e:
            print(f"Error processing {video} and {audio}: {e}")


# Define folder paths
source_folder = "Videos Seperated"
output_folder = "Videos Combined"

combine_audio_video(source_folder, output_folder)
