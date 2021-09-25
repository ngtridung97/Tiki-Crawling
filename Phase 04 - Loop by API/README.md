### Introduction
----------
We are moving to another option to crawl Tiki - using their API through "Inspect -> Network".

**Result**

![](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2004%20-%20Loop%20by%20API/Tiki_API.png?raw=true)

After finishing Category part, we should run a simple self-join query (temporarily using Pandas instead) to get leaf category list. After that, loop through each id, paging, ... to get full picture. Results simply stored in csv.

This method is faster than using Soup. Category list cost around 16 minutes, then 60 product can be get per second - tested on Thinkpad X13.

### Feedback & Suggestions
----------
Please feel free to fork, comment or give feedback to ng.tridung97@gmail.com