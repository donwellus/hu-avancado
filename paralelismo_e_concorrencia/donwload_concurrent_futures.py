import requests
import string
from time import time
import concurrent.futures

# from multiprocessing import Process, JoinableQueue, current_process
# from time import time, sleep

def image_download(country_code):
    image_name = f'{country_code}.gif'
    pic_url = f'http://localhost:8002/flags/{country_code}/{country_code}.gif'

    response = requests.get(pic_url, stream=True)
    if not response.ok:
        # print(f'{pic_url}: {response.status_code}')
        return

    with open(f'images/{image_name}', 'wb') as handle:
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

def create_country_list():
    return [
        f'{a}{b}'
        for a in string.ascii_lowercase[:26]
        for b in string.ascii_lowercase[:26]
    ]

def download_all(lst):
    for country in lst:
        image_download(country)

if __name__ == '__main__':
    elapsed = time()
    countries = create_country_list()
    n_workers = 26*26

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(image_download, c): c for c in countries}
        for future in concurrent.futures.as_completed(future_to_url):
            pass
            # url = future_to_url[future]
            # try:
            #     data = future.result()
            # except Exception as exc:
            #     print('%r generated an exception: %s' % (url, exc))
            # else:
            #     print('%r page is %d bytes' % (url, len(data)))

    print(f'Time: {time() - elapsed}')

    # consumers = [
    #     Thread(target=counter, args=[f'Serie-{i}', n])
    #     for i in range(n_thread)
    # ]


