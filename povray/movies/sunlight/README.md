* Hum

One day we'll do that:
   - Run getmaps.sh to fill data/inputimages
   - Run numbering.sh to fill data/out1 with simple symlinks of previous images (simplifying subsequent scripts)
   - Run generatespolar.sh to fill data/out2 with polar (pizza) version


Right now, reusing old data, we have:
   - data/oldata/data/out0: original 2017 images (not available now, as they added a banner) 1200x600
   - data/oldata/data/out1: symlinks to out0, generated by ./numbering.sh
   - data/oldata/data/out2: flat version made by the polar.sh script (some way, couldn't replicate), numbered 0-flat.jpg to 359-flat.jpg 500x500
   - data/oldata/data/out3: run povray avec VERTICAL=false
