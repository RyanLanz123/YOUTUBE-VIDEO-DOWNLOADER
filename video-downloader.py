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

# Video URL
url = "https://www.youtube.com/shorts/s-O0oLqfBz4"
# Save path - Ensure it's a raw string or escape backslashes
save_path = r"C:\Users\ryanl\OneDrive\Desktop\Py Projects\YOUTUBE-VIDEO-DOWNLOADER"

# Call the download function
download_video(url, save_path)
