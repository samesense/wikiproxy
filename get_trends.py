"""Get trending RSS URLs and put in newsbeuter url file"""
import os, random, local_settings

def get_trend_urls():
    """wget twitter URL and parse out URLs"""

    trends = []
    twitter = 'http://search.twitter.com/'
    tmp = 'tmp' + str(random.randint(0,1000))
    os.system('wget %s --output-document=%s' % (twitter, tmp))
    with open(tmp) as f:
        for line in f:
            if 'a href' in line and 'search?q' in line:
                trends.append(twitter
                              + line.split('a href=\"/')[1].split('\"')[0])
    os.system('rm %s' % tmp)
    return trends                
    
def main():
    """GO"""

    trend_urls = {}
    for t in [url.replace('search?',
                          'search.atom?')
              for url in get_trend_urls()]:
        trend_urls[t] = True

    # load old feeds
    with open(local_settings.newsbeuter_urls) as f:
        for line in f:
            trend_urls[line.strip()] = True
            
    with open(local_settings.newsbeuter_urls, 'w') as f:
        for trend_url in trend_urls:
            f.write(trend_url + '\n')

main()




