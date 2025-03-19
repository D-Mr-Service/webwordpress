# from ftplib import FTP
# import os
# import sys
# import time
#
# def upload_file(ftp, local_path, filename, retries=3, delay=5):
#     """
#     尝试上传文件，失败时进行重试
#     """
#     for attempt in range(1, retries + 1):
#         try:
#             with open(local_path, 'rb') as f:
#                 ftp.storbinary(f'STOR {filename}', f)
#             print(f"已上传: {filename}")
#             return True
#         except Exception as e:
#             print(f"尝试第 {attempt} 次上传 {filename} 失败，错误: {str(e)}")
#             if attempt < retries:
#                 time.sleep(delay)
#     return False
#
# def upload_to_ftp(local_dir, remote_path, host, user, password, port=21, timeout=120, passive_mode=True):
#     uploaded_files = []
#     failed_files = []
#     ftp = None
#     try:
#         # 连接FTP服务器并登录
#         ftp = FTP()
#         ftp.connect(host, port, timeout=timeout)
#         ftp.login(user, password)
#         ftp.set_pasv(passive_mode)
#         print("成功连接到FTP服务器")
#
#         # 调整套接字超时设置
#         ftp.sock.settimeout(timeout)
#
#         # 确保远程目录存在，如不存在则尝试创建
#         try:
#             ftp.cwd(remote_path)
#             print(f"远程目录存在: {remote_path}")
#         except Exception as e:
#             print(f"远程目录不存在，尝试创建: {remote_path}")
#             dirs = [d for d in remote_path.split('/') if d]
#             ftp.cwd('/')
#             for dir in dirs:
#                 try:
#                     ftp.cwd(dir)
#                 except Exception:
#                     ftp.mkd(dir)
#                     ftp.cwd(dir)
#             print(f"目录创建成功: {remote_path}")
#
#         # 定义图片文件后缀（大小写均可）
#         image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
#
#         # 上传本地目录中的图片文件
#         for filename in os.listdir(local_dir):
#             local_path = os.path.join(local_dir, filename)
#             if os.path.isfile(local_path) and os.path.splitext(filename)[1].lower() in image_exts:
#                 success = upload_file(ftp, local_path, filename)
#                 if success:
#                     uploaded_files.append(filename)
#                 else:
#                     failed_files.append(filename)
#
#         print(f"\n上传完成，总共成功上传 {len(uploaded_files)} 个文件")
#         if failed_files:
#             print("以下文件上传失败：")
#             for f in failed_files:
#                 print(f"  - {f}")
#         return uploaded_files, failed_files
#
#     except Exception as e:
#         print(f"操作过程中发生错误: {str(e)}")
#         return uploaded_files, failed_files
#
#     finally:
#         if ftp:
#             try:
#                 ftp.quit()
#             except Exception as e:
#                 print(f"在ftp.quit()时出错，尝试调用ftp.close()关闭连接: {str(e)}")
#                 ftp.close()
#             print("已断开FTP连接")
#
# if __name__ == "__main__":
#     # 配置参数，根据实际情况修改
#     local_dir = r'C:\Users\chenx\Pictures\Screenshots'
#     ftp_host = '154.201.92.67'
#     ftp_user = 'dsdsdsd'
#     ftp_pass = 'zK5LzmNWYz3rA73e'
#     ftp_port = 21
#     remote_path = '/'  # 目标远程目录
#     timeout = 120  # 设置超时时间为120秒
#     passive_mode = True  # 根据需要设置为True或False
#
#     # 执行上传操作
#     uploaded, failed = upload_to_ftp(local_dir, remote_path, ftp_host, ftp_user, ftp_pass, ftp_port, timeout, passive_mode)
#
#     print("\n上传结果总结：")
#     if uploaded:
#         print("已成功上传的文件：")
#         for f in uploaded:
#             print(f"  - {f}")
#     else:
#         print("没有文件上传成功。")
#
#     if failed:
#         print("上传失败的文件：")
#         for f in failed:
#             print(f"  - {f}")
#     else:
#         print("所有文件均上传成功。")
#
#     # 如果存在上传失败的文件，则以错误码退出
#     if failed:
#         sys.exit(1)
