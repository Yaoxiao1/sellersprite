from utils import *
import time


product_research_url = "https://www.sellersprite.com/v2/product-research"
store_tracking_url = "https://www.sellersprite.com/v2/store-tracking"
driver = get_driver_from_local()


# sleep 5 seconds to see the page



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

def main():
    global driver
    # step1 open necessary tabs
    driver.get(product_research_url)
    print(driver.title)
    driver.implicitly_wait(5.)
    driver.execute_script(f"window.open(`{store_tracking_url}`, '_blank');")
    driver.switch_to.window(driver.window_handles[0])

    #step2 wait for user to login, and setup the initial page
    # 等待特定的 div 出现
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.container.p-0.pt-3')))
    print("特定的 div 已出现，继续执行后续操作")
    wait_for_user_login()
    print("user clicked")
    
    #step3 get all boxes
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.d-flex.flex-wrap.bg-white.pl-4.pr-4.pb-4.mb-4.position-relative')))
    container_div = driver.find_element(By.CSS_SELECTOR, 'div.d-flex.flex-wrap.bg-white.pl-4.pr-4.pb-4.mb-4.position-relative')
    content_boxes = container_div.find_elements(By.CSS_SELECTOR, 'div.content-grid-product-box')
    
    for box in content_boxes:
        process_content_boxes(box)
    driver.quit()


def wait_for_user_login():
    global driver
    inject_continue_button_script = """
    var button = document.createElement('button');
    button.innerHTML = '请设置好筛选条件后点击此按钮继续';
    button.id = 'continueButton';
    button.style.position = 'fixed';
    button.style.top = '10px';
    button.style.right = '10px';
    button.style.zIndex = '10000';
    document.body.appendChild(button);
    
    button.addEventListener('click', function() {
        window.continueClicked = true;
    });
    """
    driver.execute_script(inject_continue_button_script)

    # 等待用户点击继续按钮
    WebDriverWait(driver, 300).until(lambda driver: driver.execute_script("return window.continueClicked === true"))
    print("用户已点击继续按钮")


def process_content_boxes(box):
    global driver
    # 悬停到box上
    actions = ActionChains(driver)
    actions.move_to_element(box).perform()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-tips="去亚马逊查看"]')))
    
    # 找到a标签，其中data-tips="去亚马逊查看"
    try:
        amazon_link = box.find_element(By.CSS_SELECTOR, 'a[data-tips="去亚马逊查看"]')
        amazon_link.click()
        print("点击了去亚马逊查看的链接")
        # 切换到新打开的标签页
        driver.switch_to.window(driver.window_handles[-1])
        
        # 等待15秒
        time.sleep(15)
        
        # 关闭当前标签页
        driver.close()
        
        # 切换回原始标签页
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"未找到去亚马逊查看的链接: {e}")
    
    time.sleep(1000)



if __name__ == "__main__":
    main()