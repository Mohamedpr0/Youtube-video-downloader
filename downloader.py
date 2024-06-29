from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if not stream:
            print("No progressive stream available")
            return
        
        print(f"Downloading '{yt.title}'...")
        stream.download(output_path)
        print("Download complete!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_folder = input("Enter the output folder path (leave blank for current directory): ").strip() or "./"
    
    download_video(video_url, output_folder)
