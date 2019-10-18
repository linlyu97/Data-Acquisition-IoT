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
    <p>https://vimeo.com/user102996791/review/367173414/cb3d1d712a</p>

<hr />
<h2 id="introduction">Introduction</h2>
<ul>
  This project is designed to simulate an integrated indoor air quality real-time monitoring system prototype. The system will utilize a multi sensor system that placed at different locations within a closed environment and measure relevant quantities such that could provide insights to the environment air conditions. The project also enabled the IOT features such that it allows users to manipulate and visualize smart devices status using web-based platform.
</ul>

<h3 id="motivation">Motivation</h3>
<ul>
  Having a good air-quality real time control is extremely important for everyone of us, we sometimes struggle with all different types of sensors we have to buy and install for our house. Lacking an integrated sensing system in the marketplace seems obvious to us. Meanwhile, as people go after high intelligent life, intelligence of household, which can help us efficiently and easily to process and monitor the sensors data obtained, also appears particularly necessary. Therefore, our project is designed to resolve the issue that helps residents to dynamically monitor the indoor air condition visually feedback the current air quality.
</ul>

<h3 id="goals">Goals</h3>
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

<h2 id="2.1"> Physical Principles</h2>
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

</ul>
  
  <h2 id="problems-encountered">Conclusion</h2>
  <ul>
    <p>
      Our final project establishes IOT mode and automatic mode respectively. In IOT mode, users can independently control appliances, such as LED and fans, through OpenChirp. In automatic mode, the system can through the preset python program, through the DHT11 Temperature & humidity sensor module and gas smoke sensor module to real-time monitor the indoor temperature, humidity and combustible gas concentration; Raspberry Pi processes the collected data and makes corresponding instructions through buzzer alarm sensor module, LED, etc. What's more, the accuracy of collected data is checked by the precision and recall of real-time calculation.
    </p>
   
  </ul>
  
  <h2 id="future-plan">Reference</h2>
  <ul>
    [1] ASHRAE, Thermal Environmental Conditions for Human Occupancy, American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASRHAE Standard 55-1992), Atlanta, 1992.
    [2] Fundamentals of Combustible Gas Detection
    [3] https://howtomechatronics.com/tutorials/arduino/dht11-dht22-sensors-temperature-and-humidity-tutorial-using-arduino/
    [4] https://lastminuteengineers.com/dht11-dht22-arduino-tutorial/
    [5] https://lastminuteengineers.com/mq2-gas-senser-arduino-tutorial/
    [6] https://lastminuteengineers.com/ds18b20-arduino-tutorial/
    [7] https://www.mouser.com/datasheet/2/321/605-00008-MQ-2-Datasheet-370464.pdf
  </ul>

  </article>

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

