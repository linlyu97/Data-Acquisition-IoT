 <body>

  <div class="site-header">

  <nav class="site-nav">
    <a href="#" class="menu-icon">
      <i class="fa fa-navicon fa-lg"></i>
    </a>

  <div class="trigger">
      <a class="page-link" href="https://inferlab.github.io/12740"> Course Site</a>
  </div>
  </nav>


  </div>


  <div class="page-content">
    <div class="wrapper">
      <div class="post">

  <header class="post-header">
     <h1 class="post-title" style="text-align: center">Indoor Air Quality Monitoring System - Progress Report</h1>
     <p class="post-meta" > Group AA: Yu Du; Yuhang Liang; Lin Lyu</p>
  </header>

  <article class="post-content">
    <p class="page-link" href= "https://vimeo.com/user102996791/review/367173414/cb3d1d712a"> Video Link</p>

<hr />
<h2 id="introduction">Introduction</h2>
<ul>
  This project is designed to simulate an integrated indoor air quality real-time monitoring system prototype. The system will utilize a multi sensor system that placed at different locations within a closed environment and measure relevant quantities such that could provide insights to the environment air conditions. The project also enabled the IOT features such that it allows users to manipulate and visualize smart devices status using web-based platform.
</ul>

<h2 id="motivation">Motivation</h2>
<ul>
  Having a good air-quality real time control is extremely important for everyone of us, we sometimes struggle with all different types of sensors we have to buy and install for our house. Lacking an integrated sensing system in the marketplace seems obvious to us. Meanwhile, as people go after high intelligent life, intelligence of household, which can help us efficiently and easily to process and monitor the sensors data obtained, also appears particularly necessary. Therefore, our project is designed to resolve the issue that helps residents to dynamically monitor the indoor air condition visually feedback the current air quality.
</ul>

<h2 id="goals">Goals</h2>
<ul>
The proposed outcome of the project will be real-time data collecting system and an alter system dynamically suggest the user to take proper action when any one of the measurements go beyond the theoretical healthy standard.
The vision of the project is to lay a foundation for IOT and automatic system that user can change the indoor conditions using smart devices. The front end of our data acquisition system are different sensors, from which monitoring data of air can be obtained. The system compares precision and recall to ensure the accuracy of data by using a reference sensor to serve as ground truth. Then legal data can also be visualized through OpenChirp so that users can directly see the change of air quality in a day using a web browser or other smart devices, and can be used to change the status of the smart devices based on individual users’ preferences.
</ul>
<hr />

<h2 id="Phenomena of Interests"> Phenomena of Interests </h2>
<ul>
The phenomena of interest in our project include temperature, humidity and combustible gas concentration of air in the room.
</ul>

<h3 id >

<h3 id="2.1"> Physical Principles</h3>
<ul>
<p>Temperature</p>
<ul>Temperature is a physical quantity expressing hot and cold. If the room temperature is too low, the body's heat will be lost to the air too much, and people will feel cold, which reflects the necessity of appropriate room temperature. In this project, what we consider most is room temperature, which is the range of air temperature that most people prefer for indoor settings. According to Thermal Environmental Conditions for Human Occupancy[1], the appropriate indoor temperature of human body in summer is 23~26℃, and 20~23.5℃ in winter. In this project, we will dynamically make decisions based on current seasonality.
</ul>
<p> Humidity</p>
<ul>
Humidity is the measure of water vapour present in the air. Humidity parameters are stated in diverse ways and the corresponding units are based on the measurement technique used. The most commonly used terms are “Relative Humidity RH”, “Parts Per Million (PPM)” by weight or by volume and “Dew/Frost Point (D/F PT)”, in which the two latter are subclasses of “Absolute Humidity (AB)”. What we use in this project is relative humidity. Relative Humidity (abbreviated as RH) is defined as the ratio of the amount of moisture content of air to the maximum (saturated) moisture level that the air can hold at the same given temperature and pressure of the gas. According to Thermal Environmental Conditions for Human Occupancy[1], the appropriate indoor humidity of human body is 40~60%, which we used in the algorithms.
</ul>
<p>Combustible Gas</p>
<ul>Combustible gases include natural gas, methane, butane, propane and hydrogen. Vapor density is one of the properties of combustible gas. The definition of it is the relative of the vapor as compared with air. It is calculated as the ratio of the molecular weight of the vapor to the molecular weight air.[2] In our project,  the gas density is represented in terms of voltage and converted into standard unit to describe gas density
</ul>

