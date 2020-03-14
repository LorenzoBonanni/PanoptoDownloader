import sys
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import urllib.request

options = Options()
options.add_extension("config/elicpjhcidhpjomhibiffojpinpmmpil.crx")
driver = webdriver.Chrome(executable_path="config/chromedriver", options=options)
config_file_name = "config/config.yaml"
with open(config_file_name) as f:
    config_file = yaml.load(stream=f, Loader=yaml.BaseLoader)
    username = config_file["username"]
    password = config_file["password"]


def get_videos() -> dict:
    """
    open video config files, retrieves data and returns it
    :return:
    """

    with open("config/videos.yaml", 'r') as v:
        return yaml.load(stream=v, Loader=yaml.BaseLoader)


def login():
    """
    goes to panopto main page and makes login
    :return:
    """

    driver.get("https://univr.cloud.panopto.eu/Panopto/Pages/Home.aspx")
    button = driver.find_elements_by_id("loginButton")[0]
    button.click()
    button = driver.find_elements_by_class_name("input-wrapper")[1]
    button.click()
    username_field = driver.find_element_by_id("IDToken1")
    username_field.send_keys(username)
    password_field = driver.find_element_by_id("IDToken2")
    password_field.send_keys(password)
    send_button = driver.find_element_by_class_name("btn")
    send_button.click()


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = min(int(count*block_size*100/total_size),100)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def download_video(subject: str, url: str):
    """
    download video lessons
    :param subject: the subject of the video that is being downloaded
    :param url: the url from which the program will download the file
    :return:
    """

    try:
        driver.get(url)
        # wait till the page is completely load
        time.sleep(5)
        # save lesson name
        lesson = driver.find_elements_by_id("deliveryTitle")[0].text
        # locate the extension on the screen searching for its icon
        v = pyautogui.locateOnScreen("./config/icon.png", confidence=.5)
        # click extension button
        pyautogui.click(x=v[0], y=v[1], clicks=1, interval=0.0, button="left")
        # click download button
        pyautogui.click(x=v[0], y=v[1] * 2, clicks=1, interval=0.0, button="left")
        source_tag = driver.find_element_by_tag_name("source")
        file_name = f"{subject} {lesson}"
        print("\n" + file_name)
        urllib.request.urlretrieve(source_tag.get_attribute("src"), f"output/{file_name}.mp4", reporthook)
    finally:
        pass

def main():
    login()
    videos = get_videos()
    for subject in videos:
        for url in videos[subject]:
            download_video(subject, url)
    driver.quit()


if __name__ == '__main__':
    main()
