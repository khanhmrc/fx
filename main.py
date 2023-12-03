import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta

# Khởi tạo đối tượng CurrencyRates
cr = CurrencyRates()

# Lấy dữ liệu tỷ giá giữa USD và EUR trong 30 ngày gần đây
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

dates = []
rates = []

current_date = start_date
while current_date <= end_date:
    rate = cr.get_rate('USD', 'EUR', date_obj=current_date)
    dates.append(current_date)
    rates.append(rate)
    current_date += timedelta(days=1)

# Tạo biểu đồ chứng khoán
plt.plot(dates, rates)
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.title('USD to EUR Exchange Rate')
plt.xticks(rotation=45)
plt.show()