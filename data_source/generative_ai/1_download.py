file_links = [
    {
        "title": "Real-time Scene Text Detection with Differentiable Binarization",
        "url": "https://arxiv.org/pdf/1911.08947"
    },
    {
        "title": "General OCR Theory",
        "url": "https://arxiv.org/pdf/2109.10282"
    },
    {
        "title": "Attention is all you need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "MobileNet",
        "url": "https://arxiv.org/pdf/1704.04861"
    },

]

import os
import wget

def is_exist(file_link):
    return os.path.exists(f"./{file_link['title']}.pdf")

for file_link in file_links:
    if not is_exist(file_link):
        wget.download(url=file_link['url'], out=f"./{file_link['title']}.pdf")

