from abc import ABC,abstractmethod
#####bara encapsul be har kodom az classa name ezafe kn ke hide bshe
class shape(ABC):
    def __init__(self,perimeter=None,area=None,volume=None, **kwargs):
        self.volume=volume
        self.perimeter=perimeter
        self.area=area
        #Encapsulation
        self._name=None
    
    def Area(self, **kwargs):
        pass
    
    def Volume(self,**kwargs):
        pass
    
    def Perimeter(self,**kwargs):
        pass
    
    def __str__(self):
        return f'this is a shape with the area of {self.area} and volume of {self.volume} and perimeter of {self.perimeter}'
    
    def display(self):
        for key, value in vars(self).items():
            print(f'{key} : {value}')
   
    def __call__(self, **kwargs):
        pass
#abstraction
#polimorphism(vghti dr class frznd poresh konim)
    @abstractmethod   
    def get_name(self,**kwargs):
        self._name=input('please enter your shape name: ')
        print(f'yor shapes name is {self._name}')
        
class three_d(shape):
    def __init__(self,side_area=None,total_area=None,**kwargs):
        super().__init__()
        self._side_area=side_area
        self._total_area=total_area

    def get_name(self):
        super().get_name()
        print('and this is a 3d shape')
        
    def side_area(self,**kwargs):
        print(f'your side area is {self._side_area}')
    
    def total_area(self,**kwargs):
        
        print(f'your total area is {self._total_area}')
    def Volume(self,**kwargs):
        pass
        
    def Perimeter(self,**kwargs):
        print('its 3d shape and dosent have perimeter')
    
class two_d(shape):
    def __init__(self,diameter=None,angle_between_diameter=None,**kwargs):
        super().__init__()
        self._diameter=diameter
        self.__angle_between_diameter=angle_between_diameter
    def Volume(self, **kwargs):
        print('your volume is 0,its 2d shape')
        
    def Perimeter(self,**kwargs):
        pass 
    
    def Area(self, **kwargs):
        pass
    
    def get_name(self):
        super().get_name()  
        print('and its a 2d shape')
    
class parallelogram(two_d):
    def __init__(self,smaller_side,bigger_side,hight_on_bigger_side,hight_on_smaller_side,**kwargs):
        super().__init__()
        self.smaller_side=smaller_side
        self.bigger_side=bigger_side
        self.hight_on_bigger_side=hight_on_bigger_side
        self.hight_on_smaller_side=hight_on_smaller_side
    
    def Volume(self,**kwargs):
        super().Volume()
    
    def Perimeter(self,**kwargs):
        return ((self.bigger_side)+(self.smaller_side))*2
    
    def Area(self,**kwargs):
        print('yor area is smaller_side * hight_on_smaller_side or bigger_side * hight_on_bigger_side')
        return (self.smaller_side) * (self.hight_on_smaller_side)
    
    def name(self):
        super().get_name()  
        print('and its kind of parallelogram')
    
    def detail(self,**kwargs):
        print(f'you have two side with size of {self.smaller_side} and two side with size of {self.bigger_side} ')
     
    def attribute(self,**kwargs):
        print('your diameter cut each other in half and the same opposite angles and up with down side and right with left side are parallel')

class trapezium(two_d):
    def __init__(self,up_side,down_side,right_side,left_side,hight):
        super().__init__()
        self.up_side=up_side
        self.down_side=down_side
        self.right_side=right_side
        self.left_side=left_side
        self.hight=hight
        
    def Volume(self,**kwargs):
        super().Volume()
    
    def Perimeter(self,**kwargs):
        return self.up_side + self.down_side + self.right_side + self.left_side
    
    def Area(self,**kwargs):
        print('yor area is (up_side + down_side) * hight/2')
        return ((self.up_side) + (self.down_side))* self.hight /2
    
    def detail(self,**kwargs):
        print('its diameter could be different')
    
    def attribute(self,**kwargs):
        print('it  have two side (up and down)which are parallel')
        
    def kind(self):
        if self.right_side == self.left_side:
            print('its an isosceles trapezoid')
        else:
            print('its an ordinary trapezium')
    
    def name(self):
        super().get_name()  
        print('and its kind of trapezium')
        
class triangle(two_d):
    def __init__(self,side1,side2,side3,hight1,hight2,hight3,**kwargs):
        super().__init__()
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.hight1=hight1
        self.hight2=hight2
        self.hight3=hight3

    def Volume(self,**kwargs):
        super().Volume()

    def Perimeter(self,**kwargs):
        return self.side1 + self.side2 + self.side3
    
    def Area(self,**kwargs):
        print('yor area is on side * hight of that side/2')
        return ((self.side1) * (self.hight1)) /2
    
    def kind(self):
        if self.side1==self.side2==self.side3:
            print('its an equilateral triangle')
            print('all of its angles are the same')
        elif self.side1==self.side2!=self.side3 or self.side1==self.side3!=self.side2 or self.side3==self.side2!=self.side1:
            print('its an isosceles triangle ')
            print('two angles are the same')
        elif (self.side1)**2==(self.side2)**2 +(self.side3)**2 or (self.side2)**2==(self.side1)**2 +(self.side3)**2 or (self.side3)**2==(self.side2)**2 +(self.side1)**2:
            print('its a right triangle')
            print('it has one angle that is 90 degree')
        else:
            print('its an ordinary triangle')
            
    def name(self):
        super().get_name()  
        print('and its kind of triangle')
        
