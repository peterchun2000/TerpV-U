# TerpV'U

### Inspiration/Problem to Solve

Whether you're a Public Speaker, Professor, or even a Pastor, there has always been moments where you've seen people dose off on your their smartphones (you might be one yourself). Excessive phone usage can be an indication of a boring speech, an uninterested crowd of students, etc. Wouldn't it be nice to be able to quantitatively visualize how many people were on their phone and for how long? 

### How?

Current, smartphone/phone detection Vision AI models can only be used from a relatively short distance. Thus, the capability of detecting the number of phone in a large lecture hall or conference room is virtually impossible with this approach. However, smartphone screens emit a small amount of Inferred light (IR), which we can take advantage of. By modifying a webcam to only let through inferred light, we can create a simple yet effective vision model that detects and tracks the IR light emitted by smartphones. This can easily be implemented large scale by placing the camera above and slightly behind the audience. 

### Technology

We decided to utilize a simple Logitech webcamera for the hardware. As for the software development side, we used **Flask** (a Python web framework), **OpenCV** (a computer vision library), and **Bootstrap** (a CSS framework). 

### Implementation

