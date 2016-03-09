#!/bin/env python

from PIL import Image
import math

imonx=1000
imony=1000

mimonx=imonx/2
mimony=imony/2

mimonm=(mimonx+mimony)/2.

def neigbours(nx,ny):
  nxm=max(nx-1,0)
  nxM=min(imonx,nx+1)
  nym=max(ny-1,0)
  nyM=min(imony,ny+1)
  
  return (nxm,nym,nxM,nyM)
  

def smothimo(imoray):
  print "smothimo()"
  out=False
  for ix in range(imonx):
    for iy in range(imony):
      if ( (ix-mimonx)*(ix-mimonx)+(iy-mimony)*(iy-mimony) < mimonm*mimonm ):
        if (imoray[ix][iy][3]==0):
          out=True
          (nxm,nym,nxM,nyM)=neigbours(ix,iy)
          for iix in range(nxm,nxM):
            for iiy in range(nym,nyM):
              for iii in range(4):
                imoray[ix][iy][iii]+=imoray[iix][iiy][iii]
  return out





def main():
  imi = Image.open("../../common/data/earth_surface_map.jpg")

  (iminx,iminy)=imi.size


  imoray=[]

  for ix in range(imonx):
    imoray.append([])
    for iy in range(imony):
      imoray[ix].append([0,0,0,0])

  cpt=0
  for px in imi.getdata():
    cpt+=1
    ix=cpt%iminx
    iy=cpt/iminx
    theta=ix*2.*3.141592653/iminx
    r=iy*1.0/imony
    
    ox=min(int(math.cos(theta)*r*mimonx+mimonx),imonx-1)
    oy=min(int(math.sin(theta)*r*mimony+mimony),imony-1)
    
    #print ("ix="+str(ix)+"   iy="+str(iy)+"   theta="+str(theta)+"   r="+str(r)+"  ox="+str(ox))
    
    #print (ox,oy)
    
    imoray[ox][oy][0]+=px[0]
    imoray[ox][oy][1]+=px[1]
    imoray[ox][oy][2]+=px[2]
    imoray[ox][oy][3]+=1
    
  
  #while (smothimo(imoray)):
  #  pass
  imoral=[]
  for lx in imoray:
    for px in lx:
      if (px[3]>0):
        r=int(px[0]/px[3])
        g=int(px[1]/px[3])
        b=int(px[2]/px[3])
      else:
        r=g=b=0
      imoral.append((r,g,b))
    
  
  imo=Image.new("RGB",(imonx,imony))
  imo.putdata(imoral)

  imo.save("test.jpg")



main()