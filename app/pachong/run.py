# 本爬虫的运行环境为 Win10 2004
# 爬取网站是 爱词吧（http://word.iciba.com），如有侵权，请联系我，QQ57464715
# 在运行前，请先建立好数据库 create database tools_english default charset utf8mb4;
# 同时，使用的第三方库如下：
# pip install selenium
# pip install requests
# pip install bs4
# pip install html5lib
# pip install sqlalchemy
# pip install pymysql


from active import Active
import time


def run():
    x = Active()
    print("*** 开始获取所有单词分类列表 ***")
    t_0 = time.time()
    x.get_class()
    t_1 = time.time()
    print(f"*** 耗时：{t_1 - t_0} ***")
    print("*** 开始获取所有单词分类中的所有课程 ***")
    x.get_course()
    t_2 = time.time()
    print(f"*** 耗时：{t_2 - t_1} ***")
    print("*** 开始获取所有单词分类中的所有词汇 ***")
    x.get_words()
    t_3 = time.time()
    print(f"*** 耗时：{t_3 - t_2} ***")
    print("*** 开始将爬取的数据写入数据库 ***")
    x.write_in_db()
    t_4 = time.time()
    print(f"*** 耗时：{t_4 - t_3} ***")


if __name__ == "__main__":
    run()

