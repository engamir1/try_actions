import re
import time
from urllib.request import urlopen

# ====================================================================
# make code run every 2 hours
# import schedule
from bs4 import BeautifulSoup

from db import drop_tender_collection, insert_document, insert_many

# ====================================================================

my_data = []
# drop_tender_collection()


def show_Data(data, title, entity):
    # if len = 17 money required operation
    if len(data) >= 17:
        tender_title = title.text
        entity = entity
        # print(tender_title)
        # رقــم العملية شرائية/المزايدة:
        a = data[0].text
        # print(f'this is a :  {a}')
        # ناريخ التقديم:
        b = data[1].text
        # print(f'this is b :  {b}')
        # تاريخ فتح المظاريف:
        c = data[2].text
        # print(f'this is date_of_opining :  {c}')
        # نوع العملية شرائية/المزايدة:
        d = data[3].text
        # print(f'this is a1 :  {d}')
        # طبيعة العملية شرائية :
        e = data[4].text
        # print(f'this is b :  {e}')
        # الحالة:
        f = data[5].text
        # print(f'this is f :  {f}')
        # تاريخ الأعلان :
        f1 = data[6].text
        # print(f'this is f1 :  {f1}')
        # تقبل التجزئة:

        f2 = data[7].text
        # print(f'this is f2 :  {f2}')
        # توجد عروض بديلة:

        f3 = data[8].text
        # print(f'this is f3 :  {f3}')
        # نظام التقييم:

        f4 = data[9].text
        # print(f'this is f4 :  {f4}')
        # سعر كراسة الشروط للشركات الكبيرة:

        f5 = data[10].text
        # print(f'this is f5 :  {f5}')
        # التأمين الابتدائي:

        f6 = data[11].text
        # print(f'this is f6 :  {f6}')
        # سعر كراسة الشروط الصغيرة والمتناهية الصغرة

        f7 = data[12].text
        # print(f'this is f7 :  {f7}')

        # النشاط:
        f8 = data[13].text
        # print(f'this is f8 :  {f8}')
        # الوصف:
        f9 = data[14].text
        # print(f'this is f9 :  {f9}')

        # الشروط:
        f10 = data[15].text
        # print(f'this is f10 :  {f10}')

        # ملاحظات :
        f11 = data[16].text
        # print(f'this is f11 :  {f11}')
        x = {
            "tender_title": tender_title,
            "entity": entity,
            "purchase_no": a,
            "submission_date": b,
            "envelopes_opening_date": c,
            "purchase_type": d,
            "the_nature_purchasing": e,
            "status": f,
            "announcement_date": f1,
            "accept_retail": f2,
            "alternative_offers": f3,
            "evaluation_system": f4,
            "book_price_for_large_companies": f5,
            "insurance": f6,
            "micro_tender_book_price": f7,
            "activity": f8,
            "description": f9,
            "terms": f10,
            "notes": f11,
        }
        my_data.append(x)
        # insert_document(x)
    if len(data) == 13:
        tender_title = title.text
        entity = entity
        # print(tender_title)
        # رقــم العملية شرائية/المزايدة:
        a = data[0].text
        # print(f'this is a :  {a}')
        # ناريخ التقديم:
        b = data[1].text
        # print(f'this is b :  {b}')
        # تاريخ فتح المظاريف:
        c = data[2].text
        # print(f'this is date_of_opining :  {c}')
        # نوع العملية شرائية/المزايدة:
        d = data[3].text
        # print(f'this is a1 :  {d}')
        # طبيعة العملية شرائية :
        e = data[4].text
        # print(f'this is b :  {e}')
        # الحالة:
        f = data[5].text
        # print(f'this is f :  {f}')
        # تاريخ الأعلان :
        f1 = data[6].text
        # print(f'this is f1 :  {f1}')
        # تقبل التجزئة:

        f2 = data[7].text
        # print(f'this is f2 :  {f2}')
        # توجد عروض بديلة:

        f3 = data[8].text
        # print(f'this is f3 :  {f3}')
        # نظام التقييم:

        f4 = data[9].text
        # print(f'this is f4 :  {f4}')
        # سعر كراسة الشروط للشركات الكبيرة:

        f5 = data[10].text
        # print(f'this is f5 :  {f5}')
        # التأمين الابتدائي:

        f6 = data[11].text
        # print(f'this is f6 :  {f6}')
        # سعر كراسة الشروط الصغيرة والمتناهية الصغرة

        f7 = data[12].text
        # print(f'this is f7 :  {f7}')

        # # النشاط:
        # f8 = data[13].text
        # print(f'this is f8 :  {f8}')
        # # الوصف:
        # f9 = data[14].text
        # # print(f'this is f9 :  {f9}')

        # # الشروط:
        # f10 = data[15].text
        # # print(f'this is f10 :  {f10}')

        # # ملاحظات :
        # f11 = data[16].text
        # print(f'this is f11 :  {f11}')

        x = {
            "tender_title": tender_title,
            "entity": entity,
            "purchase_no": a,
            "submission_date": b,
            "purchase_type": c,
            "the_nature_purchasing": c,
            "status": e,
            "announcement_date": f,
            "accept_retail": f1,
            "alternative_offers": f2,
            "evaluation_system": f3,
            "activity": f4,
            "description": f5,
            "terms": f6,
            "notes": f7,
        }
        my_data.append(x)
        # insert_document(x)
        # if len = 0 this is search page
    if len(data) == 0:
        print(f" this is search page....")


