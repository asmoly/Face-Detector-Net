# Face Detector Net
 
Wider Faces Dataset: http://shuoyang1213.me/WIDERFACE/

Video about this project: 
 
This is a cnn net that is able to find faces in an image. I used the wider faces dataset to train the neural network.

It takes in an RGB image as a tensor and outputs a tensor of the image where each pixel has 5 values. The first one is how likely it is that there is a face there, the rest of the values are coordinates for the bounding box which are regressed. The first two are values of a vector that points to the upper left corner of the bounding boxes from the pixel's coordinates, and the second two are the width and height.

On the left is a mask which represents the likelyhood of there being a face in ever pixel. The white pixels are where the neural net thinks there is a face. There are a few random white pixels that show up where there isn't a face but that is dealt with in post proccessing.

More specificaly this net has 13 convolutional layers and 8 deconvolution layers. In the convolutional layers the images size is decreased by a factor of 2, 4 times. And in the deconvolutional layers the image is increased by a factor of 2, 2 times.

After the neural net has given a result it needs to somehow create the bounding box around the face so that it isn't just a bunch of pixels floating around. So, there is a program which finds all the groups of pixels that are connected, it then check to make sure the amount of pixels in that group is more than a certain threshhold to cast out any stray pixels. Since each pixel has values for a bounding box, it takes the average of all the values to get the final bounding box

The other way I could have made this neural net was by just outputing coordinates of the bounding box rather than ouputing every pixel, but this would limit the amount of faces I could find because there would be a limited amount of coordinates that the neural net could output. But since I used a mask the neural net is able to find as many faces as you want.

Using the neural network:
