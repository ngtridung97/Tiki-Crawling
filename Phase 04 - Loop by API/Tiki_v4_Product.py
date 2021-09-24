import requests
import json
import pandas as pd
import os

category_path = 'Product.csv'
if os.path.exists(category_path):
    os.remove(category_path)

def get_web(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response

def get_prod(cate_id):
    prod_url = 'https://tiki.vn/api/personalish/v1/blocks/listings?category='
    prod_data = get_web(prod_url + str(cate_id)).json()

    start_page = int(prod_data['paging']['from'])
    end_page = int(prod_data['paging']['last_page'])

    prod_list = []
    for i in range(start_page, end_page + 1):
        prod_page_url = prod_url + str(cate_id) + '&page=' + str(i)
        prod_page_data = get_web(prod_page_url).json()

        j = 0
        for d in prod_page_data['data']:
            query_id = prod_page_data['data'][j]['id']
            sku_id = prod_page_data['data'][j]['sku']
            prod_name = prod_page_data['data'][j]['name']
            brand_name = prod_page_data['data'][j]['brand_name']
            price = prod_page_data['data'][j]['price']
            origin_price = prod_page_data['data'][j]['original_price']
            discount_perc = prod_page_data['data'][j]['discount_rate']
            stock_qty = prod_page_data['data'][j]['stock_item']['qty']
            sold_qty = 0 if prod_page_data['data'][j]['quantity_sold'] is None else prod_page_data['data'][j]['quantity_sold']['value']
            review_count = prod_page_data['data'][j]['review_count']
            rating_avg = prod_page_data['data'][j]['rating_average']
            seller_id = prod_page_data['data'][j]['seller_product_id']
            cate_id = cate_id
            
            df = pd.DataFrame((query_id, sku_id, prod_name, brand_name, price, origin_price, discount_perc, stock_qty, sold_qty, review_count, rating_avg, seller_id, cate_id)).T
            df.to_csv(category_path, sep='\t', encoding='utf-16', mode='a', header=False, index=False)
            prod_list.append((query_id, sku_id, prod_name, brand_name, price, origin_price, discount_perc, stock_qty, sold_qty, review_count, rating_avg, seller_id, cate_id))
            j += 1
            
    return prod_list

get_prod('1795')