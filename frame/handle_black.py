import yaml


def handle_black(fun):
    def run(*args,**kwargs):
        instance_self=args[0]
        with open("../frame/black_list.yaml","r",encoding="utf-8") as f:
            black_lists = yaml.load(f)
        # 捕获异常（找不到元素）
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            #遍历黑名单
            for black in black_lists:
                #如果发现黑名单中的元素存在
                ele=instance_self.driver.find_elements(*black)
                #对黑名单的元素进行处理
                if len(ele)>0:
                    #通过点击的方式，关闭弹窗
                    ele[0].click()
                    # 再次查找
                    return instance_self.find(*args,**kwargs)
            raise e
    return run