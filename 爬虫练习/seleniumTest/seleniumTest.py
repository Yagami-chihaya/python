from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


bs = webdriver.Edge(executable_path='msedgedriver.exe')

try:
    bs.get("https://www.bilibili.com")
    bs.maximize_window()


    search_input = bs.find_element_by_class_name("nav-search-keyword")
    search_input.send_keys("嘉然今天吃什么")

    search_input.send_keys(Keys.ENTER)

    bs.switch_to.window(bs.window_handles[1])

    sleep(2)
    ranOfSpace = bs.find_element_by_css_selector('.face-img')
    print(ranOfSpace)
    ranOfSpace.click()

    bs.switch_to.window(bs.window_handles[2])


    bs.execute_script('window.confirm("好兄弟给然然点个关注吧，我求求你了呜呜QWQ")')
except:
    print("缺少浏览器驱动，请去官网下载")
finally:
    print("不管程序怎样，求你给然然点个关注吧呜呜呜")







