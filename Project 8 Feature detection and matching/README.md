### This computer vision project used Feature matching from OpenCV and added little code for calculation total price of the items the computer have seen and matched. 

**The workflow of this program**
1. Get names of items from files' name (Picture files) and saved them in list.

2. Create price list that corresponding with the name list. 

3. Create dictionary by using name list as keys and price list as values.

4. Feature matching the saved pictures and items appeared on the webcam video using code from OpenCV document. 

![matcher_flann](https://user-images.githubusercontent.com/123642022/221353107-3edf34da-cc17-40e1-8246-4e31d30c9fe4.jpg)

source: <https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html>

5. When the item was matched, item's name will be recalled and used as key to get item's value for calculation.

![Screenshot_20230225_052612](https://user-images.githubusercontent.com/123642022/221353296-3a775f94-f428-4786-b6d2-058fbd7ec94f.png)

6. Press esc to end the program. 

---


