def append_text_to_file(file_path, new_line):
    """
    将指定内容写入到指定的 txt 文件的最后一行

    参数:
      file_path: 文件路径
      new_line: 需要写入的文本内容
    """
    # 以追加模式打开文件（如果文件不存在则会创建）
    with open(file_path, 'a', encoding='utf-8') as file:
        # 如果文件内容不是空的，先写入一个换行符以确保内容在新的一行
        file.write('\n' + new_line)


