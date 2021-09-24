import requests
from collections import deque
import json
import re
import numpy as np
import pandas as pd
import os

category_path = 'Category_py.csv'
if os.path.exists(category_path):
    os.remove(category_path)

def get_web(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response

def get_main():
    url = 'https://tiki.vn/api/shopping/v2/mega_menu'
    data = get_web(url).json()

    cate_list = []
    i = 0
    for d in data['data']:
        try:
            query_id = re.findall('([1-9][0-9]*)', data['data'][i]['item']['url'])[0]
            title = data['data'][i]['item']['title']
            parent_id = '0'

            df = pd.DataFrame((query_id, title, parent_id)).T
            df.to_csv(category_path, sep='\t', encoding='utf-16', mode='a', header=False, index=False)
            cate_list.append((query_id, title, parent_id))
        except Exception as err:
            print(err)
        i += 1

    return cate_list

def get_sub(parent_cate):
    id = str(parent_cate[0])
    sub_url = 'https://tiki.vn/api/personalish/v1/blocks/listings?category='
    sub_data = get_web(sub_url + id).json()

    sub_cate_list = []
    if sub_data['filters'][0]['display_name'] == 'Danh Mục Sản Phẩm':
        i = 0
        for s in sub_data['filters'][0]['values']:
            try:
                query_id = str(sub_data['filters'][0]['values'][i]['query_value'])
                title = sub_data['filters'][0]['values'][i]['display_value']
                parent_id = parent_cate[0]

                df = pd.DataFrame((query_id, title, parent_id)).T
                df.to_csv(category_path, sep='\t', encoding='utf-16', mode='a', header=False, index=False)
                sub_cate_list.append((query_id, title, parent_id))
            except Exception as err:
                print(err)
            i += 1
            
    return sub_cate_list

def get_all(main_cate):
    queue = deque(main_cate)
    while queue:
        parent_cate = queue.popleft()
        category_list = get_sub(parent_cate)
        queue.extend(category_list)

main_cate = get_main()
get_all(main_cate)
print('Crawl done!')