<<<<<<< HEAD
<h3 id="2.2"> Static and Dynamic Behavior</h3>
<ul>
<p>Temperature</p>
<ul>
  Temperature can be influenced by many factors, such as time and human activities. Temperature is usually low at midnight, decreasing in the early hours of the morning, and then increasing rapidly until just after midday. It then decreasing during the night. As for the human activities, the more people in the room, the more heat they radiate, and the temperature in the room would rise. Thus, read-time monitoring of room temperature is necessary.
</ul>
<p> Humidity</p>
<ul>
  Humidity changes throughout the day. Relative humidity is usually high at midnight and in the early morning, drops rapidly, after the sun rises, until it is lowest just after midday. However, the human body often cannot feel the change of indoor humidity in a short time until there is some physiological response, such as thirst, which is not a good idea for keeping healthy in the long run. Therefore, it is necessary to know the humidity change in time.
</ul>
<p>Combustible Gas</p>
<ul>
  Many kinds of combustible gas that people use frequently, such as natural gas, are odorless, which means it could be hard for human to detect gas leakage. When the combustible gas reaches the explosive range, it is hazardous for people to stay in the room. Therefore, the detect of combustible gas is essential.
</ul>

<h3 id="2.3"> Signal Characteristics</h3>
<p>Temperature & Humidity</p>
<ul>
  As for the detection of the temperature and humidity, the sensor we use is DHT11. The format of output data is 40-bit data, including 8bit integral RH data + 8bit decimal RH data + 8bit integral T data + 8bit decimal T data + 8bit check-sum. If the data transmission is right, the check-sum should be the last 8bit of "8bit integral RH data + 8bit decimal RH data + 8bit integral T data + 8bit decimal T data". Thus, the signal of temperature and humidity of discrete data points.
</ul>
<p>Combustible gas</p>
<ul>
  In our project, the sensor we use for detecting combustible gas is MQ-2. And the concentration of combustible gas is reflected by 0~4.2V analog output voltage. The voltage varies with the concentration of combustible gas in the room. The higher the concentration the higher the voltage.
</ul>

<h2 id="Review of Sensors Being Utilized"> Review of Sensors Being Utilized </h2>
<ul>
  The sensors that are used for Indoor Air Quality Monitoring System are as follows:
</ul>
<ul>
  <li>DHT11</li>
  <li>MQ-2</li>
  <li>DS18B20 (Reference)</li>
</ul>
<ul>
  The indication devices includes:
</ul>
<ul>
  <li> Leds in different colors(blue and red) </li>
  <li>Buzzer Module</li>
</ul>
<ul>
  Physical devices integrated:
</ul>
<ul>
  <li> Ventilation fan</li>
  <li> Heat dissipation fan</li>
</ul>
<h3 id="3.1"> Physical Principle</h3>
<p>DHT11</p>
<ul>
  DHT11 Temperature & Humidity Sensor features a temperature & humidity sensor complex with a calibrated digital signal output. This kind of sensor consists of a humidity sensing component, an NTC temperature sensor and an IC on the back side of it[3].
  For measuring humidity, we would use the humidity sensing component which has two electrodes with moisture holding substrate between them. So as the humidity changes, the conductivity of the substrate changes or the resistance between these electrodes changes. On the other hand, a NTC temperature sensor/Thermistor to measure temperature[4].
</ul>
<p> MQ-2 </p>
<ul>
  MQ2 is one of the commonly used gas sensors in MQ sensor series. It is a Metal Oxide Semiconductor (MOS) type Gas Sensor also known as Chemiresistors, as the detection is based upon change of resistance of the sensing material when the Gas comes in contact with the material[5]. It uses a simple voltage divider network so that concentrations of gas can be detected.
