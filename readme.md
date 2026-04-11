#AllSky to Go STSCI
![single image with data](./Images/image-20260406215048.jpg)

## how to install

copy all files in the home Directory. 


## Setup crontab

````
crontab -e
````

add this two cronjobs

```
*/30 * * * * python ~/allsky/gps_coords.py
0 */1 * * * /home/raspberry/allsky/scripts/moon_height_venv.sh
```



## install skyfield for moon diagram

```
pip3 install skyfield matplotlib numpy
```

if this not work use a virtual environment
```
sudo apt install python3-venv
mkdir -p ~/allsky/venv
python3 -m venv ~/allsky/venv
source ~/allsky/venv/bin/activate
pip install skyfield requests
```

test the moon_height.py script
```
python ~/allsky/scripts/moon_height.py
```
Change crontab entry. moon_height_venv.sh use For skyfield the new use a virtual enviroment 
```
crontab -e
0 */1 * * * /home/raspberry/allsky/scripts/moon_height_venv.sh

```

if this is not working you can use the quick and dirty Methode

```
pip install skyfield --break-system-packages
```

Now you can overlay this image with your camera Picture. Go to your Webbrowser and to your allsky Webpage. Go to the "Overlay Editor" and Chose "add Existing Image Field". In the image menue you can select moon_height.png.


## install gps
For installing the gps-module I have used the install manuel from Allsky_go
[AllskyGo_GPS_install](https://github.com/Chrise-2000/Allsky_Go/blob/main/C_Installation%20Manual%20v3.0.pdf)
Use a usb-hps-module were you can connect with your pi. IF you don´t want to use a or you haven`t an gps-module enter you coordinates in ~/allskygps_coords.txt


![Startrail](./Images/startrails-20260406)
