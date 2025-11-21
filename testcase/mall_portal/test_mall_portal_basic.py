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

    @allure.story(next(c_id) + '登录 + 推荐商品 + 商品详情')
    @pytest.mark.parametrize(
        'base_info, testcase',
        get_testcase_yaml('./testcase/mall_portal/mall_logging.yaml')
    )
    def test_mall_portal_flow(self, base_info, testcase):
        """
        根据 YAML 定义的 baseInfo 和 testCase 执行接口请求。
        """
        # 动态设置用例标题，方便 Allure 报告展示
        allure.dynamic.title(testcase['case_name'])

        # 调用框架核心方法，根据 YAML 组合请求、断言和提取变量
        RequestBase().specification_yaml(base_info, testcase)



