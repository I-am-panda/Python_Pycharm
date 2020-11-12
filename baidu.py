from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
    login_name = driver.find_element_by_id('username')
    login_name.send_keys('13800138006')
    password = driver.find_element_by_id('password')
    password.send_keys('123456')
    driver.find_element_by_id('verify_code').send_keys('1')
    driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').send_keys('手机')
    driver.find_element_by_xpath('//*[@id="sourch_form"]/a').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[3]/div/div[1]/a/img').click()
    driver.find_element_by_id('join_cart').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a').click()
    driver.find_element_by_xpath('//*[@id="hd-my-cart"]/a/div/span').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a').click()
    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    main();