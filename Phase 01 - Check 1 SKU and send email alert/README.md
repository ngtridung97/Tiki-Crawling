[Tiki](https://tiki.vn/) is one of the most popular e-commerce website in Vietnam. The purpose of this project is crawling as much as possible product information then reshape them in PostgreSQL. Scripts can be fired daily to collect historical pricing data for a week.

**Features:**
+ Database: [PostgreSQL 12.1 64-bit](https://www.postgresql.org/download/)
+ Language: [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
+ Libraries: [psycopg2](https://pypi.org/project/psycopg2/), [requests](https://pypi.org/project/requests/), [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
+ Platform: [Anaconda](https://www.anaconda.com/)
+ Sample Script: [Tiki_v1.ipynb](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Tiki_v1.ipynb)

See how it works below

### First approach - Loop through all main categories
----------
The idea is crawling every sub-pages of each category, which looks like the above image.

**Get html information by BS and category list**
```python
soup = get_web('https://tiki.vn')
categories = soup.findAll('a', {'class', "MenuItem__MenuLink-sc-181aa19-1 fKvTQu"})
category, link = [], []

for h in range(len(categories)):
    try:
        link.append(categories[h]['href'])
        category.append(categories[h].text)
    except:
        print('pass')
        
cat = list(zip(category,link))
```

**Main crawling function in 1 page**
```python
def crawl_insert(cat, j, articles, k, cur, conn, tablename):
    brand = articles[k]['data-brand'].strip().replace("'", "")
    category = cat[j][0]
    sub_category = articles[k]['data-category'].strip().replace("'", "")
    product = articles[k]['data-title'].strip().replace("'", "")
    product_id = articles[k]['data-seller-product-id'].strip()
    product_sku = articles[k]['product-sku'].strip()
    img = articles[k].img['src'].strip()
    final_price = articles[k].find_all('span', {'class': "final-price"})[0].text.strip().replace("đ", "").replace(".", "").split(' ')[0]
    regular_price = final_price if articles[k].find_all('span', {'class': "price-regular"}) == [] else articles[k].find_all('span', {'class': "price-regular"})[0].text.strip().replace("đ", "").replace(".", "").split(' ')[0]
    disc_perc = "0%" if articles[k].find_all('span', {'class': "sale-tag sale-tag-square"}) == [] else articles[k].find_all('span', {'class': "sale-tag sale-tag-square"})[0].text.strip().split(' ')[0]
    voucher = ["?" if articles[k].find_all('p', {'class': "price-tag"}) == [] else articles[k].find_all('span', {'class': "code"})[0].text][0]
    voucher_price = ["?" if articles[k].find_all('p', {'class': "price-tag"}) == [] else articles[k].find_all('span', {'class': "price"})[0].find('span').text.replace("đ", "").replace(".", "")][0]
    installment = ["?" if articles[k].find_all('span', {'class': "installment-price-v2"}) == [] else articles[k].find_all('span', {'class': "installment-price-v2"})[0].text][0]
    review = [articles[k].find_all('p', {'class': "review"})[0].text.strip('\(\)') if articles[k].find_all('p', {'class': "review"}) != [] else "Chưa có nhận xét"][0]
    rating = ["?" if articles[k].find_all('span', {'class': "rating-content"}) == [] else articles[k].find_all('span', {'class': "rating-content"})[0].find('span')['style'].split(':')[1]][0]
    product_link = 'https://tiki.vn' + articles[k].a['href']
    batch = strftime("%Y-%m-%d %H:%M:%S", localtime())
```

**Main crawling code in many pages**
```python
for j in range(len(cat)):
    soup = get_web(cat[j][1])
    articles = soup.find_all('div', {'class': "product-item"})
    print('Looping: ' + cat[j][1])
    for k in range(len(articles)):
        crawl_insert(cat, j, articles, k, cur, conn, tablename)

    links = soup.find_all('div', {'class': "list-pager"})
        
    # Exit while loop when reaching to the last page
    while links[0].find_all('a', {'class': "next"}) != []:
        soup = get_web('https://tiki.vn' + links[0].find_all('a', {'class': "next"})[0]['href'])
        articles = soup.find_all('div', {'class': "product-item"})
        print('Looping: ', cat[j][0], links[0].find_all('a', {'class': "next"})[0]['href'].split('&')[1], sep=' ')
        for i in range(len(articles)):
            crawl_insert(cat, j, articles, i, cur, conn, tablename)
        links = soup.find_all('div', {'class': "list-pager"})
        
print('Crawl done!')
```

**Result**

In the batch "26-June-2020", I collected 20255 records and I also notice the maximum page view per url is 209.

That's why I think with the above code, we can't crawl enough information due to limit in a number of page view. For examples: only category "Thiết Bị Số - Phụ Kiện Số" had around more than 1 millions item in that day.

That led to another thought about getting a fullfil information: get a list contain all links categories and sub-categories, then loop though every url of that list.

### Second approach - Loop through all main categories and sub categories urls
----------
The idea is just like 1st way, we need to append a list that gather all categories (both main and sub) from the website, then crawling every pages of them instead of only main categories.

In progress.

### Feedback & Suggestions
----------
Please feel free to fork, comment or give feedback to ng.tridung97@gmail.com