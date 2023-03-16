import json5
import ast

data = """{"comment": "手工用例"购买预付费中配置子机-DHCP-linux公共镜像-snap快照"关联的自动化用例"commontest.qcloud.CVM.LifeCycle.Create.CVM_Create_0010.Create"测试"通过"\n用例日志 http://cte.woa.com/tlog/3790200/11428425_20230307234614/commontest.qcloud.CVM.LifeCycle.Create.CVM_Create_0010.Create_20230307234711376.xml \n 测试任务 http://cte.woa.com/task/3790200", "comment_custom": "用例日志 http://cte.woa.com/tlog/3790200/11428425_20230307234614/commontest.qcloud.CVM.LifeCycle.Create.CVM_Create_0010.Create_20230307234711376.xml \n 测试任务 http://cte.woa.com/task/3790200", "fileArr": [], "status": "succeed", "steps": [], "type": "auto_testcase_update_result", "case_id": "7038756", "report_id": 0, "testcase_name": "购买预付费中配置子机-DHCP-linux公共镜像-snap快照", "automate_testcase_name": "commontest.qcloud.CVM.LifeCycle.Create.CVM_Create_0010.Create", "status_display": "通过", "data_succeed": , "data_fail": }"""
print(json5.loads(data))
# print(ast.literal_eval(json.dumps(data)))