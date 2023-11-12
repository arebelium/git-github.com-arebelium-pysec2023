# Exercise 12
## Write a program which downloads file from the Internet
```python
url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
destination = url.split('/')[-1]
def download_file(url, destination):
    urllib.request.urlretrieve(url, destination, reporthook=show_progress_percentage)
    print("\nDownload complete!")
```
## Given you try and download a very large file then how do you monitor the progress? Research on urllib.urlretrieve() to solve this problem
2 ways of showing progress were explored: <br>
1. As percentage: <br>
```python
def show_progress_percentage(count, block_size, total_size):
    percentage = count * block_size * 100 / total_size
    print(f"Downloading... {percentage:.0f}% complete", end='\r')
```
2. As a progress bar: <br>
```python
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
```