import time
import os
import pandas as pd
import wget
from bs4 import BeautifulSoup
import json
import requests
main_list = []
xx = 0

# made by hiren solanki........................................................................


for x in range(1,20):
    xx = xx + 1

    cookies = {
        'amplitude_id_fef1e872c952688acd962d30aa545b9eudemy.com': 'eyJkZXZpY2VJZCI6ImVjMDc0MTljLTQ4ZWMtNDM2NS04Nzc5LThkZmUzYmI1MTM1M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwNjIwMjQ3NDk5OCwibGFzdEV2ZW50VGltZSI6MTYwNjIwMjQ3NTQwNCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MSwic2VxdWVuY2VOdW1iZXIiOjJ9',
        'ud_firstvisit': '2021-05-04T15:27:20.103847+00:00:1ldwxE:2ItT7PEdSaHUkSZ7n-eIjIM1i3w',
        '__udmy_2_v57r': '332ed346398840f99ee574201e894b5a',
        'existing_user': 'true',
        'optimizelyEndUserId': 'oeu1620142044905r0.3981063295510878',
        'EUCookieMessageShown': 'true',
        '__ssid': 'd0a64add66fe3750109ec9260c39a0c',
        'G_ENABLED_IDPS': 'google',
        'ud_last_auth_information': '{\\"suggested_user_avatar\\": \\"https://img-c.udemycdn.com/user/50x50/anonymous_3.png?Expires=1624604988&Signature=OEPx8UlRnLzhm6MNFPI-axn~fCDvG4dkcHzMujp0NP~7Krkmx56xSXHmMg7YA3q0B-bO7lY6hF5iJAC9r~8DpKZvrRSOF5HKm1IekIGjSxFh13fWvLww76z0bsgyZG9DnWxJq9mbv36-kuBnwNpPv1BhGwsw4eRwnjRQnd3~iDdokFl0XWhpx1~~BVaPfptCx4bq9Mw2bYrhXhSpFxNJQTp3pFlUnNHGAc8Rgrefq~3YNzcCixgFKWtNLv-UEag3fcKv7avCQdO04cMaDlRHEzctbpSmx4BSoigdTGE461epoPpDRTNzO2jNSO9fmd0DfDxd2D6kfDwCpCaAptAgdw__&Key-Pair-Id=APKAITJV77WS5ZT7262A\\"\\054 \\"suggested_user_name\\": \\"Hirensolanki\\"\\054 \\"backend\\": \\"google\\"\\054 \\"suggested_user_email\\": \\"19it.hiren.solanki@gmail.com\\"}:1lwJUi:uBxbaF4m9WaGmIAwrC0Q8rA6CKA',
        'csrftoken': 'VDkQtqynPhRth8oCYcM1CCRcsrXGZuTRgrIvorx7IGcTbITQ008mWlD7vP8xVG75',
        'ki_r': '',
        'IR_PI': 'df2bb6bb-b2da-11ea-ab38-42010a246305%7C1625601808929',
        'stc111655': 'env:1625514999%7C20210805195639%7C20210705203328%7C8%7C1014624:20220705200328|uid:1620142057472.1269709263.6040921.111655.2042665879:20220705200328|srchist:1014623%3A1625513044%3A20210805192404%7C1014624%3A1625514999%3A20210805195639:20220705200328|tsa:1625514999965.843351221.6663966.6598557382933814.3:20210705203328',
        '_ga': 'GA1.2.1587946624.1606202476',
        'ki_t': '1620142055664%3B1625513147467%3B1625515425006%3B2%3B10',
        '_ga_7YMFEFLR6Q': 'GS1.1.1625514991.3.1.1625515452.8',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Wed+Jul+07+2021+12%3A53%3A16+GMT%2B0530+(India+Standard+Time)&version=6.10.0&hosts=&consentId=f8efa69b-88b4-4488-8755-434667227604&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0005%3A1%2CC0002%3A1%2CC0004%3A1%2CBG1%3A1&AwaitingReconsent=false',
        'muxData': 'mux_viewer_id=57e501fc-f427-44dc-8c9a-dd9cfe458fb2&msn=0.1638989094631651&sid=a8ae1ff3-6ca6-4f2a-9b57-d7eaa1c3cc05&sst=1626893266821&sex=1626894791775',
        'ud_cache_brand': 'INen_US',
        'ud_cache_language': 'en',
        'ud_cache_version': '1',
        'ud_cache_user': '',
        'ud_cache_modern_browser': '1',
        'ud_cache_price_country': 'IN',
        'ud_cache_logged_in': '0',
        'ud_cache_campaign_code': 'BILLIONSDAY21',
        'ud_cache_marketplace_country': 'IN',
        'ud_cache_release': 'ab5feba9c4ec204c453f',
        '__udmy_1_a12z_c24t': 'VGhlIGFuc3dlciB0byBsaWZlLCB0aGUgdW5pdmVyc2UsIGFuZCBldmVyeXRoaW5nIGlzIDQy',
        'ud_cache_device': 'desktop',
        'seen': '1',
        '__udmy_4_a12z': '56c806db2d4d44116df0996be19f79317dc858355f545c35df04c5019628db82',
        '__cf_bm': 'UBEMFlNV7HGmArZ.B5CUHi.s_Mfn70BkM9C8_WnY0tc-1633673218-0-AZtDSEOKOSFNek8JoSiAt/g1CXS9Cq0zYMskCk2sap1VXu8l2fcddN0zR1hBB8aRqrm4/MN5YeEGzJcw4ei8Osk=',
        '__cfruid': '108e2b96d6740349939233318c2fdf1ea5ef56a7-1633673218',
        'evi': '3@SdlYLPUUIss0NGPAYlFVCMVBpK6qS5EIGlwDmQQVGzEjn9jnFbu-8omEGVr92Cbup-2Xesnnr9TCvp2vneu-LCS1v3MSUOuPag9WSLq_GZubxJR_nhM4riVZ9mbg_I2MR2k7ttto_OIlqF0GdeIfpRzDTwz3F-orPLVEbWQ_69A6Ksy5PkSWZDqGkKYqD34=',
        'ud_rule_vars': 'eJxljstqwzAQRX_FaNvajB62R_MtBqHI41Q0RUSSswn596o0gYTArIZ77rlXUX0-cuXVXWKJNWXSWvGqzaQtooHNWuZxNgokozWH0VNI6TuyoE5cF7HFXOo_61ZfeWn_RShQsoe5B-wk0qjJwCDBGpQfAASwiM-WOvmG1rSHL1ez37YYXEl7DuwuPkd_ON3bCqcnILRI4buyxp8XJfZgOmkJFKl5mKW20_imzHzeubztlfC3FyYCbDcYQG3wAd_E7Rfcblfk:1mYj3A:o5Db-KZ3-Vml5pMeiOG7eQqhLLI',
        'eventing_session_id': 'kZdbj23oRFWRar9fmqvrLw-1633675088759',
    }

    headers = {
        'authority': 'www.udemy.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'x-udemy-cache-release': 'ab5feba9c4ec204c453f',
        'x-udemy-cache-user': '',
        'x-udemy-cache-modern-browser': '1',
        'x-udemy-cache-language': 'en',
        'x-udemy-cache-brand': 'INen_US',
        'x-requested-with': 'XMLHttpRequest',
        'x-udemy-cache-logged-in': '0',
        'x-udemy-cache-device': 'desktop',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'x-udemy-cache-version': '1',
        'x-udemy-cache-price-country': 'IN',
        'x-udemy-cache-marketplace-country': 'IN',
        'x-udemy-cache-campaign-code': 'BILLIONSDAY21',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.udemy.com/courses/development/web-development/?p=2',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('p', xx),
        ('page_size', '16'),
        ('subcategory', ''),
        ('instructional_level', ''),
        ('lang', ''),
        ('price', ''),
        ('duration', ''),
        ('closed_captions', ''),
        ('subs_filter_type', ''),
        ('subcategory_id', '8'),
        ('source_page', 'subcategory_page'),
        ('locale', 'en_US'),
        ('currency', 'inr'),
        ('navigation_locale', 'en_US'),
        ('skip_price', 'true'),
        ('sos', 'ps'),
        ('fl', 'scat'),
    )

    response = requests.get('https://www.udemy.com/api-2.0/discovery-units/all_courses/', headers=headers, params=params, cookies=cookies)

    response = response.text
    data  = json.loads(response)
    # print(data)
    data = data['unit']['items']


    for x in data:
        id = x['id']
        name = x['title']
        product_url = 'https://www.udemy.com/'+x['url']
        rating = x['rating']
        num_reviews = int(x['num_reviews'])
        content_info_short = x['content_info_short']
        paid = x['is_paid']

        headline = x['headline']

        objectives_summary = x['objectives_summary']
        num_subscribers = int(x['num_subscribers'])
        image = x['image_750x422']

        main_dir = {
            'cource_id':id,
            'cource_name':name,
            'cource_url':product_url,
            'rating':rating,
            'reviews':num_reviews,
            'content_info':content_info_short,
            'image':image,
            'cource_subscribers':num_subscribers,
            'summary': objectives_summary,
            'headline':headline,
            'cource_paid':paid,
        }
        main_list.append(main_dir)
        print(main_dir)
    print(len(main_list))


df = pd.DataFrame(main_list)
df.to_json('udemy.json', orient='records', lines=True)


print('script run successfully')
