import math

deg180 = math.pi
deg90 = deg180/2

for i in range(3, 11):
    topHeight = math.tan(deg90-deg180/i)
    bottomHeight = math.tan(deg90/i)
    width = math.sqrt(topHeight*bottomHeight) # Such that width/topHeight = bottomHeight/width
    topAngle = 2*math.atan(width/topHeight)
    bottomAngle = deg180-topAngle
    longLength = math.sqrt(topHeight**2+width**2)
    shortLength = math.sqrt(bottomHeight**2+width**2)
    print(f"{i}: top angle: {topAngle/math.pi*180} or {topAngle}, bottom angle: {bottomAngle/math.pi*180} or {bottomAngle}, long length: {longLength}, short length: {shortLength}")
