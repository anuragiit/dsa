import re
regex=r'\d{3}\.\d{2}\.\d{1}\.\d{2}'
matches=re.findall(regex,"""102.11.2.22,
102.23.3.33,
123.345.334.23,
109.23.4.12""")
for match in matches:
    print(match)

print(re.compile(r'\d{3}.*').search('123bgc'))