class pentagon(two_d):
    def __init__(self,side1,side2,side3,side4,side5,**kwargs):
        super().__init__()
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.side4=side4
        self.side5=side5
        
    def Volume(self,**kwargs):
        super().Volume()
    
    def Perimeter(self,**kwargs):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5
    
    def kind(self):
        if self.side1==self.side2==self.side3==self.side4==self.side5:
            print('its a regular pentagon')
            print('all of the angles are the same')
        else:
            print('its an ordinary pentagon')

    def name(self):
        super().get_name()  
        print('and its kind of pentagon')

class circle(two_d):
    def __init__(self,radius,**kwargs):
        super().__init__()
        self.radius=radius
        self.__pi=3.14
    
    def Volume(self,**kwargs):
        super().Volume()
    
    def Perimeter(self):
        return 2*self.__pi*self.radius
    
    def diameter(self):
        return self.radius*2
    
    def Area(self):
        return (self.radius **2) *self.__pi

    def name(self):
        super().get_name()  
        print('and its kind of circle')
#aggrigation    
class diamond():
    def __init__(self,side1,side2,side3,side4,hight1,obj,**kwargs):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.side4=side4   
        self.hight1=hight1
        self.obj=obj
    
    def Volume (self,**kwargs):
        print('this is a 2d shape and dose not have volume')
    
    def Perimeter(self,**kwargs):
        return self.side1 + self.side2 + self.side3 + self.side4
    
    def Area(self,**kwargs):
        return self.obj.Area()
    #aggrigation az class motevazi al azla
    #obj ye objecte az class motevaze al azla
    def attribute (self,**kwargs):
        return self.obj.detail()
        print('you have 2 diameter that make 90 degree angle when they cut each other')
#aggrigation   
class rectangle():
    def __init__(self,side1,side2,diameter,d_angle,obj,**kwargs):
        self.side1=side1
        self.side2=side2 
        self.diameter=diameter
        self.d_angle=d_angle
        self.obj=obj
        
    #aggrigation az class motevazi al azla
    #obj ye objecte az class motevaze al azla
    def Volume(self):
        return self.obj.Volume()
    
    def Area(self,**kwargs):
        return self.obj.Area()
    
    def Perimeter(self):
        return (self.side1 + self.side2 )*2
    
    def attribute (self,**kwargs):
        return self.obj.attribute()
        print('you have 2 diameter that are the same size and 4 equal angle which are 90 degree')
##composition and aggrigation      
class square():
    def __init__(self,side1,obj,**kwargs):
        self.side1=side1
        self.__obj=obj
        self.__obj1=rectangle(self.side1,self.side1,self.side1,self.side1,self.side1,self.__obj)
        self.__obj2=diamond(self.side1,self.side1,self.side1,self.side1,self.side1,self.__obj)
        self.__d_angle=45
        
    def Volume(self):
        print('its volume can be calculated by volume of diamond or rectangle')
        return self.__obj1.Volume()
    
    def Area(self):
        return self.side1 **2
    
    def Perimeter(self):
        return self.side1 *4
    
    def attribute (self,**kwargs):
        return self.__obj1.attribute()
        return self.__obj2.attribute()
    def diameter(self):
        return self.side1 * 2**0.5
    
    
    
class spherical(three_d):
    def __init(self, radius):
        super().__init__()
        self.radius=radius
        self.__pi=3.14
    
    def Volume(self):
        return  4*self.__pi *(self.radius**3) /3
    
    def Area(self):
        return 4* self.__pi *(self.radius **2)
    
    def Perimeter(self):
        super().Perimeter()
        
    def detail(self):
        print('in this shape the total and the side area are the same')
     
    def name(self):
        super().get_name()
        print('and its kind of spherical')
        
class cone(three_d):
    def __init__(self,radius,hight):
        super().__init__()
        self.radius=radius
        self.hight=hight
        self.__pi=3.14
        
    def Volume(self):
        return self.__pi * (self.radius**2) * self.hight /3
    
    def side_area(self):
        return self.__pi * self.radius *((self.hight **2 + self.radius **2)**0.5)

    def total_area(self):
        return self.side_area() + self.__pi + self.radius **2

    def Perimeter(self):
        super().Perimeter()    

    def name(self):
        super().get_name()
        print('and its kind of cone')    
        
class pyramid(three_d):
    def __init__(self,side,hight,around_side,side_hight):
        super().__init__()
        self.side=side
        self.hight=hight
        self.side_hight=side_hight
        self.around_side=around_side

    def side_area(self):
        return 4* (self.side_hight * self.side /2)
    
    def total_area(self):
        return self.side_area() + self.side **2
    
    def Volume(self):
        return self.hight * (self.side **2)/3
    
    def Perimeter(self):
        super().Perimeter()  
        
    def name(self):
        super().get_name()
        print('and its kind of pyramid')
        
class cylinder(three_d):
    def __init__(self,radius,hight):
        super().__init__()
        self.radius=radius
        self.hight=hight
        self.__pi=3.14
    
    def Volume(self):
        return self.__pi * (self.radius**2) * self.hight
   
    def side_area(self):
        return 2* self.__pi * self.radius *self.hight

    def total_area(self):
        return self.side_area() + 2*( self.__pi + self.radius **2)

    def Perimeter(self):
        super().Perimeter()    

    def name(self):
        super().get_name()
        print('and its kind of cylinder')
     
        
        


    
    
         
    
        
    
    
        
        
        



    
            
    
    
























        
    
    
    
    
    
    
    
        
    
    
        
        






