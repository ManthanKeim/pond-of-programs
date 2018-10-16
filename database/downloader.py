import sys
from PyQt5.QtWidgets import QProgressBar
from urllib import request

def download(url, filename):
    bar = QProgressBar(title='Downloading...', label=url)

    def report(block_count, block_size, total_size):
        if block_count == 0:
            bar.set(0, total_size)
        bar.inc(block_size)xx

    request.urlretrieve(url, filename, reporthook=report)

if __name__ == '__main__':
    url = input()
    filename = url.split("/") + ".jpg"
    download(url, filename)
