#輸入攝氏溫度 印出華氏溫度 temperature

c_temperature = input('請輸入攝氏溫度：')
c_temperature = float(c_temperature)
f_temperature = c_temperature * 9 / 5 + 32
print('攝氏 ', c_temperature, ' 度 = 華氏 ', f_temperature, ' 度')

