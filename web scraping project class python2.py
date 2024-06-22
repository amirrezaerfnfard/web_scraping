# import library.
from urllib.request import urlopen
from bs4 import BeautifulSoup


# use functions for Additional sections.
def get_price_ranking(text_ranking: str):
    return float(
        text_ranking.get_text().replace("$", "").replace("\n", "").replace(",", "")
    )


def get_name_ranking(text_name_rank: str):
    return text_name_rank.get_text().replace(",", "").replace("\n", "")


def get_price_market(text_market: str):
    return float(
        text_market.get_text()
        .replace(",", "")
        .replace("", "")
        .replace("$", "")
        .replace("\n", "")
    )


def get_name_market(text_name_mark: str):
    return text_name_mark.get_text().replace(",", "").replace("\n", "")


# variable definition for program logic.
address_coinranknig = urlopen("https://coinranking.com/")
address_market = urlopen("https://coinmarketcap.com/")


coinranking_html = BeautifulSoup(address_coinranknig.read(), "lxml")
coinmarket_html = BeautifulSoup(address_market.read(), "lxml")


table_ranking = coinranking_html.find_all("div", {"class": "valuta"})
table_market = coinmarket_html.find_all("div", {"class": "sc-a093f09c-0 gPTgRa"})
name_ranking = coinranking_html.find_all("span", {"class": "profile__subtitle-name"})
name_market = coinmarket_html.find_all("div", {"class": "sc-1c5f2868-3 dhNyQP"})
value_ranking = 20
value_market = 20
count_ranking = 0
count_market = 0
math_count = 0

#  program logic.

for name_rank in range(0, 10, 1):
    count_ranking = count_ranking + 1
    price_name_ranking = get_name_ranking(name_ranking[name_rank])
    price_ranking = get_price_ranking(table_ranking[2 * name_rank])
    total_ranking = f"coinranking:{price_name_ranking} :{price_ranking}"
    print(total_ranking)

    print("-----------------------------------------")
print(
    "***************************************************************************************"
)
for name_mark in range(0, 10, 1):
    count_market = count_market + 1
    price_name_market = get_name_market(name_market[name_mark])
    price_market = get_price_market(table_market[name_mark])
    total_market = f"coinmraketcap:{price_name_market}: {price_market}"
    print(total_market)
    print("------------------------------------------")
    # for s in range(10):
    #     if price_market > price_ranking:
    #         print(f"{total_market}>{price_ranking}")
    #     elif price_market < price_ranking:
    #         print(f"{total_market}<{price_ranking}")

    if price_market > price_ranking:
        print(f"{total_market}  >  {total_ranking}")
    if price_market < price_ranking:
        print(f"{total_ranking}  >  {total_market}")
# print("THE END Program")


#  ENd the program
# print("THE END Program")
