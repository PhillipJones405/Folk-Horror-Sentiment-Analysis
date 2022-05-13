from Scweet.scweet import scrape

#fork the repo for Scweet here:
# https://github.com/Altimis/Scweet

data = scrape(words=['hereditary'], since="2018-06-08", until="2019-06-07", from_account=None, interval=1,
               headless=False, display_type="Top", save_images=False, lang="en",
               resume=False, filter_replies=False, proximity=True)

data.to_csv('hereditary.csv')

data2 = scrape(words=['saint maud'], since="2019-01-29", until="2022-04-28", from_account=None, interval=1,
              headless=False, display_type="Top", save_images=False, lang="en",
              resume=False, filter_replies=False, proximity=True)

data2.to_csv('st_maud.csv')


data1 = scrape(words=['midsommar'], since="2019-07-03", until="2019-08-04", from_account=None, interval=32,
               headless=False, display_type="Top", save_images=False,
               resume=False, filter_replies=False, proximity=True, lang="en")
data1.to_csv('midsommar.csv')
