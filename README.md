Polygon Analysis
===================


Our aim is to build a module which is enough to analyze a polygon and return some fruitful information like an angle, slope, sides, corner coordinates etc. So we build **py2pyAnalysis**. Two line of code is sufficient to tear down a polygon of upto 15 sides. For overview of the module, consider this page is sufficient, if you are intrested in the working behind the program then visit [py2py](http://www.py2py.com/polygon-analysis-overview-and-explaination/)

----------

Installation
-------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **py2pyAnalysis**.

```bash
pip install py2pyAnalysis
```
----------

Documents
-------------

Let's take a look at it, 


```python
 polygon_analysis ( file_name,
                     show_and_save_contour='yes',
                     show_and_save_analysis='yes',
                     show_sides='yes',
                     show_angles='yes',
                     show_slope='yes',
                     show_name='yes',
                     save_data_to_csv='yes',
                     font=cv2.FONT_HERSHEY_PLAIN
                     )

```

> - **file_name :** as clear from the name, it takes a file name, if the file is in the same directory then you can simply type name, else type the full path to the file.

> - **show_and _save_contour :** it allows you to see the various shapes that program detects in the image, it will also save the image file in a folder to Data/file_name_analysis/contour image.
Everything that saves during the program related to this file will save in this particular folder only.

> - **show_and_save_analysis :** it allows you to see the numerical data on the image itself. the data includes Sides, Angles, and Slope. also, the name of an image will also be written there, The image will also save in the same directory as above.

> - **Show_angles :** This will show the angles on the image, changing it to NO will result to not showing angles on the image.

> - **Show_slope :** This will show the Slope on the image, changing it to NO will result to not showing Slope on the image.

> - **font :** you can change the Font if you want, Here is the list of some fonts.
```python
    cv2.FONT_HERSHEY_SIMPLEX
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX
    cv2.FONT_HERSHEY_COMPLEX
    cv2.FONT_HERSHEY_TRIPLEX
    cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
```

This program returns
```python 
return (len(sides),sides,distance,slope,angles,Name) 
```


> - **len(sides): :**  Number of sides in a detected Polygon.

> - **Sides :** Tit returns the coordinates of the shape. Side[0] is the first [x,y] set. Similarly side[0][0] & side[0][1] will give you first x and y point respectivelly.

> - **Distances :** It returns the distance between two points in pixels.

> - **Slope :** It returns back the slope values corresponds to each side.

> - **Angle :** It returns back an array of angles.

> - **Name :** It returns back the name of the shape.


If anytime you forgot the which come after which then just type 
```python
import py2pyAnalysis as py
py.help()
```
and it will bring you the code below

```python
#https://pypi.org/project/py2pyAnalysis/
#https://github.com/Pushkar-Singh-14/Polygon-Analysis
#http://py2py.com/polygon-analysis-overview-and-explaination/

Number_of_sides,Coordinates,Distance_in_pixels,Slopes,Angles,Names= py.polygon_analysis ( file_name,
                     show_and_save_contour='yes',
                     show_and_save_analysis='yes',
                     show_sides='yes',
                     show_angles='yes',
                     show_slope='yes',
                     show_name='yes',
                     save_data_to_csv='yes',
                     font=cv2.FONT_HERSHEY_PLAIN
                     ) 
```
