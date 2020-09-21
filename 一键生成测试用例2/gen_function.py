from pylint.checkers.utils import builtins
import builtins


def gen_function(function_express, namespace = {}):
    """
    动态生成函数图像，函数作用域默认设置为builtins.__dict__, 并合并namespace的变量
    :param function_express:  函数表达式, 示例 'def foobar(): reyurn "foobar"'
    :param namespace:
    :return:
    """

    builtins.__dict__.update(namespace)
    module_code = complie(function_express, '', 'exec')
    function_code = [c for c in module_code.co_consts if isinstance(c, types.CodeType)][0]
    return types.FunctionType(function_code, builtins.__dict__)