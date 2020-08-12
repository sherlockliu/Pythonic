# ！/usr/bin/python
import re

def remove_sensitive_data(msg: str, sensitive_data: set) -> str:
    if not sensitive_data:
        return msg

    escaped_data = [re.escape(s) for s in sensitive_data]
    sensitive_data_re = re.compile(r"\b(" + "|".join(escaped_data) + r")\b".replace("+", "\+"), re.I)
    return sensitive_data_re.sub("***REDACTED***", msg)

print(remove_sensitive_data("358.7",['7']))
print(remove_sensitive_data("358.71",['7']))
print(remove_sensitive_data("abc c c c",[' c  ']))

# 358.***REDACTED***