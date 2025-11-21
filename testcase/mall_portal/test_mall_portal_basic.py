import pytest
import allure

from base.generateId import m_id, c_id
from base.apiutil import RequestBase
from common.readyaml import get_testcase_yaml

@allure.feature(next(m_id) + 'mall‑portal接口测试')
class TestMallPortalBasic:
    """
    这是针对 mall‑portal 核心接口的自动化测试类。
    流程包括：会员登录 → 获取首页推荐商品列表 → 查询商品详情。
    """

    @allure.story(next(c_id) + "用户登录")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/mall_portal/mall_logging.yaml'))
    def test_logging(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "推荐商品列表")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/mall_portal/mall_list.yaml'))
    def test_logging(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "商品细节")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/mall_detail/mall_logging.yaml'))
    def test_logging(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)



