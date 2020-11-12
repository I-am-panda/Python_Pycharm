# coding = utf-8
# 导包
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
# 引入Keys包
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    # 打开有道主页
    # driver.get("https://www.youdao.com/")
    # driver.find_element_by_name('q').send_keys("有道")
    # driver.find_element_by_tag_name('button').click()

    # 打开百度开发者平台
    driver.get("http://lbsyun.baidu.com/apiconsole/key#/home")
    driver.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn').click()
    driver.find_element_by_name('userName').send_keys(u"龙广998")
    driver.find_element_by_name('password').send_keys('1658176394')
    driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
    # 20秒寻找元素时间
    driver.implicitly_wait(20)
    driver.find_element_by_link_text('创建应用').click()
    # 构造“Select”对象
    select = Select(driver.find_element_by_tag_name('select'))
    # 取消所有选项的选中的状态
    # 注意：deslect_all()函数仅适用于带mutilple属性的select元素
    # select.deselect_all()
    # 根据元素的text内容定位选项
    # select.select_by_visible_text('微信小程序')
    # 根据元素的index定位选项
    # select.select_by_index(3)
    # 根据元素的value属性值定位选项
    # select.select_by_value('3')
    # 定位到下拉框
    down_list = driver.find_element_by_id('appType')
    # 再点击下拉框的选项
    down_list.find_element_by_xpath("//option[@value='21']").click()
    time.sleep(5)

    # 选择所有input元素
    inputs = driver.find_elements_by_tag_name('input')
    # 过滤出所有的checkbox并勾选之（属性TYPE值为checkbox则为复选框元素）
    for input in inputs:
        # 获取元素的某个属性值
        if input.get_attribute('type')  =='checkbox':
            input.click()
    # 等待两秒
    time.sleep(2)

    # 选择所有的checkbox元素
    # checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
    checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
    for check in checkboxes:
        # 勾选复选框
        check.click()
    print("复选框个数:%s" %(len(checkboxes)))

    # 去掉最后一个复选框
    checkboxes.pop(len(checkboxes)-1).click()
    time.sleep(2)
    driver.quit()



def test():
    # 创建谷歌浏览器实例
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开百度主页
    driver.get("https://www.baidu.com")
    print("标题：" + driver.title)
    # 找到百度搜索输入框
    search_text =driver.find_element_by_id('kw')
    # 输入内容
    search_text.send_keys('selenium')
    # 模拟回车键
    search_text.send_keys(Keys.ENTER)

    for i in range(5):
        # 退格删除字符
        search_text.send_keys(Keys.BACKSPACE)
    # 全选输入框内容
    search_text.send_keys(Keys.CONTROL,'a')
    # 复制输入框内容
    search_text.send_keys(Keys.CONTROL,'c')

    time.sleep(2)
    # 清空百度搜索输入输入框
    search_text.clear()
    # 通过name定位并且输入“Name”
    driver.find_element_by_name('wd').send_keys(u"Name")

    # 粘贴输入框内容
    search_text.send_keys(Keys.CONTROL, 'v')

    time.sleep(2)
    # 清空百度搜索输入输入框
    search_text.clear()
    # 通过标签元素定位并且输入“标签元素”
    search_input = driver.find_element_by_tag_name('input.s_ipt')
    search_input.send_keys('标签元素')

    time.sleep(2)
    # 清空百度搜索输入输入框
    search_text.clear()
    # 通过CSS Selector定位并且输入“CSS”
    search_text = driver.find_element_by_css_selector('#kw')
    search_text.send_keys('CSS Selector')

    time.sleep(2)
    # 清空百度搜索输入输入框
    search_text.clear()
    # 通过Xpath定位并且输入“Xpath”
    search_text = driver.find_element_by_xpath('//input[@id="kw"]')
    search_text.send_keys('Xpath')

    time.sleep(2)
    # 清空百度搜索输入输入框
    search_text.clear()
    # 通过CSS Selector定位并且输入“CSS”
    search_text = driver.find_element_by_css_selector('#kw')
    search_text.send_keys('CSS Selector')

    # 提交表单
    # search_text.submit()
    # 找到“百度一下”按钮并且点击
    button = driver.find_element_by_id('su')
    button.click()
    # 等待3秒
    time.sleep(3)
    # 5秒寻找元素时间
    driver.implicitly_wait(5)
    # 找到贴吧按钮并点击
    # 通过寻找文字链接（完整的）
    # tieba_button = driver.find_element_by_link_text('贴吧')
    # tieba_button.click()
    # 通过寻找文字链接（部分的）
    tieba_button = driver.find_element_by_partial_link_text('贴')
    tieba_button.click()

    try:
        #     等待页面刷新
        # WebDriverWait(driver,10).until(EC.title_contains('百度'))
        # 定时等待5秒
        time.sleep(2)
        print(driver.title)
    finally:
        driver.quit()

