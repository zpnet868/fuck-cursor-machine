import shutil
import os
import json
import random
import re

def generate_random_machine_id():
    def replace_char(c):
        r = random.randint(0, 15)
        if c == 'x':
            v = r
        else:
            v = (r & 0x3) | 0x8
        return format(v, 'x')

    pattern = re.compile('[xy]')
    return pattern.sub(lambda m: replace_char(m.group()), 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx')



def update_installer():
    # 获取 %LOCALAPPDATA% 路径
    localappdata_path = os.getenv('LOCALAPPDATA')
    if not localappdata_path:
        print("[1]  无法获取 %LOCALAPPDATA% 路径")
        return

    # 构建目标路径
    target_dir = os.path.join(localappdata_path, 'cursor-updater')
    target_file = os.path.join(target_dir, 'installer.exe')

    # 如果目标路径不存在，则创建目录
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"[1]  创建目录: {target_dir} √")

    # 如果 installer.exe 存在，则删除
    if os.path.exists(target_file):
        os.remove(target_file)
        print(f"[1]  删除文件: {target_file} √")

    # 创建一个新的空 installer.exe 文件
    with open(target_file, 'w') as f:
        pass  # 创建一个空文件
    print(f"[1]  创建新的空文件: {target_file} √")




def add_to_hosts(ip, domain):
    # 获取 hosts 文件路径
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

    # 检查是否有管理员权限
    try:
        with open(hosts_path, 'r') as f:
            pass
    except PermissionError:
        print("[2]  请以管理员权限运行此脚本！")
        return

    # 检查是否已经存在该映射
    with open(hosts_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if domain in line and ip in line:
                print(f"[2]  '{ip} {domain}' 已存在于 hosts 文件中。√")
                return

    # 添加新的映射
    with open(hosts_path, 'a') as f:
        f.write(f'\n{ip}\t\t{domain}\n')
        print(f"[2]  成功添加 '{ip} {domain}' 到 hosts 文件。√")



def generate_random_machine_id():
    def replace_char(c):
        r = random.randint(0, 15)
        if c == 'x':
            v = r
        else:
            v = (r & 0x3) | 0x8
        return format(v, 'x')

    pattern = re.compile('[xy]')
    return pattern.sub(lambda m: replace_char(m.group()), 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx')

def modify_storage_json():
    # 获取 %APPDATA% 路径
    appdata_path = os.getenv('APPDATA')
    if not appdata_path:
        print("[3]  无法获取 %APPDATA% 路径")
        return

    # 构建 storage.json 文件路径
    storage_path = os.path.join(appdata_path, 'Cursor', 'User', 'globalStorage', 'storage.json')
    if not os.path.exists(storage_path):
        print(f"[3]  文件不存在: {storage_path}")
        return

    # 读取 storage.json 文件
    try:
        with open(storage_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[3]  读取文件失败: {e}")
        return

    # 生成新的随机值
    new_mac_machine_id = generate_random_machine_id()
    new_sqm_id = "{" + generate_random_machine_id() + "}"
    new_machine_id = generate_random_machine_id()
    new_dev_device_id = generate_random_machine_id()

    # 修改键值
    if "telemetry.macMachineId" in data:
        data["telemetry.macMachineId"] = new_mac_machine_id
    if "telemetry.sqmId" in data:
        data["telemetry.sqmId"] = new_sqm_id.upper()
    if "telemetry.machineId" in data:
        data["telemetry.machineId"] = new_machine_id
    if "telemetry.devDeviceId" in data:
        data["telemetry.devDeviceId"] = new_dev_device_id

    # 写回 storage.json 文件
    try:
        with open(storage_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("[3]  成功修改 storage.json 文件 √")
    except Exception as e:
        print(f"[3]  写入文件失败: {e}")


print("******* fuck-cursor-machine v1.0 2025/02/18 *******")
print("******* 适用于0.44.* *******")
print("******* 禁止自动更新, 修改机器码 *******")
print("******* https://github.com/zpnet868/fuck-cursor-machine *******")
# 屏蔽更新
update_installer()
add_to_hosts('127.0.0.1', 'download.todesktop.com')
# 调用方法
modify_storage_json()


# 示例用法
# print(generate_random_machine_id())