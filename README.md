# Halogen

Traffic is one of the major issues in metropolitan cities. Effects of this are Delay, Pollution, Higher Fuel consumption, Accidents. 
This is because of too many vehicles, breaking oftraffic rules, improper traffic management.  <br>
75,200 people lost their lives in crashes at traffic crossings in 2017, which is over 50% of the total deaths on Indian roads.
<br></br>This project focuses on - Breaking of Traffic Signals.
<br>Technologies used:
- Python
- ALPR
  (Automatic License Plate Recognition)
- OpenCV
- FFMPEG
- PyQt GUI Widget Toolkit
- MySQL

It aims to: <br>
- Fetch the CCTV footage when the signal is RED
- The cameras have to be placed such that the vehicles would be visible in the footage only when they break the signal
- Fetch the images frame by frame through the footage and track the number plate of vehicles
- Search for the registered vehicle number in the database and notify the owner to pay the required fine