def test2():
    driver = webdriver.Chrome();
    # driver.get('http://ishouke.blog.sohu.com/')
    # blog_url = driver.find_element_by_id('blogUrl')
    # # 定位“首页”连接元素
    # home_page = blog_url.find_element_by_link_text('首页')
    # # 打印连接href属性
    # print(home_page.get_attribute('href'))


    # 打开百度主页
    # driver.get("https://www.baidu.com")
    driver.get("https://jqueryui.com/resources/demos/draggable/scroll.html")
    driver.implicitly_wait(5)
    # # 鼠标右键搜索按钮
    # chain = ActionChains(driver)
    # rt = driver.find_element_by_id("su")
    # chain.context_click(rt).perform()

    # # 鼠标双击搜索按钮
    # chain = ActionChains(driver)
    # rt = driver.find_element_by_id("su")
    # chain.double_click(rt).perform()

    # 找到需要拖拽的源元素位置
    source = driver.find_element_by_id('draggable3')
    # 找到需要拖拽的目标元素位置
    target = driver.find_element_by_id('draggable')
    # 构造动作类
    action = ActionChains(driver)

    # 开始拖拽
    action.drag_and_drop(source,target).perform()

    time.sleep(5)
    driver.quit()

def test3():
    # 创建谷歌浏览器实例
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开百度主页
    driver.get("https://www.baidu.com")
    print("标题：" + driver.title)
    # 找到百度搜索输入框
    search_text = driver.find_element_by_id('kw')
    # 输入内容
    search_text.send_keys('selenium')
    # 通过submit()来操作
    # 注意：submit()方法的使用前提是元素必须在表单范围内
    driver.find_element_by_id('su').submit()
    time.sleep(1)
    # 将页面滚动条拖动到底部
    js = 'document.documentElement.scrollTop=10000'
    driver.execute_script(js)

    time.sleep(1)

    # 将滚动条移动到页面的顶部
    js = 'document.documentElement.scrollTop=0'
    driver.execute_script(js)
    # 弹出警告框
    js = 'alert("警告！")'
    driver.execute_script(js)

    # 弹出警告对话框“确认”操作
    alter = driver.switch_to.alert
    alter.accept()

    # # 隐藏选中的元素
    # js = '$("#su").fadeOut();'
    # driver.execute_script(js)

    # arguments对象用来引用Arguments对象
    # fadeOut()方法用来淡出效果来隐藏被选元素
    button = driver.find_element_by_id('su')
    js = '$(arguments[0]).fadeOut()'
    driver.execute_script(js,button)

    print("标题：" + driver.title)


    # 当前窗口句柄
    current_handle = driver.current_window_handle
    driver.implicitly_wait(6)
    # 打开一个新窗口
    span  = driver.find_element_by_link_text('两岸进入准战争状态？国台办回应')
    span.click()
    # 切换窗口
    # 所有窗口句柄
    handles = driver.window_handles
    # 注意：如不用driver.switch_to.window(目标窗口)，在新页面查找元素会出现找不到元素的情况
    # 循环遍历窗口句柄
    for handle in handles:
        print(handle.title())
        # 判断当前窗口句柄是否为目标句柄
        if current_handle != handle:
            # 如果不是，跳转到原来窗口
            driver.switch_to.window(current_handle)

    time.sleep(3)
    driver.quit()

def test4():
    # 创建谷歌浏览器实例
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开百度主页
    driver.get("https://www.baidu.com")
    print("标题：" + driver.title)
    # 找到百度搜索输入框
    search_text = driver.find_element_by_id('kw')
    # 打印当前driver所在窗口中的网址
    current_web_url = driver.current_url
    print("搜索前的网址："+current_web_url)
    # 输入内容
    search_text.send_keys('selenium')
    # 通过submit()来操作
    # 注意：submit()方法的使用前提是元素必须在表单范围内
    driver.find_element_by_id('su').submit()

    # 打印当前driver所在窗口中的网址
    current_web_url = driver.current_url
    print("搜索后的网址：" + current_web_url)

    time.sleep(1)

    # 后退
    driver.back()
    current_web_url = driver.current_url
    print("后退后的网址"+current_web_url)

    # 设置浏览器的高、宽
    # 设置浏览器宽为400，高为800显示
    driver.set_window_size(400,800)

    time.sleep(2)

    # 前进
    driver.forward()

    # # 弹出警告框
    # js = 'alert("警告！")'
    # driver.execute_script(js)
    #
    # # 弹出警告对话框“确认”操作
    # alter = driver.switch_to.alert
    # alter.accept()
    #
    # time.sleep(1)

    # # 弹出对话框
    # js = 'confirm("你喜欢这个世界吗?");'
    # driver.execute_script(js)
    #
    # time.sleep(2)
    #
    # # 弹出确认对话框“取消”操作
    # alter = driver.switch_to.alert
    # # 取消
    # alter.dismiss()

    # time.sleep(2)
    #
    # # 弹出提示框
    # js = '''
    #         var name;
    #         name=prompt("请输入你的姓名?");
    #      '''
    # driver.execute_script(js)
    #
    # time.sleep(2)
    #
    # # 弹出提示框，确认操作
    # alter = driver.switch_to.alert
    #
    # # 获取对话框文字
    # print(alter.text)
    #
    # # 确认
    # alter.accept()

    time.sleep(5)
    driver.quit()

