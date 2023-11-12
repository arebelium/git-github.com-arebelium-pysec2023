import progressbar
import urllib.request

bar = None

def show_progress_percentage(count, block_size, total_size):
    percentage = count * block_size * 100 / total_size
    print(f"Downloading... {percentage:.0f}% complete", end='\r')

def show_progress_bar(count, block_size, total_size):
    global bar
    if bar is None:
        bar = progressbar.ProgressBar(maxval=total_size)
        bar.start()

    downloaded = count * block_size
    if downloaded < total_size:
        bar.update(downloaded)
    else:
        bar.finish()
        bar = None

def download_file(url, destination):
    urllib.request.urlretrieve(url, destination, reporthook=show_progress_bar)
    print("\nDownload complete!")

# download an example password file from github
url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
destination = url.split('/')[-1]
download_file(url, destination)
