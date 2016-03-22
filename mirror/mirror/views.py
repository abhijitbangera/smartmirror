from django.shortcuts import render,redirect
from datetime import timedelta,datetime,date,time
import pywapi
from lxml import html
import requests

def mypage(request):
	weather_com_result = pywapi.get_weather_from_weather_com('INXX0012')
	date1=date.today()
	time1=datetime.now().time()
	weather_type=weather_com_result['current_conditions']['text']
	temperature=weather_com_result['current_conditions']['temperature']
	Location="Bangalore"
	humidity=weather_com_result['current_conditions']['humidity']
	result = pywapi.get_weather_from_yahoo('INXX0012', 'metric') 
	
	day_plus1=weather_com_result["forecasts"][1]["day_of_week"]
	day_plus1_type=weather_com_result["forecasts"][1]["day"]["text"]
	day_plus1_low=weather_com_result["forecasts"][1]["low"]
	day_plus1_high=weather_com_result["forecasts"][1]["high"]

	day_plus2=weather_com_result["forecasts"][2]["day_of_week"]
	day_plus2_type=weather_com_result["forecasts"][2]["day"]["text"]
	day_plus2_low=weather_com_result["forecasts"][2]["low"]
	day_plus2_high=weather_com_result["forecasts"][2]["high"]

	day_plus3=weather_com_result["forecasts"][3]["day_of_week"]
	day_plus3_type=weather_com_result["forecasts"][3]["day"]["text"]
	day_plus3_low=weather_com_result["forecasts"][3]["low"]
	day_plus3_high=weather_com_result["forecasts"][3]["high"]


	day_plus4=weather_com_result["forecasts"][4]["day_of_week"]
	day_plus4_type=weather_com_result["forecasts"][4]["day"]["text"]
	day_plus4_low=weather_com_result["forecasts"][4]["low"]
	day_plus4_high=weather_com_result["forecasts"][4]["high"]

	page = requests.get('http://www.ganeshaspeaks.com/leo/leo-daily-horoscope.action')
	html1 = html.fromstring(page.content)
	prediction = html1.xpath('//*[@id="main-wrapper"]/div/div/div[2]/section/div[2]/div/div/div[1]/span/text()')[0].replace('Ganesha','Magic Mirror')

	newspage = requests.get('https://news.google.co.in/')
	html2 = html.fromstring(newspage.content)
	news1 = html2.xpath('//*[@id="MAA4AEgAUABgAWoCaW4"]/span/text()')[0]
	news2 = html2.xpath('//*[@id="MAA4AEgBUABgAWoCaW4"]/span/text()')[0]
	news3 = html2.xpath('//*[@id="MAA4AEgCUABgAWoCaW4"]/span/text()')[0]
	news4 = html2.xpath('//*[@id="MAA4AEgDUABgAWoCaW4"]/span/text()')[0]
	news5 = html2.xpath('//*[@id="MAA4AEgEUABgAWoCaW4"]/span/text()')[0]


	print(news1)
	context={'name':'Abhi',
			 'date': date1,
			 'time':time1,
			 'weather_type':weather_type,
			 'temperature':temperature,
			 'humidity':humidity,
			 'Location':Location,
			 'day_plus1':day_plus1,
			 'day_plus1_type':day_plus1_type,
			 'day_plus1_low':day_plus1_low,
			 'day_plus1_high':day_plus1_high,
			 'day_plus2':day_plus2,
			 'day_plus2_type':day_plus2_type,
			 'day_plus2_low':day_plus2_low,
			 'day_plus2_high':day_plus2_high,
			 'day_plus3':day_plus3,
			 'day_plus3_type':day_plus3_type,
			 'day_plus3_low':day_plus3_low,
			 'day_plus3_high':day_plus3_high,

			 'day_plus4':day_plus4,
			 'day_plus4_type':day_plus4_type,
			 'day_plus4_low':day_plus4_low,
			 'day_plus4_high':day_plus4_high,

			 'prediction': prediction,

			 'news1':news1,
			 'news2':news2,
			 'news3':news3,
			 'news4':news4,
			 'news5':news5,
			 
			 }
	
 	
	
	return render(request, "index.html", context)