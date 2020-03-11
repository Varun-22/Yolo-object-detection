# caMicroscope-GSoC-2020-code-challenge
<h2>Problem statement:</h2>
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image. For example, given an image with both cats and dogs, return bounding boxes for only cats.
<h2>Solution:</h2>
<h3>Approach</h3>
Tiny Yolo architecture was used which is as shown below:
<img src="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/Tinyyolo_architecture.png"></a>
Weights: <a href="https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5">yolo-tiny.h5</a>
<h2>Results:</h2>
<h3>Input Image:</h3>
<img src="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/input.jpg">
<h3>Output Image:</h3>
<img src="https://github.com/Varun-22/caMicroscope-GSoC-2020-code-challenge/blob/master/images/prediction_output.jpg">
<h3>Running the code:</h3>
The ipynb of the code provided was implemented in google colab environment. If you already have the required libraries, run from cell 2.
Since it was colab, cv2_imshow was used. For running on local system, use cv2.imshow.
