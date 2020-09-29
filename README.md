[Tiki](https://tiki.vn/) is one of the most popular e-commerce websites in Vietnam. The purpose of this project is crawling as much as possible product information, then reshape them in PostgreSQL. Scripts can be fired daily to collect historical pricing data for a week.

**Features:**
+ Database: [PostgreSQL 12.1 64-bit](https://www.postgresql.org/download/)
+ Language: [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
+ Libraries: [psycopg2](https://pypi.org/project/psycopg2/), [requests](https://pypi.org/project/requests/), [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [smtplib](https://docs.python.org/3/library/smtplib.html)
+ Platform: [Anaconda](https://www.anaconda.com/)
+ Sample Scripts: [Tiki_v2_Category.ipynb](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories/Tiki_v2_Category.ipynb), [Tiki_v2_Product.ipynb](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories/Tiki_v2_Product.ipynb)

See how it works below

### Introduction
----------
[Phase 01](https://github.com/ngtridung97/Tiki-Crawling/tree/master/Phase%2001%20-%20Check%201%20SKU%20and%20send%20email%20alert) - Gather product URLs list, apply conditions, send an email whether that condition was met.

[Phase 02](https://github.com/ngtridung97/Tiki-Crawling/tree/master/Phase%2002%20-%20Loop%20through%20all%20SKUs%20in%2016%20main%20categories) - Gather 16 main-category URLs list, loop until the last page of each URL.

[Phase 03](https://github.com/ngtridung97/Tiki-Crawling/tree/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories) - Gather an active main-and-sub category list, classify all "deepest-category" URLs, loop until the last page of each URL.

Phase 04 - Gather all product URLs in Phase 03, add on other SKUs options (In Progress).

Phase 05 - Call Tiki's Category and Product API (In Progress).

### Feedback & Suggestions
----------
Please feel free to fork, comment or give feedback to ng.tridung97@gmail.com
