# Sitemap-Checker
A Python crawler that can check your sitemap file straight from a given URL.

It works by providing the base URL of your site such as example.com/sitemap.xml, 
splitting each section to a pool workers which will crawl the whole section simultanously. 

Please remember to check that the starting URL is in fact the sitemaps of sitemaps otherwise it won't work.

---------------------------------------------------------------------------------------------------------
The product of this program is a csv for each section containing the following:
        Crawled URL | Status Code | Redirects | Comments
        
        example.com | 200 \ 400   | [0,inf.)  | "didn't wrote the full URL because it has a comma"
---------------------------------------------------------------------------------------------------------
