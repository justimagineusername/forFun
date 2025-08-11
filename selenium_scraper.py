from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time


options = Options()
options.headless = True


driver = webdriver.Chrome(options=options)

try:
    url = "https://www.list.am/"
    driver.get(url)
    time.sleep(3)  # Զանգվածի լիարժեք բեռնում

    posts = driver.find_elements(By.CSS_SELECTOR, "a[href^='/item/']")

    results = []

    for post in posts:
        try:
            title = post.text.strip()
            link = post.get_attribute('href')
            results.append({"title": title, "link": link})
        except Exception:
            continue

    # Պահպանում CSV-ում
    with open("list_am_selenium_posts.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Պահպանվեց {len(results)} հայտարարություն list_am_selenium_posts.csv ֆայլում։")

finally:
    driver.quit()

