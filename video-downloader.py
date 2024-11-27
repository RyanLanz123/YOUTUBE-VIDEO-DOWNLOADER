from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        # Filter MP4 streams and get the highest resolution
        highest_res_stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    return folder  # Return the selected folder path

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:  # Ensure the returned folder path is valid
        print(f"Selected folder: {save_dir}")
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")