# ====================================================================
pages = set()


def getLinks(url1):
    html = urlopen(f"{url1}")
    bs = BeautifulSoup(html, "html.parser")

    try:
        # title = (str(bs.find('h3', {'class': 'panel-title'}).get_text()))
        data = bs.find_all("span", {"class": "col-xs-6"})
        entity = bs.find_all("a", {"class": "col-xs-6"})
        if entity:
            entity = entity[0].text
        else:
            entity = None
        title = bs.find("h3", {"class": "panel-title"})
        show_Data(data, title, entity)
    except AttributeError:
        print("this page is missing something-- continue...")
    # except requests.exceptions.Timeout:
    #     print("Timeout occurred")
    #     getLinks(url1)

    #

    # https://etenders.gov.eg/Tender/DoSearch?status=3&page=1
    # (Tender)\/\d{0,8}|(DoSearchSorted)\/\d{0,9}|(\W(page)\W\d{0,100})
    # (Tender)\/\d{0,8}|(DoSearchSorted)\/\d{0,9}|(\Wpage\W\d{0,5})
    # (Tender)\/\d{0,8}|(DoSearchSorted)\/\d{0,9}|(\W*)(page=)\d{1}
    # Tender/(\d{,7})|(DoSearch\Wstatus=\d&page=\d{,3})
    # "/Tender\/(\d{,7})|(DoSearch\Wstatus=\d&page=2)
    # (https:\/\/etenders\.gov\.eg\/Tender/\d{,7})$|(DoSearch\Wstatus=\d&page=\d{,3})
    # (https:\/\/etenders\.gov\.eg\/Tender/\d{,7})$|https:\/\/etenders\.gov\.eg\/Tender/(DoSearch\Wstatus=\d&page=\d{,3})
    # (https:\/\/etenders\.gov\.eg\/Tender/\d{,7})$|https:\/\/etenders\.gov\.eg\/Tender/(DoSearch\?status=3&page=\d{1,100})
    total_links_in_page = bs.find_all(
        "a",
        href=re.compile(
            "/Tender/\d{,7}$|(https://etenders.gov.eg/Tender/)(DoSearch\?status=3)"
        ),
    )
    for link in total_links_in_page:
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newpage = link.attrs["href"]
                # pages.add(newpage)
                print(f"the url is :{newpage}")
                getLinks(newpage)


# ====================================================================
# start point for scraping in ==>  https://etenders.gov.eg/


def start_scrap(url: str):
    getLinks(url)
    drop_tender_collection()
    insert_many(my_data)
    # print(f"i inserted {len(my_data)}")


if __name__ == "__main__":
    start_scrap("https://etenders.gov.eg/")

# schedule.every().day.at("03:00:00").do(getLinks("https://etenders.gov.eg/"))
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# ====================================================================
# insert_many(my_data)

# يمكن الحصول على عمليات اكتر من التى يمكن التقدم لها بسبب وجود امر مباشر ولكن حالتها لا يمكن التقدم لها لذلك
# لم تحسب ضمن العمليات التى يمكن التقدم لها
# بالرغم من تواجدها فى العمليات التى يمكن التقدم لها