</ul>
<p> DS18B20 </p>
<ul>
  DS18B20 is 1-Wire interface Temperature sensor manufactured by Dallas Semiconductor Corp. The unique 1-Wire Interface requires only one digital pin for two way communication with a microcontroller.The sensor comes usually in two form factors. One is that comes in TO-92 package looks exactly like an ordinary transistor[6] and the other is a waterproof probe style.
</ul>
<h3 id="3.2"> Static and Dynamic Behavior of Sensor</h3>
<ul>
  <p> DHT11Static behavior: Senstivity</p>
  <ul>
    DHT11 which contains a thermistor, can more easily detect small changes in temperature and is  more sensitive than a less sensitive sensor, like a thermocouple. This sensitivity, however, comes at the expense of linearity. This can be an important factor when determining the ideal sensor choice for the temperatures measuring.
  </ul>
  <p> DHT11Static behavior: Accuracy</p>
  <ul>
    The accuracy of humidity is ±5% and The accuracy of temperature is ±2°C.
  </ul>
  <p> DHT11Static behavior: Repeatablility</p>
  <li>The repeatability about humidity is  ±1% <li>
  <li>The repeatability about temperature is  ±0.2°C <li>
  <p> DHT11Static behavior: Dynamic Behavior</p>
  <ul>
    Lag: there is a lag between the changes in temperature or humidity intensity and resistance of sensor. However, this lag can be ignored.
  </ul>

  <p> MQ-2: Sensitivity</p>
  <ul>
  MQ-2 gas sensor has high sensitivity to  combustible gas in wide range(300-10000ppm)[7] ,sensitivity=Rs(in air)/Rs(1000ppm isobutane)≥5
  </ul>

<h3 id="3.3"> Sensor Characteristics Discussions</h3>
<p>DHT11 and DS18B20</p>
<ul>
  We can see from the following table: the accuracy of DS18B20 is significantly higher than the accuracy of DTH11. In this case, we assume that the data collected by DS18B20 is ground truth. So we could do some data analysis by comparing the data collected by these two sensors, separately.
</ul>





<h2 id="future-plan">Future Plan</h2>
<ul>



=======
>>>>>>> 5b2953cd5b9ffb458f25e5f309f8f6989e44734e
</ul>
  
<h2 id="problems-encountered">Conclusion</h2>
<ul>
<p>
   Our final project establishes IOT mode and automatic mode respectively. In IOT mode, users can independently control appliances, such as LED and fans, through OpenChirp. In automatic mode, the system can through the preset python program, through the DHT11 Temperature & humidity sensor module and gas smoke sensor module to real-time monitor the indoor temperature, humidity and combustible gas concentration; Raspberry Pi processes the collected data and makes corresponding instructions through buzzer alarm sensor module, LED, etc. What's more, the accuracy of collected data is checked by the precision and recall of real-time calculation.
</p>
   
</ul>
  
<h2 id="future-plan">Reference</h2>
<ul>
<p>
[1] ASHRAE, Thermal Environmental Conditions for Human Occupancy, American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASRHAE Standard 55-1992), Atlanta, 1992.
[2] Fundamentals of Combustible Gas Detection
[3] https://howtomechatronics.com/tutorials/arduino/dht11-dht22-sensors-temperature-and-humidity-tutorial-using-arduino/
[4] https://lastminuteengineers.com/dht11-dht22-arduino-tutorial/
[5] https://lastminuteengineers.com/mq2-gas-senser-arduino-tutorial/
[6] https://lastminuteengineers.com/ds18b20-arduino-tutorial/
[7] https://www.mouser.com/datasheet/2/321/605-00008-MQ-2-Datasheet-370464.pdf
</p>
</ul>



  <div align="center">
  	<a href="#">
  	<i class="fa fa-arrow-circle-up fa-2x"></i>
  	</a>
  </div>

  </div>

  </div>
  </div>

  <div class="footer center">


</div>


  </body>

