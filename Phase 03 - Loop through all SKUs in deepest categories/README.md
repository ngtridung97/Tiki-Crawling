### Introduction
----------
To continue the incomplete concept in Phase 02 - about getting all active Tiki's categories - or I mean the deepest category nodes, we gotta define a function that can scrape and store category list into PostgreSQL, as well as their relationship (Parent-Child pattern).

**Result**

![](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories/Category.png?raw=true)

After finishing Category part, we should run a simple self-join query like below to get a "deepest-category" list we want to loop through.
```sql
select
    a.category_id, a.category_name, a.url
from public.tiki_category as a
left join public.tiki_category as b
    on a.category_id = b.parent_id
where b.category_name is null;
```
Finally, we could re-use the script in Phase 02 for Product table.

In my opinion, I assume Tiki category list would have a structured format. That's why I think [Tiki_v2_Category.ipynb](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories/Tiki_v2_Category.ipynb), [Tiki_v2_Product.ipynb](https://github.com/ngtridung97/Tiki-Crawling/blob/master/Phase%2003%20-%20Loop%20through%20all%20SKUs%20in%20deepest%20categories/Tiki_v2_Product.ipynb) can be fired respectively weekly and daily in order to crawl a full week historical data.

### Feedback & Suggestions
----------
Please feel free to fork, comment or give feedback to ng.tridung97@gmail.com