import pygame
import PyGameComponents
import Location
import asyncio
import aiohttp

weatherList = []
weatherClock = pygame.time.Clock()
timeSinceLastWeatherCall = 0
refreshMinutes = 1
isCelsius = False
currentWeather = 'Loadiffng...'
currentTemperature = 'Loading...'

def ClockTick():
    global timeSinceLastWeatherCall
    dt = weatherClock.tick()
    timeSinceLastWeatherCall += dt

async def UpdateWeather():
        global isCelsius
        global currentWeather
        global currentTemperature
        global weatherList
        apiKey = 'e15f46e2fe5e6c476aa7f8ff3429bad0'
        city = Location.getCurrentCity()
        countryCode = 'US'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{countryCode}&appid={apiKey}"

        #try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()

                    temperature = data['main']['temp']
                    weatherDescription = data['weather'][0]['main']

                    tempC = temperature - 273.15
                    tempF = tempC*1.8 + 32

                    isWeatherChanged = False
                    if(weatherDescription != currentWeather):
                        isWeatherChanged = True

                    currentWeather = weatherDescription
                    if(isCelsius):
                        currentTemperature = round(tempC)
                    else:
                        currentTemperature = round(tempF)
                    
                    print(f'Temperature: {currentTemperature}, Weather: {currentWeather}')

                    if(isWeatherChanged):
                        for display in weatherList:
                            display.temp = currentTemperature
                            display.weather = currentWeather
                            display.UpdateDisplay(True)
                    else:
                        for display in weatherList:
                            display.temp = currentTemperature
                            display.weather = currentWeather
                            display.UpdateDisplay()
                    return
        #except:
            print("[Weather] Error getting weather information")
            return

asyncio.run(UpdateWeather())

class WeatherDisplay():
    def __init__(self,x,y,iconSize,textSize,tempTextOffset,weatherTextOffset,textPadding=5,refreshMinutes=5,isCelcius=False,location=None):
        self.x = x
        self.y = y
        self.iconSize = iconSize
        self.textSize = textSize
        self.tempTextOffset = tempTextOffset
        self.weatherTextOffset = weatherTextOffset
        self.textPadding = textPadding
        self.refreshMinutes = refreshMinutes
        self.isCelcius = isCelcius
        self.clock = pygame.time.Clock()
        self.timeSinceLastWeatherCall = 0
        self.temp = ''
        self.weather = ''
        self.icon = PyGameComponents.Entity('Images/CustomWeatherIcons/Clear.png',self.x,self.y,self.iconSize,self.iconSize)
        self.tempTextComponent = PyGameComponents.Text(self.x,self.y, f'Loading...', 'arial', self.textSize,(255,255,255),True)
        self.weatherTextComponent = PyGameComponents.Text(self.x, self.y, f'Loading...', 'arial', self.textSize,(255,255,255),True)
        
        self.tempTextComponent.setPosition(self.x + self.iconSize + self.tempTextComponent.rect.width/2 + self.textPadding, self.y + self.tempTextOffset)
        self.weatherTextComponent.setPosition(self.x + self.iconSize + self.weatherTextComponent.rect.width/2 + self.textPadding, self.y + self.weatherTextOffset)

        self.location = location

        self.isDrawn = True

        global weatherList
        global currentWeather
        global currentTemperature
        if(self.location == None):
            self.weather = currentWeather
            self.temp = currentTemperature
            self.UpdateDisplay(True)
            weatherList.append(self)
        else:
            asyncio.run(self.UpdateWeather())

    async def UpdateWeather(self):
        apiKey = 'e15f46e2fe5e6c476aa7f8ff3429bad0'
        city = self.location
        countryCode = 'US'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{countryCode}&appid={apiKey}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()

                        temperature = data['main']['temp']
                        weatherDescription = data['weather'][0]['main']

                        tempC = temperature - 273.15
                        tempF = tempC*1.8 + 32

                        isWeatherChanged = False
                        if(weatherDescription != self.weather):
                            isWeatherChanged = True

                        self.weather = weatherDescription
                        if(self.isCelcius):
                            self.temp = round(tempC)
                        else:
                            self.temp = round(tempF)
                        
                        print(f'Temperature: {self.temp}, Weather: {self.weather}')

                        if(isWeatherChanged):
                            self.UpdateDisplay(True)
                        else:
                            self.UpdateDisplay()
                        return
        except:
            return
        #return None

    def UpdateDisplay(self,updateIcon = False):
        if(self.isCelcius):
            self.tempTextComponent.changeText(f'{self.temp}°C')
            self.tempTextComponent.setPosition(self.x + self.iconSize + self.tempTextComponent.rect.width/2 + self.textPadding, self.y + self.tempTextOffset)
        else:
            self.tempTextComponent.changeText(f'{self.temp}°F')
            self.tempTextComponent.setPosition(self.x + self.iconSize + self.tempTextComponent.rect.width/2 + self.textPadding, self.y + self.tempTextOffset)
            
        self.weatherTextComponent.changeText(f'{self.weather}')
        self.weatherTextComponent.setPosition(self.x + self.iconSize + self.weatherTextComponent.rect.width/2 + self.textPadding, self.y + self.weatherTextOffset)

        if(updateIcon):
            self.icon.changeSrc(f'Images/CustomWeatherIcons/{self.weather}.png')
        
    def draw(self,screen):
        if(self.isDrawn):
            if(self.location != None):
                dt = self.clock.tick()
                self.timeSinceLastWeatherCall += dt

                if(self.timeSinceLastWeatherCall > self.refreshMinutes*60000):
                    asyncio.run(self.UpdateWeather())
                    self.timeSinceLastWeatherCall = 0
            
            self.icon.draw(screen)
            self.tempTextComponent.draw(screen)
            self.weatherTextComponent.draw(screen)