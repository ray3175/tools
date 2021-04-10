import time
from multiprocessing import Manager
import requests
from bs4 import BeautifulSoup
from driver import Driver
from multi import multi_run
from db import DB


class Active:
    def __init__(self):
        self.url = "http://word.iciba.com"
        self.css_locator = {
            "class": ".main_l .cl>li",
            "course": ".study-speed-m.cl .c_panel",
            "study": ".fr>.word_button_blue",
            "word_area": ".mid .change-pic.cl .change-pic-mid.fl .change-pic-mid-box"
        }
        self.class_list = list()

    def get_class(self):
        driver = Driver()
        driver.maximize_window()
        driver.get(self.url)
        for element in driver.find_elements_by_css_selector(self.css_locator["class"]):
            class_id = element.get_attribute("class_id")
            has_child = element.get_attribute("has_child")
            title = element.find_element_by_tag_name("h3").text
            _class = {
                "name": title,
                "id": class_id,
                "url": []
            }
            if has_child == "1":
                sub_css_locator = ".main_l_box>ol>li"
                for sub_element in element.find_elements_by_css_selector(sub_css_locator):
                    sub_class_id = sub_element.get_attribute("class_id")
                    _class["url"].append({
                        "key": sub_class_id,
                        "value": f"{self.url}/?action=courses&classid={sub_class_id}"
                    })
            else:
                _class["url"].append({
                    "key": class_id,
                    "value": f"{self.url}/?action=courses&classid={class_id}"
                })
            self.class_list.append(_class)
        driver.close()
        driver.quit()
        return True

    def _get_course(self, _class, global_list, semaphore):
        semaphore.acquire()
        tmp_list = list()
        for url_dict in _class["url"]:
            url = url_dict["value"]
            class_id = url_dict["key"]
            flag_all = True
            while flag_all:
                sub_tmp_list = list()
                try:
                    driver = Driver()
                    driver.maximize_window()
                    driver.get(url)
                    flag = True
                    while flag:
                        time.sleep(5)
                        try:
                            driver.find_elements_by_css_selector(self.css_locator["course"])
                            flag = False
                        except:
                            print("课程页面获取失败，正在重试。。。")
                    for element in driver.find_elements_by_css_selector(self.css_locator["course"]):
                        course_id = element.get_attribute("course_id")
                        sub_tmp_list.append(f"{self.url}/?action=words&class={class_id}&course={course_id}")
                    driver.close()
                    driver.quit()
                    flag_all = False
                except:
                    print("课程driver丢失，正重新执行。。。")
            for i in sub_tmp_list:
                tmp_list.append(i)
        global_list.append({
            "name": _class["name"],
            "url": tmp_list
        })
        semaphore.release()
        return True

    def get_course(self):
        global_list = Manager().list()
        multi_run(self._get_course, self.class_list, global_list)
        self.class_list = global_list
        return True

    def _get_words(self, _class, global_list, semaphore):
        semaphore.acquire()
        tmp_list = list()
        for url in _class["url"]:
            flag_all = True
            while flag_all:
                sub_tmp_list = list()
                try:
                    driver = Driver()
                    driver.maximize_window()
                    driver.get(url)
                    flag_0 = True
                    while flag_0:
                        time.sleep(5)
                        try:
                            driver.find_element_by_css_selector(self.css_locator["study"]).click()
                            flag_0 = False
                        except:
                            print(f"单词概览页面获取失败，正在重试。。。链接是：{url}")
                    time.sleep(5)
                    flag_1 = False
                    try:
                        driver.find_elements_by_css_selector(self.css_locator["word_area"])
                        flag_1 = True
                    except:
                        print(f"单词详情页面进入失败，可能该单元没有单词，链接是：{url}")
                    if flag_1:
                        html = driver.page_source
                        bs = BeautifulSoup(html, "html5lib")
                        for word_area in bs.find("div", attrs={"class": "mid"}).find_all("div", attrs={"class": "change-pic cl"}):
                            word_area_sub = word_area.find("div", attrs={"class": "change-pic-mid fl"}).find("div", attrs={"class": "change-pic-mid-box"})
                            word_line = word_area_sub.find("div", attrs={"class": "word_sound_list"})
                            if english:=word_line.find("span", attrs={"class": "word"}):
                                english = english.get_text()
                            if phonetic_symbol:=word_line.find("span", attrs={"class": "sound"}):
                                phonetic_symbol = phonetic_symbol.get_text().replace(" ", "").replace("\n", "")
                            if audio_url:=word_line.find("a", attrs={"class": "icon_s2"}):
                                audio_url = audio_url.attrs.get("id")
                            flag_2 = True
                            while flag_2:
                                try:
                                    audio = requests.get(audio_url).content if audio_url else None
                                    flag_2 = False
                                except:
                                    print("单词音频获取失败，正在重试。。。")
                            chinese_line = word_area_sub.find("dl", attrs={"class": "word_sy"})
                            if chinese:=chinese_line.find("dd"):
                                chinese = chinese.get_text()
                            example_sentence_line = word_area_sub.find("dl", attrs={"class": "word_lj"})
                            example_sentence_list = list()
                            for bs_example_sentence in example_sentence_line.find_all("dd"):
                                example_sentence_english, example_sentence_chinese, *_ = bs_example_sentence.get_text("|", strip=True).split("|")
                                example_sentence_audio_url = bs_example_sentence.find("a").attrs.get("id")
                                flag_3 = True
                                while flag_3:
                                    try:
                                        example_sentence_audio = requests.get(example_sentence_audio_url).content if example_sentence_audio_url else None
                                        flag_3 = False
                                    except:
                                        print("例句音频获取失败，正在重试。。。")
                                example_sentence_list.append({
                                    "english": example_sentence_english,
                                    "chinese": example_sentence_chinese,
                                    "audio": example_sentence_audio
                                })
                            sub_tmp_list.append({
                                "english": english,
                                "chinese": chinese,
                                "phonetic_symbol": phonetic_symbol,
                                "audio": audio,
                                "example_sentence": example_sentence_list
                            })
                    driver.close()
                    driver.quit()
                    flag_all = False
                except:
                    print("单词driver丢失，正重新执行。。。")
            for i in sub_tmp_list:
                tmp_list.append(i)
        global_list.append({
            "name": _class["name"],
            "word_list": tmp_list
        })
        semaphore.release()
        return True

    def get_words(self):
        global_list = Manager().list()
        multi_run(self._get_words, self.class_list, global_list)
        self.class_list = global_list
        return True

    def write_in_db(self):
        return DB().write_data_in_db(self.class_list)


