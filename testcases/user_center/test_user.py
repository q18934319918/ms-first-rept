import time
from time import sleep

import allure

from page.user_page import Userpage
from testcases.user_center.conftest import delete_user, delete_code
from utils.assert_util import assert_compare
from utils.mysql_util import db
from utils.read import read_yaml


@allure.epic("美客生鲜项目")
@allure.feature("用户中心")
class TestUser:
    @allure.title("未登录时跳转")
    def test_go_login(self,driver_project):
        #实例化page
        page = Userpage(driver_project)
        with allure.step("点击请登录"):
            page.click(page.ple_login)
        actual_url = page.get_current_url()
        expected_url = "http://meikefresh.5istudy.online/#/app/login"
        assert_compare(expected_url,"==",actual_url)
        page.back()
        page.move_to_element(page.vip_center)
        with allure.step("点击我的订单"):
            page.click(page.my_order)
        actual_url = page.get_current_url()
        assert_compare(expected_url, "==", actual_url)
        page.back()
        page.move_to_element(page.vip_center)
        with allure.step("点击我的收藏"):
            page.click(page.my_fav)
        actual_url = page.get_current_url()
        assert_compare(expected_url, "==", actual_url)
        page.back()
        page.move_to_element(page.vip_center)
        with allure.step("点击我的收货地址"):
            page.click(page.my_address)
        actual_url = page.get_current_url()
        assert_compare(expected_url, "==", actual_url)
        page.back()
        with allure.step("点击我的购物车"):
            page.click(page.shopping_cart)
        page.switch_to_window()
        actual_url = page.get_current_url()
        assert_compare(expected_url, "==", actual_url)
        page.close_driver()
        page.switch_to_window(to_parent_window=True)

    def test_register(self,driver_project):
        data = read_yaml()['register_ok']
        page = Userpage(driver_project)
        with allure.step("点击免费注册"):
            page.click(page.register)
        with allure.step("输入手机号"):
            page.send_keys(page.register_mobile,data['mobile'])
        with allure.step("点击获取验证码"):
            page.click(page.send_code)
            time.sleep(2)
        with allure.step("获取短信验证码"):
            sql = f"select code from users_verifycode where mobile = {data['mobile']} order by id desc limit 1;"
            code = db.select_db_one(sql)['code']
        with allure.step("输入验证码"):
            page.send_keys(page.input_code,code)
        with allure.step("输入密码"):
            page.send_keys(page.input_password,data['password'])
        with allure.step("点击注册并登陆"):
            page.click(page.register_submit)
        test = page.get_text(page.user_name)
        assert_compare(str(data['mobile']),"==",test)
        time.sleep(3)
        delete_user(data['mobile'])
        delete_code(data['mobile'])





