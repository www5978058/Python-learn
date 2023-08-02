"""
字符串判断 startswith endswith isalpha isdigit isalnum isspace
isalpha 是否纯字母
isdigit 是否纯数字
isalnum 是否字母或数字
isspace 是否是空白
"""
s = "hello world"
print(s.startswith("hello"))
print(s.endswith("hello"))
print("00".isdigit())
print(" ".isspace())
"""
True
False
True
True
"""