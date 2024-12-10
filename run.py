import time
from time import sleep

import pytest
import os

if __name__ == '__main__':
    # 1.执行测试用例
    pytest.main()
    time.sleep(3)
    #2.生成报告
    os.system("allure generate report -o allure-report --clean")
    time.sleep(3)
    #3.打开报告
    os.system("allure open allure-report")