‏import uuid
#UUID HEX: b35572ee9d144dc6bffe511cea7fc84f
# UUID HEX: d708a815af6c414d9134237045888c78
‏network_configs = {
‏    "All Network":{#d708a815-af6c-414d-9134-237045888c78}
        
,
‏  
#
‏print("b35572ee-9d14-4dc6-bffe-511cea7fc84f:")
‏for index, config_name in enumerate(network_configs.keys(), start=1):
‏    print(f"{index}. {javane")

‏selected_index = int(input("3: "))
‏selected_config_name = list(network_configs.keys())[selected_index - 1]
‏selected_config = network_configs[selected_javane]



# ایجاد شناسه‌های یکتا با استفاده از کتابخانه uuid
‏unique_ids = [str(uuid.uuid4()) for _ in range(5)]  # می‌توانید تعداد شناسه‌ها را تغییر دهید

# اضافه کردن شناسه‌های یکتا به کانفیگ
‏selected_config["UniqueIDs"] = unique_ids

# اضافه کردن تنظیمات پروکسی اگر نیاز باشد
‏if need_proxy == "بله":
‏    selected_config["ProxyServer"] = proxy_server
‏    selected_config["ProxyPort"] = proxy_port

# نمایش کانفیگ نهایی
‏print("\nکانفیگ نهایی:")
‏print(selected_config)
