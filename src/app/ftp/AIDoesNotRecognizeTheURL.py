import re

def remove_text_from_file(file_path, target_text):
    """
    从文件中删除指定的文本内容，并且删除目标内容左右的空白字符（如空格和换行）

    参数:
      file_path: 文件路径
      target_text: 需要删除的指定内容
    """
    # 以读取模式打开文件，读取所有内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 构造正则表达式，匹配目标文本及其左右的空白字符
    pattern = r'\s*' + re.escape(target_text) + r'\s*'
    new_content = re.sub(pattern, '', content)

    # 以写入模式重新写入修改后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


