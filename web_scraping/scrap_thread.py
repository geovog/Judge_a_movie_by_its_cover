import time as t
import csv
import os
import pandas as pd
import concurrent.futures
from bs4 import BeautifulSoup
import shutil
import requests

df = pd.read_csv("C:/Users/manta/Desktop/title-basics/data.tsv", sep="\t")
MAX_THREADS = 30
DIRECTORY = os.fsencode("C:/IMDB_dataset/temp/")
asd = df['startYear'].astype(str).str[:4]
df['startYear'] = pd.to_numeric(asd, errors='coerce')
rslt_df = df.loc[df['startYear'] > 1999]
rsltdf = rslt_df.loc[rslt_df['startYear'] < 2011]
rsltdf = rsltdf.reset_index(drop=True)

rsltdf = rsltdf[~rsltdf.titleType.str.contains("tvSeries")]
rsltdf = rsltdf[~rsltdf.titleType.str.contains("tvSpecial")]
rsltdf = rsltdf[~rsltdf.titleType.str.contains("tvEpisode")]
rsltdf = rsltdf[~rsltdf.titleType.str.contains("videoGame")]
rsltdf = rsltdf[~rsltdf.titleType.str.contains("video")]
rsltdf = rsltdf.reset_index(drop=True)

result = []

for value in rsltdf["tconst"]:
    result.append('https://www.imdb.com/title/' + value)
# add column 'urls'
rsltdf["urls"] = result


def download_url(url):
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
    content = requests.get(url, headers=header)
    soup = BeautifulSoup(content.text, 'html.parser')
    titlenamepart = url.split(sep='/')
    urlname = titlenamepart[4]
    try:
        the_url = soup.find("link", {"rel": "image_src"})['href']
        # the records with this png on their listing, did not have an image.
        if the_url == "https://m.media-amazon.com/images/G/01/imdb/images-ANDW73HA/imdb_fb_logo._CB1542065250_.png":
            pass
        else:
            the_url = the_url.split('_V1_', 1)[0]
            response = requests.get(the_url + '_V1_.jpg', stream=True)
            # save image
            with open(DIRECTORY + urlname + '.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            t.sleep(0.5)
    except Exception as e:
        print(e + " " + urlname)
        with open(r'exceptions', 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(urlname)
        pass


def download_img(img_urls):
    threads = min(MAX_THREADS, len(img_urls))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, img_urls)


def make_dataset():
    nameslist = []

    for file in os.listdir(DIRECTORY):
        filename = os.fsdecode(file)
        names = filename.split(sep='.')
        nameslist.append(names[0])

    dfnew = rsltdf[rsltdf['tconst'].isin(nameslist)]
    # drop rows which have no genre, in our case they had the '\N' value
    dfnew = dfnew[~dfnew.genres.str.contains(r'\\N')]
    dfnew.to_csv('new.csv', index=False)

    dfgroupped = dfnew[['originalTitle', 'startYear', 'genres']].groupby(['genres']).agg(['count'])
    print(dfgroupped)


def main(img_urls):
    download_img(img_urls)
    make_dataset()


main(result)
