from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
product_research_url = "https://www.sellersprite.com/v2/product-research"
store_tracking_url = "https://www.sellersprite.com/v2/store-tracking"

driver.get(product_research_url)
print(driver.title)
driver.implicitly_wait(5.)
driver.execute_script(f"window.open(`{store_tracking_url}`, '_blank');")
driver.switch_to.window(driver.window_handles[0])

# sleep 5 seconds to see the page

time.sleep(5000)
driver.quit()

# step1 open necessary tabs
# step2 wait for user to login, after login both, press a button to trigger step3
# step3 get all boxes
# <div class="content-grid-product-box">
# loop
# 悬停到box上，找到<a>标签，其中data-tips="去亚马逊查看"，点进href,找到<a>标签，id="sellerProfileTriggerId",获取href中的seller的id
# 如果找到了seller的id，go step4
# step4 进入store-tracking页面，找到内容为添加店铺的按钮，点击，找到textarea标签，输入刚刚的seller的id，点击添加
# 找到button type="submit"，点击， 找到弹出的button type="button", 里面的<span>内容为"确定"，点击
# 找到tr,找到td class="align-middle", 往下找div class='td', 往下找div，里面有4个a标签，第一个标签提取href最后的days=7，第二个提取href最后的days=15
# 点击第一个a标签，找BSR不为空的tr
# 找button, type="button", data-days="15"，找BSR不为空的tr
# bsr不为空的tr找法，tr内部第3个td(从1开始)，下面的div class='td', 找button, 能trim成数字（格式是9,019这种，要考虑逗号，或者简单点，不是'-'就行）
# 完成后回到store-tracking页面，找到<input type="checkbox" id="checkbox_t000">, 选中， 找到button, id="remove-selected-all"，点击
# 弹出的框中找到button type="button" 内容是“确定”， 点击
# 继续step3的loop
# inject 一个按钮，点击停止