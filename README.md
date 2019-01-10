# Polygon-Analysis
This is capable of detecting the shapes and doing some cool analysis like detecting the shape with greater accuracy, measuring the angles, determining the slope and measuring the distance in pixels between two points, 
This program is an easy one-liner program to do analysis on a polygon.

Let's take a look at it


polygon_analysis (file_name,
                     show_and_save_contour='yes',
                     show_and_save_analysis='yes',
                     show_sides='yes',
                     show_angles='yes',
                     show_slope='yes',
                     show_name='yes',
                     save_data_to_csv='yes',
                     font=cv2.FONT_HERSHEY_PLAIN)



file_name: as clear from the name, it takes a file name, if the file is in the same directory then you can simply type name, else type the full path to the file.

show_and _save_contour= it allows you to see the various shapes that program detects in the image, it will also save the image file in a folder to Data/file_name_analysis/contour image.
Everything that saves during the program related to this file will save in this particular folder only.

show_and_save_analysis: it allows you to see the numerical data on the image itself. the data includes Sides, Angles, and Slope. also, the name of an image will also be written there, The image will also save in the same directory as above.

Show_angles: This will show the angles on the image, changing it to NO will result to not showing angles on the image.

Show_slope: This will show the Slope on the image, changing it to NO will result to not showing Slope on the image.

Show_sides: This will show the Sides on the image, changing it to NO will result to not showing Sides on the image. Note that the sides here are in pixels. 

show_name: This will show the Name on the image, changing it to NO will result to not showing Sides on the image.

font: you can change the Font if you want, Here is the list of some fonts
	Here are few to play with:
    cv2.FONT_HERSHEY_SIMPLEX
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX
    cv2.FONT_HERSHEY_COMPLEX
    cv2.FONT_HERSHEY_TRIPLEX
    cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    
This program return (len(sides),sides,distance,slope,angles,Name)

len(sides): Number of sides in a figure.
Sides: it returns the coordinates of the shape. Side[0] is the first [x,y] set. Same side[0][0] will give you first x point. 
Distances: It returns the distance between two points in pixels.
Slope: It returns back the slope values corresponds to each side
Angle: It returns the angles.
Name: It returns back the name of the shape.

Number_of_sides,Coordinates,Distance_in_pixels,Slopes,Angles,Names= polygon_analysis(file_name,
                                                                               show_and_save_contour='yes',
                                                                               show_and_save_analysis='yes',
                                                                               show_sides='yes',
                                                                               show_angles='yes',
                                                                               show_slope='yes',
                                                                               show_name='yes',
                                                                               save_data_to_csv='yes',
                                                                               font=cv2.FONT_HERSHEY_PLAIN)






