import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import image
from PIL import Image
import os
from scipy import ndimage
import math
from decimal import Decimal



def polygon_analysis(file_name,
                     show_and_save_contour='yes',
                     show_and_save_analysis='yes',
                     show_sides='yes',
                     show_angles='yes',
                     show_slope='yes',
                     show_name='yes',
                     save_data_to_csv='yes',
                     font=cv2.FONT_HERSHEY_PLAIN):
    
    

    ##font = cv2.FONT_HERSHEY_PLAIN
    ##font = cv2.FONT_HERSHEY_TRIPLEX

    cwd = os.getcwd()
    name_file=os.path.splitext(file_name)[0]
    counter3=0
    limit=3  #detection_limit #3

    if ((show_and_save_analysis=='yes') or (show_and_save_contour=='yes')or (save_data_to_csv=='yes')):
        
        path_save_temp=os.path.join(cwd,'Data')
        path_save=os.path.join(path_save_temp,f'{name_file}_analysis')
        
        
        if not os.path.exists(path_save):
            os.makedirs(path_save)

            
    image = Image.open(file_name, 'r')
    image_size = image.size
    width_old = image_size[0]
    height_old = image_size[1]

    bigside=int(max(width_old,height_old)*1.5)
    background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
    offset = (0,0)
    background.paste(image, offset)
    file_name2=f'{width_old*2}X{height_old*2}_{name_file}.png'
    save_image=os.path.join(cwd,file_name2)
    save_image_in_data=os.path.join(path_save,file_name2)


    if ((show_and_save_analysis=='yes') or (show_and_save_contour=='yes') or (save_data_to_csv=='yes')):
        background.save(save_image_in_data)
        img = cv2.imread(save_image_in_data, cv2.IMREAD_GRAYSCALE)
        img1 = cv2.imread(save_image_in_data)
        image = Image.open(save_image_in_data)
        width, height = image.size
        blur = cv2.GaussianBlur(img,(5,5),0)
        img = plt.imread(save_image_in_data)
        plt.imshow(img)
        
    else:
        background.save(save_image)
        img = cv2.imread(save_image, cv2.IMREAD_GRAYSCALE)
        img1 = cv2.imread(save_image)
        image = Image.open(save_image)
        width, height = image.size
        blur = cv2.GaussianBlur(img,(5,5),0)
        img = plt.imread(save_image)
        plt.imshow(img)
        

    font_of_name=cv2.FONT_HERSHEY_TRIPLEX
    font_size_name=max(height,width)*0.002
    font=cv2.FONT_HERSHEY_TRIPLEX
    font_size=font_size_name/1.5
    


    colors = 10*['r', 'b', 'y','g','k','c', 'm', 'seagreen','navy','gold','coral', 'violet', 'crimson','skyblue','hotpink','slateblue', 'b', 'y','g','k','r', 'b', 'y','g','k']
    markers = 10*['*', '+', 'o', 'P', 'x','s', 'p', 'h', 'H', '<','>', 'd', 'D', '^', '1']
    shapes= ['Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon','Hendecagon','Dodecagon','Trisdecagon','Tetradecagon','Pentadecagon']

    abc=[]
    sides=[]
    distance=[]
    m=[]
    angles=[]
    slope=[]
    Name=[]




    def error_detection(abc):
        error = []
        for i in range(len(abc)):
            if (i== len(abc)-1):
                error.append(abs((abc[i]-abc[0])/abc[0]))
            else:
                error.append(abs((abc[i]-abc[i+1])/abc[i+1]))
        return (abs(np.mean(error)*100))




    def error_detection_alternate(abc):
        error = []
        for i in range(int(len(abc)/2)):
            alt_error= (abs((abc[i]-abc[i+2])/abc[i+2]))
            error.append(alt_error)
        return (abs(np.mean(error)*100))




    def sides_length_and_slope(sides):
        sides= np.reshape(sides,(len(sides),2))
        x=[]
        y=[]
        m=[]
        deg_tan=[]
        side_len=[]
        
        
        for a,b in sides:
            x.append(a)
            y.append(b)

        for i in range(len(sides)):
            if (i == (len(sides)-1)):
                side_len.append(round((math.sqrt(((x[i]-x[0])**2)+((y[i]-y[0])**2))),2))
                if ((x[0]-x[i])==0):
                    m.append(round(((y[0]-y[i])/1),2))
                else:
                    m.append(round(((y[0]-y[i])/(x[0]-x[i])),2))
            
            else:
                side_len.append(round((math.sqrt(((x[i]-x[i+1])**2)+((y[i]-y[i+1])**2))),2))
                if ((x[i+1]-x[i])==0):
                    m.append(round(((y[i+1]-y[i])/1),2))
                else:
                    m.append(round((((y[i+1]-y[i])/(x[i+1]-x[i]))),2))
        print(side_len)    
        return side_len,m,x,y




    def allow(sides=sides,width=width,height=height):
        side,_,x,y =  sides_length_and_slope(sides)
        
        for i in range(len(sides)):
            if (side[i]<(width_old*0.05)) or (x[i]<(max(width_old,height_old)*0.010))or (y[i]<(max(width_old,height_old)*0.010))or (x[i]>(max(width_old,height_old)*0.98))or(y[i]>(max(width_old,height_old)*0.98)) :
                
               #height-height*0.02
    ##        if(x[i]==0)or(y[i]==0)or(x[i]>(height-5))or(y[i]>(width-5))or(side[i]<(width/20)):
                flag=0
                break
            else:
                flag=1
        if(flag==1):
            
            return (np.reshape(sides,(len(sides),2)))




    def angle(sides,m):
        
        for i in range(len(sides)):
            if (i == (len(sides)-1)):
                if math.degrees(math.atan(m[0])-math.atan(m[i]))< 0:
                    angles.append(round(math.degrees(math.atan(m[0])-math.atan(m[i]))+180,2))
                    
                else:
                    angles.append(round(math.degrees(math.atan(m[0])-math.atan(m[i])),2))
                    
            else:
                if math.degrees(math.atan(m[i+1])-math.atan(m[i]))< 0:
                    angles.append(round(math.degrees(math.atan(m[i+1])-math.atan(m[i]))+180,2))
                    
                else:
                    angles.append(round(math.degrees(math.atan(m[i+1])-math.atan(m[i])),2))
                