def test5():
    # 创建谷歌浏览器实例
    driver = webdriver.Chrome()
    # 测试选择下拉界面网站
    driver.get("http://www.script-tutorials.com/demos/87/index.html")
    driver.implicitly_wait(10)
    # 定位到下拉菜单面板
    ul = driver.find_element_by_id('nav')
    # 注意：针对这种鼠标移动到页面，自动弹出菜单的，用CSS或xpath，id等是无法一次到位的
    # 通过父标签[父标签属性名=父标签属性值]>子标签：nth-child(索引序号)
    # 定位到菜单项所在的小面板
    li = ul.find_element_by_css_selector('li:nth-child(2)')
    # 定位到菜单项并点击
    li.find_element_by_css_selector('ul>li>a').click()

    time.sleep(5)
    driver.quit()

def test6():
    driver = webdriver.Chrome()
    driver.get("http://www.115.com")
    driver.implicitly_wait(10)
    # account_button = driver.find_element_by_link_text('使用账号登录')
    # account_button.click()
    # driver.implicitly_wait(10)
    # account_input = driver.find_element_by_id('js-account')
    # account_input.clear()
    # account_input.send_keys('17620972194')
    # passwd_input = driver.find_element_by_id('js-passwd')
    # passwd_input.clear()
    # passwd_input.send_keys('Aa123456')
    # driver.find_element_by_id('js-submit').click()

    # 打开金十测试主站
    driver.get('https://dcdn-test.jin10.com/')
    chain = ActionChains(driver)
    driver.implicitly_wait(6)
    # 找到下拉菜单面板
    div = driver.find_element_by_class_name('left-navs')
    # 找到下拉面板下的子元素
    span = div.find_element_by_css_selector('div:nth-child(5)')
    # 鼠标移动到面板下的子元素
    chain.move_to_element(span).perform()
    # 点击
    driver.find_element_by_link_text('我的自选').click()

    # # 当前窗口句柄
    # current_handle = driver.current_window_handle
    # driver.find_element_by_link_text('免费注册').click()
    # # 所有窗口句柄
    # handles = driver.window_handles
    # # 循环遍历窗口句柄
    # for handle in handles:
    #     # 判断当前窗口句柄是否为目标句柄
    #     if current_handle != handle:
    #         # 如果不是，跳转到目标窗口
    #         driver.switch_to.window(handle)
    # chain = ActionChains(driver)
    # # 定位地区下拉列表
    # area_list = driver.find_element_by_css_selector('h5[rel="title"]')
    # chain.move_to_element(area_list).perform()
    # driver.implicitly_wait(5)
    # # 点击香港下拉菜单
    # driver.find_element_by_css_selector('a[data-btn="hk"]').click()
    # # 关闭注册页面
    # driver.close()
    # # 切换当前页面为原来的页面
    # driver.switch_to.window(current_handle)

    time.sleep(5)
    driver.quit()

def test7():
    driver = webdriver.Chrome()
    # 打开奶牛快传主页
    driver.get("https://cowtransfer.com/")
    # 要上传的文件
    driver.implicitly_wait(4)
    file_path = "D:\\test.txt"
    # 注意：不做判断，如果文件不存在，会一直弹出提示
    # 判断file_path是否为目录
    if True == os.path.isdir(file_path):
        raise Exception("ee：目录")
    # 判断文件是否存在
    if False == os.path.exists(file_path):
        raise Exception("ee：文件不存在")
    else:
        # 此方法仅对上传按钮为input标签有效
        # 定位上传按钮并上传本地文件
        driver.find_element_by_class_name('add-files-area').send_keys(file_path)

    # 切换frame
    driver.switch_to.frame('f1')
    driver.switch_to.frame('f2')

    # 添加等待时间，规定时间内，只要等待多久就等待多久
    try:
        # 等待到达十秒时，如果还找不到指定元素，则抛出一个TimeoutException异常
        # 如果未达到10秒，那么找到元素后停止等待，返回找到的元素
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,'statusImg'))
        print('找到元素')
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == '__main__':
    main()
    # test()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()