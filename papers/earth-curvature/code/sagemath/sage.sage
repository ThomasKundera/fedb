# Earth Radius
#r = 6371000
#e = 0.05

r=var('r')
e=var('e')

x=var('x')
y=var('y')
z=var('z')

h=var('h')

l = r*sqrt( (h*(2*r+h))/( (r+h)^2 ) )

hp=(r*h)/(r+h)

eq1 = x^2+y^2==l^2
eq2 = y==hp


print eq1
print eq2


xp=var('xp')
yp=var('yp')
zp=var('zp')

eqx = xp==e*x/z
eqy = yp==((y-h)/z)*e+h
eqz = zp==z

print solve([eqx,eqy,eqz,],x,y,z,h,e,r)
