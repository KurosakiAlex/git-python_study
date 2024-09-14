import speedtest

def monitor_speed():
    st = speedtest.Speedtest()

    # 测量下载速度
    download_speed = st.download() / 1024 / 1024  # 转换单位为Mbps

    # 测量上传速度
    upload_speed = st.upload() / 1024 / 1024  # 转换单位为Mbps

    # 输出结果
    print(f"下载速度：{download_speed:.2f} Mbps")
    print(f"上传速度：{upload_speed:.2f} Mbps")


if __name__ == "__main__":
    monitor_speed()

