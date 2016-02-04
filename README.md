Geofence implementation in Python
=================================

This module can work with different shapes such as square, rectangle, polygon and
circle to check if a point lies inside them or not.


Application
===========

1. Vehicle tracking system for locating a vehicle or generating alerts.
2. Geolocation based software systems for writing  business logics based on location of the user. 
3. Computer graphics, in locating a point.

Usage
=====

1. Download the geofence.py.

2. Import and start using it.

```
    import geofence
   
    #An example of square 
    g = Geofence('polygon')
    g.set_shape( ( 1, 1 ), ( 1, 2 ), ( 2, 2 ), ( 2, 1 ) )
    print g.is_inside( ( 1.5, 1.5 ) )
    print g.is_inside( ( 4.9, 1.2 ) )
    print g.is_inside( ( 1.8, 1.1 ) )


    #An example of circle
    g = Geofence('circle')
    g.set_shape( ( 1 , 1 ), 3)
    print g.is_inside( ( 1.5, 1.5 ) )
    print g.is_inside( ( 4.9, 1.2 ) )
    print g.is_inside( ( 1.8, 1.1 ) ) 

```

Disclaimer
==========

This module is not production ready, and has not been tested enough.

License
=======

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
