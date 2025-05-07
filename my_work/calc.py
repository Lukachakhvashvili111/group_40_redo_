def download_time(file_size_gb, speed_mbps):
    file_size_mb = file_size_gb * 1024  
    speed_MBps = speed_mbps / 8         
    time_seconds = file_size_mb / speed_MBps

    minutes = int(time_seconds // 60)
    seconds = int(time_seconds % 60)

    return f"Estimated download time: {minutes} minutes {seconds} seconds"

# Your values
file_size_gb = 2
speed_mbps = 50


print(download_time(file_size_gb, speed_mbps))
