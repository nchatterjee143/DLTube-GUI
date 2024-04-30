import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import run
from threading import Thread
import yt_dlp

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title('YouTube Downloader')

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Enter your search query:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.query_entry = ttk.Entry(self.root, width=40)
        self.query_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        ttk.Button(self.root, text="Download Audio (MP3)", command=self.download_audio).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        ttk.Button(self.root, text="Download Video (MP4)", command=self.download_video).grid(row=1, column=2, padx=10, pady=5, sticky='w')

    def download_audio(self):
        query = self.query_entry.get()
        if query.strip() == '':
            messagebox.showerror("Error", "Please enter a search query.")
            return

        self.download_thread = Thread(target=self.start_audio_download, args=(query,))
        self.download_thread.start()

    def start_audio_download(self, query):
        try:
            self.root.title("Downloading MP3...")
            run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', '%(title)s.%(ext)s', '--embed-thumbnail', '--embed-metadata', f'ytsearch:"{query}"'])
            self.root.title('YouTube Downloader')
            messagebox.showinfo("Success", "Audio download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def download_video(self):
        query = self.query_entry.get()
        if query.strip() == '':
            messagebox.showerror("Error", "Please enter a search query.")
            return

        self.download_thread = Thread(target=self.start_video_download, args=(query,))
        self.download_thread.start()

    def start_video_download(self, query):
        try:
            self.root.title("Downloading MP4...")
            run(['yt-dlp', '--recode-video', 'mp4', '-o', '%(title)s.%(ext)s', f'ytsearch:"{query}"'])
            self.root.title('YouTube Downloader')
            messagebox.showinfo("Success", "Video download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
