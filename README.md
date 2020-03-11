# caMicroscope-GSoC-2020-code-challenge
<h2>Problem statement:</h2>
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image. For example, given an image with both cats and dogs, return bounding boxes for only cats.
<h2>Solution:</h2>
<h3>Approach</h3>
Tiny Yolo architecture was used which is as shown below:
<a href="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/Tinyyolo_architecture.png"></a>
Weights: <a href="images/Tinyyolo_architecture.jpg">yolo-tiny.h5</a>
<h2>Results:</h2>
<h3>Input Image:</h3>
<a href="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/input.jpg"></a>
<h3>Output Image:</h3>
<a href="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/prediction_output.jpg"></a>
