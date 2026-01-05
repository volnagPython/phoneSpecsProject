import os
import json
import time
from playwright.sync_api import sync_playwright, Page , expect

def test_search_phone(page: Page):
    '''Search of the phone'''

    global phone_characteristics

    time_start = time.time()
    page.goto("https://brain.com.ua/ukr/")
    page.locator("input.quick-search-input:visible").fill("Apple iPhone 15 128GB Black")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("Результат пошуку за запитом "
                            "«Apple iPhone 15 128GB Black»")).to_be_visible()
    page.wait_for_load_state("networkidle")
    # print(page.url)
    # saved_url = page.url

    try:
        page.locator("xpath=//*[@class=\"br-pp-img br-pp-img-grid\"]/a/img[contains(@title,'Мобільний телефон"
                     " Apple iPhone 15 128GB Black (MTP03)  > ціни в Києві та Україні')]").click()
        expect(page.get_by_text("Мобільний телефон Apple iPhone 15 128GB Black (MTP03)"))

        page.wait_for_load_state("networkidle")
        print(f"✅ -- Our particular phone\'s page-- {page.url}")

    except TimeoutError as e:
        print(f"❌--This element was not found--: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
########################################################################
    print("********************  Основні характеристики   *************************")############
###################### Locating the web element and retrieving text##################
    try:
        # page.goto(current_page)

        charact2 = page.locator("//*[@id='br-pr-1']/h1")
        # charact2.wait_for()
        print(f"✅ Ім'я телефону : {charact2.text_content().strip()}")
    except TimeoutError as e:
        print(f"❌--This element was not found--: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
############### Форм -фактор t##################
    try:
        # page.goto(saved_url)
        page.wait_for_load_state("networkidle")
        charact1 = page.locator("xpath=//*[@id=\"br-pr-7\"]/div/div/div[1]/div/div[1]/span[2]/a")
        print(f"✅ Форм -фактор : {charact1.text_content()}")
    except TimeoutError as e:
        print(f"--This element was not found--: {e}")
    except Exception as e:
        print(f"--- The information was not found --- :{e}")
    finally:
        pass
########################## Колір ########################################
    try:
       # page.goto(current_page)
       page.wait_for_load_state("networkidle")
       charact3 = page.get_by_title("Колір чорний")
       print(f"✅ Колір : {charact3.text_content().strip()}")
    except TimeoutError as e:
       print(f"--This element was not found--: {e}")
    except Exception as e:
       print(f"--- The information was not found --- :{e}")
    finally:
       pass
######################### Повне імя ########################################
    try:
       #page.goto(current_page)
       page.wait_for_load_state("networkidle")
       charact4 = page.locator(".main-title").first.text_content()
       print(f"✅ Повне імя телефону: {charact4.strip()}")
    except TimeoutError as e:
       print(f"--This element was not found--: {e}")
    except Exception as e:
       print(f"--- The information was not found --- :{e}")
    finally:
       pass

# ################ Виробник #######################
    try:
        # page.goto(saved_url)
        page.wait_for_load_state("networkidle")
        charact5 = page.locator('//*[@id="br-pr-7"]'
                                '/div/div/div[11]/div/div[1]/span[2]')
        charact5.wait_for()
        print(f"✅ Виробник: {charact5.text_content().strip()}")
    except TimeoutError as e:
        print(f"--This element was not found--: {e}")
    except Exception as e:
        print(f"--- The information was not found --- :{e}")
    finally:
        pass
#################### Код ######################################
    try:
        # page.goto(saved_url)
        page.wait_for_load_state("networkidle")
        charact6 = page.locator(".br-pr-code-val").nth(0)
        # charact6.wait_for()
        print(f"✅ Код телефону : {charact6.text_content().strip()}")
    except TimeoutError as e:
        print(f"❌--This element was not found--: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
################################ Память #############################################
    try:
       # page.goto(saved_url)
       page.wait_for_load_state("networkidle")
       xpath1 = '//*[@class="br-pr-chr"]/div[4]/div/div/span[1]'
       xpath2 = '//*[@class="br-pr-chr"]/div[4]/div/div/span[2]'
       charact7 = page.locator(xpath1)
       charact8 = page.locator(xpath2)
       print(f"✅ {charact7.text_content().strip()} : "
             f"{charact8.text_content().strip()}")
    except TimeoutError as e:
       print(f"❌--This element was not found--: {e}")
    except Exception as e:
       print(f"❌--- The information was not found --- :{e}")
    finally:
       pass

########################## OS #####################
    try:
        charact9 = page.get_by_text("Операційна система").text_content()
        charact10 = page.get_by_title("Операційна система").text_content()
        print(f"✅ {charact9} : {charact10}")
    except TimeoutError as e:
        print(f"❌--This element was not found--: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
######################### Display size ################
    try:
        charact12 = page.locator('xpath=//*[@id="br-pr-7"]'
                                 '/div/div/div[2]/div/div[2]/span[2]')
        charact11 = page.get_by_text("Діагональ екрану")
        print(f"✅ {charact11.text_content()} : "
              f"{charact12.text_content().strip()}")
    except TimeoutError as e:
        print(f"❌--This element was not found--: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
######################### Ціна #########################
    try:
        charact14 = page.locator("xpath=//*[@class=\"br-pr-np\" "
                                 "and @data-pid=\"1044347\"]/div/span[1]")
        print(f"✅ Ціна: {charact14.text_content().strip()}  грн.")
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
####################### Акційна ціна ################
    try:
        charact15 = page.locator(".title-action-promo-price").first.text_content()
        aprice = charact15.strip()
        print("✅ Акційна ціна:", end="")
        if aprice == "":
            print(" - ")
        else:
            print(f"✅{aprice} грн.")
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
################# Роздільна здатність экрану ###########################
    try:
        charact16 = page.get_by_title("Роздільна здатність "
                                      "екрану 1179 х 2556")
        print(f"✅ Роздільна здатність экрану : {charact16.text_content()}")
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
######################## Кількість SIM-карт #############
    try:
        charact17 = page.get_by_title("Кількість SIM-карт 1 SIM + e-sim")
        print(f"✅ Кількість SIM-карт : {charact17.text_content()}")
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
#################### Формат SIM-карти ##############################
    try:
        charact18 = page.get_by_text("Формат SIM-карти")
        charact19 = page.locator("//*[@class=\"br-pr-chr\"]"
                            "/div[1]/div[1]/div[3]/span[2]").text_content()
        m = charact19.split()
        z = " ".join(m)
        print(f"✅ {charact18.text_content()} : {z}")
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
####################### Фото  телефону ##########################
    print("-------- Фото  телефону ------")
    # page.goto(current_page)
    page.wait_for_load_state("networkidle")
    images = page.locator(
        "xpath=//img[@title=\"Мобільний телефон Apple iPhone 15 128GB Black (MTP03) > ціни в Києві та Україні\"]").all()
    print(f"Found {len(images)} images:\n")
    photo_links = []
    for img in images:
        # Try 'src' first, then 'data-src'
        src = img.get_attribute("src")  # or img.get_attribute("data-src")
        if src:
            if any(src.lower().endswith(ext) for ext in
                   [".jpg", ".jpeg", ".webp"]):  # if at least one of the conditions is True.
                photo_links.append(src)
    print(f"--- Found {len(photo_links)} actual image links ---")
    for link in photo_links:
        print(link)
    print(70 * "-")

################### Printing all characteristics in dictionary at once ####################
    try:
        page.wait_for_selector("//div[contains(@class, 'br-pr-tblock')]")
        link1 = page.locator('//div[contains(@class, "br-pr-chr-wrap")]//span[1]')
        link2 = page.locator('//div[contains(@class, "br-pr-chr-wrap")]//span[2]')
        size1 = link1.count(); size2 = link2.count()
        k = [];v = [];size = 0
        if size1 >= size2:
            size = size2
        else:
            size = size1
        for i in range(size):
            o = link1.nth(i).text_content().strip()
            p = link2.nth(i).text_content().strip()
            m = p.split()
            z = " ".join(m)
            k.append(o)
            v.append(z)
        zippo = zip(k, v)
        phone_characteristics = dict(zippo)

        if phone_characteristics != {}:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "res_data.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(phone_characteristics, f, ensure_ascii = False, indent = 4)
            print(phone_characteristics)
        else:
            raise Exception
    except TimeoutError as e:
        print(f"❌-This element was not found-: {e}")
    except Exception as e:
        print(f"❌--- The information was not found --- :{e}")
    finally:
        pass
    time_end = time.time()
    span_time = time_end - time_start
    print("--- Tech data was collected in  :", round(span_time,2), "sec. ---")
    # Dec.11,2025

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        test_search_phone(page)
        browser.close()

        return phone_characteristics

if __name__ == "__main__":
    main()
