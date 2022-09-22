import datetime


def get_wind_message(wind):
    # based on this table info https://en.wikipedia.org/wiki/Beaufort_scale
    
    if wind["speed"]<0.5:
        description="Calm"
    elif wind["speed"]>= 0.5 and wind["speed"]<=1.5:
        description="Light air"
    elif wind["speed"]>= 1.6 and wind["speed"]<=3.3:
        description="Light breeze"
    elif wind["speed"]>= 3.4 and wind["speed"]<5.5:
        description="Gentle breeze"
    elif wind["speed"]>= 5.5 and wind["speed"]<=7.9:
        description="Moderate breeze"
    elif wind["speed"]>= 8 and wind["speed"]<=10.7:
        description="Fresh breeze"
    elif wind["speed"]>= 10.8 and wind["speed"]<=13.8:
        description="Strong breeze"
    elif wind["speed"]>= 13.9 and wind["speed"]<=17.1:
        description="High wind"
    elif wind["speed"]>= 17.2 and wind["speed"]<=20.7:
        description="Fresh gale"
    elif wind["speed"]>= 20.8 and wind["speed"]<=24.4:
        description="Strong gale"
    elif wind["speed"]>= 24.5 and wind["speed"]<=28.4:
        description="Storm"
    elif wind["speed"]>= 28.5 and wind["speed"]<=32.6:
        description="Violent storm"
    else:
        description="Hurricane force"
    
    if wind["deg"]>=348.75 and wind["deg"]<=11.25:
        direction="north"
    elif wind["deg"]>=11.25 and wind["deg"]<=33.75:
        direction="north-northeast"
    elif wind["deg"]>=33.75 and wind["deg"]<=56.25:
        direction="northeast"
    elif wind["deg"]>=56.25 and wind["deg"]<=78.75:
        direction="east-northeast"
    elif wind["deg"]>=78.75 and wind["deg"]<=101.25:
        direction="east"
    elif wind["deg"]>=101.25 and wind["deg"]<=123.75:
        direction="east-southeast"
    elif wind["deg"]>=123.75 and wind["deg"]<=146.25:
        direction="southeast"
    elif wind["deg"]>=146.25 and wind["deg"]<=168.75:
        direction="south-southeast"
    elif wind["deg"]>=168.75 and wind["deg"]<=191.25:
        direction="south"
    elif wind["deg"]>=191.25 and wind["deg"]<=213.75:
        direction="south-southwest"
    elif wind["deg"]>=213.75 and wind["deg"]<=236.25:
        direction="southwest"
    elif wind["deg"]>=236.25 and wind["deg"]<=258.75:
        direction="west-southwest"
    elif wind["deg"]>=258.75 and wind["deg"]<=281.25:
        direction="west"
    elif wind["deg"]>=281.25 and wind["deg"]<=303.75:
        direction="west-northwest"
    elif wind["deg"]>=303.75 and wind["deg"]<=326.25:
        direction="northwest"
    elif wind["deg"]>=326.25 and wind["deg"]<=348.75:
        direction="north-northwest"

    return f'{description}, {wind["speed"]}, {direction}'

def k_to_celcius(kelvin):
    # return "{:.0f}".format(kelvin-273.15)
    return int(kelvin-273.15)


def k_to_farenheit(kelvin):
    return int(9/5*(kelvin-273+32))

def get_clouds_message(cloud_coverage):
    # based on this table https://www.eoas.ubc.ca/courses/atsc113/flying/met_concepts/01-met_concepts/01c-cloud_coverage/index.html
    if cloud_coverage==0:
        return "Clear sky"
    elif cloud_coverage> 0 and cloud_coverage<=30:
        return "Few clouds"
    elif cloud_coverage>= 30 and cloud_coverage<=50:
        return "Scattered clouds"
    elif cloud_coverage>= 50 and cloud_coverage<=99:
        return "Broken clouds"
    else:
        return "Overcast"

def get_time_format(unix_time):
    print(unix_time)
    timestamp = datetime.datetime.fromtimestamp(unix_time)
    return f"{timestamp.hour}:{timestamp.minute}"

def get_coordinates_format(coords):
    # lat long
    return f'[{"{:.2f}".format(coords["lat"])}, {"{:.2f}".format(coords["lon"])}]'

def get_forecast(num):
    # make average for 4 days
    # make weather report dict for each
    return num