##        print(angles)        
        return angles
     


    def Fiveto15shape(sides):
        
        for i in range(11):
            if len(sides) == i+5:
                
                side,m,_,_= sides_length_and_slope(sides)
                angles =angle(sides,m)
                if (error_detection(angles)<limit):
                    
                    
                    print (f'Regular {shapes[i]}')
                    write_angle_slope_and_sides(sides,side,angles,m)
                    write_name(f'Regular {shapes[i]}')
                    save_to_csv(sides,side,angles,name=f"Regular {shapes[i]}", m=m)
                
                else:
                        
                    print (f'{shapes[i]}')
                    write_angle_slope_and_sides(sides,side,angles,m)
                    write_name(f'{shapes[i]}')
                    save_to_csv(sides,side,angles,name=f'{shapes[i]}',m=m)
                    
                    
                        

    def show_and_save_fig_data(sides,counter3):
        
        for i in range(len(sides)):
            counter2=0
            plt.scatter(np.reshape(sides,(len(sides),2))[i][counter2],np.reshape(sides,(len(sides),2))[i][counter2+1],marker= markers[counter3], c=colors[counter3])
            


    def write_angle_slope_and_sides(sides,side,angles,m,show_angles=show_angles,show_sides=show_sides):
        middle_point_X=[]
        middle_point_Y=[]
        for j in range(len(sides)):
            d=0
            if (j == (len(sides))-1):
                middle_point_X.append(int((((sides[j][d]+sides[0][d])/2))))
                middle_point_Y.append(int(((sides[j][d+1]+sides[0][d+1])/2)))
            else:
                middle_point_X.append(int((((sides[j][d]+sides[j+1][d])/2))))
                middle_point_Y.append(int(((sides[j][d+1]+sides[j+1][d+1])/2)))
    ##    print(middle_point_X)
    ##    print(middle_point_Y)
    ##    print(sides)
            
        if (show_angles=='yes'):
            for j in range(len(sides)):
                c=0
                cv2.putText(img1, f"{angles[j]}", (sides[j][c], sides[j][c+1]), font, font_size, ((183,9,93)))
        if(show_sides=='yes'):
            for j in range(len(sides)):
                c=0
                cv2.putText(img1, f"{side[j]}", (middle_point_X[j], middle_point_Y[j]), font, font_size, ((0,0,255))) #blue green red
        if(show_slope=='yes'):
            for j in range(len(sides)):
                c=0
                cv2.putText(img1, f"{(m[j])}", (middle_point_X[j], int(middle_point_Y[j]+(max(height,width)*0.05))), font, font_size, ((0,255,0))) #blue green red
        


    def save_to_csv(sides,side,angles,name,m):
        slope.append(m)
        distance.append(side)
        Name.append(name[:])
        
        if save_data_to_csv=='yes':
            x= 'csv_data_'+file_name[:(len(file_name)-4)]+'.csv'
            
            save_csv=os.path.join(path_save,f'csv_data_{name_file}.csv')
            with open(save_csv, mode='w') as data_file:
                data_writer = csv.writer(data_file, delimiter=';')
                fieldname=[['x_coordinate','y_coordinate','distance_in_pixels', 'angles', 'name', 'slope']]
                data_writer.writerows(fieldname)
                for i in range(len(side)):
                    c=0
                    data_writer.writerow([sides[i][c],sides[i][c+1],side[i], angles[i], name, m[i]])
            


    def write_name(name):
        if(show_name=='yes'):
            cv2.putText(img1, name, (int(max(height,width)*0.20), int(max(height,width)*0.80)), font_of_name, font_size_name, ((255,0,0))) #blue green red
            if(show_angles=='yes'):
                cv2.putText(img1, '# - Angles', (int(max(height,width)*0.70), int(max(height,width)*0.75)), font_of_name, font_size_name*0.40, ((183,9,93)))
            if(show_sides=='yes'):
                cv2.putText(img1, '# - Distance(in px)', (int(max(height,width)*0.70), int(max(height,width)*0.80)), font_of_name, font_size_name*0.40, ((0,0,255)))
            if(show_slope=='yes'):
                cv2.putText(img1, '# - Slope', (int(max(height,width)*0.70), int(max(height,width)*0.85)), font_of_name, font_size_name*0.40, ((0,255,0)))





    counter3=0
               
    _, threshold = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        sides = cv2.approxPolyDP
        cv2.drawContours(img, [sides], 0, (0), 5)
        x = sides.ravel()[0]
        y = sides.ravel()[1]

        if (show_and_save_contour=='yes'):
            counter3+=1
            show_and_save_fig_data(sides,counter3)

    ##    print(sides)
        
        sides=allow(sides)
    ##    print(len(sides))
        if (sides is not None):
    ##        print(sides)

            if len(sides) == 3:
                
                side,m,_,_= sides_length_and_slope(sides)
                angles =angle(sides,m)
                if (error_detection(angles)<limit):
                    if (error_detection(side)<limit): 
                        print ('Eq Tri')
                        write_angle_slope_and_sides(sides,side,angles,m)
                        write_name('Eq Tri')
                        save_to_csv(sides,side,angles,name='Eq Tri', m=m)
                        break

                        
                else:
                    print ('Triangle')
                    write_angle_slope_and_sides(sides,side,angles,m)
                    write_name('Triangle')
                    save_to_csv(sides,side,angles,name='Triangle',m=m)
                    break
                    
               

            if len(sides) == 4:
                side,m,_,_= sides_length_and_slope(sides)
                angles =angle(sides,m)

                if (error_detection(angles)<limit):
                    if (error_detection(side)<limit):
                        print('square')
                        write_angle_slope_and_sides(sides,side,angles,m=m)
                        write_name('square')
                        save_to_csv(sides,side,angles,name='square',m=m)
                        distance.append(side)
                        break
                    elif (error_detection_alternate(side)<limit):
                        print('rectangle')
                        write_angle_slope_and_sides(sides,side,angles,m=m)
                        write_name('rectangle')
                        save_to_csv(sides,side,angles,name='rectangle',m=m)
                        break
                
                elif (error_detection_alternate(angles)<limit):
                    
                    if (error_detection(side)<limit):
                        print('Rhombus')
                        write_angle_slope_and_sides(sides,side,angles,m=m)
                        write_name('Rhombus')
                        save_to_csv(sides,side,angles,name='Rhombus',m=m)
                        break
                        
                    elif (error_detection_alternate(side)<limit):
                        print('Parallelogram')
                        write_angle_slope_and_sides(sides,side,angles,m=m)
                        write_name('Parallelogram')
                        save_to_csv(sides,side,angles,name='Parallelogram',m=m)
                        break
                            
                else:
                    print('Quadrilateral')
                    write_angle_slope_and_sides(sides,side,angles,m=m)
                    write_name('Quadrilateral')
                    save_to_csv(sides,side,angles,name='Quadrilateral',m=m)
                        
                    break

            if(len(sides)>4):
                
                Fiveto15shape(sides)
                
                break
        else:
            pass
  
    if (show_and_save_contour=='yes'):
        save_conotur=os.path.join(path_save,f"contour_{file_name}")
        plt.savefig(save_conotur)
        im= Image.open(save_conotur)
        im.show()
##        plt.show()

        
    if (show_and_save_analysis=='yes'):
        save_analysis=os.path.join(path_save,f"analysis_{file_name}")
        cv2.imwrite(save_analysis,img1)
        im= Image.open(save_analysis)
        im.show()
    
    return len(sides),sides,distance,slope,angles,Name[0]    



    

##Number_of_sides,Coordinates,Distance_in_pixels,Slopes,Angles,Names= polygon_analysis(file_name,
##                                                                              show_and_save_contour='yes',
##                                                                             show_and_save_analysis='yes',
##                                                                             show_sides='yes',
##                                                                             show_angles='yes',
##                                                                             show_slope='yes',
##                                                                             show_name='yes',
##                                                                             save_data_to_csv='yes',
##                                                                             font=cv2.FONT_HERSHEY_PLAIN)
##print(Number_of_sides)
##print(Coordinates)
##print(Distance_in_pixels)
##print(Slopes)
##print(Angles)
##print(Names)








