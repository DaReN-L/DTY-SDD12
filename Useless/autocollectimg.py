from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir':'roadsigns\stopsign\p'})

for i in range (1,100):
    google_crawler.crawl(keyword = 'Australian Stop Sign', filters=None,max_num=100,offset=0)