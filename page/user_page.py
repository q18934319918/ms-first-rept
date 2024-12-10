from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Userpage(BasePage):
    # 请登录
    ple_login = (By.CSS_SELECTOR,'a[href="#/app/login"]')
    # 会员中心
    vip_center = (By.XPATH,'//a[contains(text(),"会员中心")]')
    # 我的订单
    my_order = (By.CSS_SELECTOR, 'a[href="#/app/home/member/order"]')
    # 我的收藏
    my_fav = (By.CSS_SELECTOR, 'a[href="#/app/home/member/collection"]')
    # 我的收获地址
    my_address = (By.CSS_SELECTOR, 'a[href="#/app/home/member/receive"]')
    # 购物车
    shopping_cart = (By.CSS_SELECTOR, 'a[href="#/app/shoppingcart/cart"]')
    """注册功能"""
    #免费注册
    register = (By.CSS_SELECTOR,'a[href="#/app/register"]')
    #手机号
    register_mobile = (By.ID,'jsRegMobile')
    #免费获取验证码
    send_code = (By.ID,'jsSendCode')
    #输入手机验证码
    input_code = (By.ID,'jsPhoneRegCaptcha')
    #输入密码
    input_password = (By.ID,'jsPhoneRegPwd')
    #注册并登陆
    register_submit = (By.ID,'jsMobileRegBtn')
    #用户名
    user_name = (By.CSS_SELECTOR,'a[href="#/app/home/member/userinfo"]')
