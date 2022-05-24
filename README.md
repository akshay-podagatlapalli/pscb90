# Machine learning assisted search for new materials for Li-ion batteries and Perovskite based LEDs light-emitting diode (PeLEDs)

## Project Description
Solid-state  electrolytes  promise  to  improve  battery  safety  as  well  as  increase  the charging speed. There  is only  a handful of materials with known good ionic conductivity and a broader screening  is  urgently  needed. This is one of the research topics being pursued by the [Clean Energy Lab](http://cleanenergy.utoronto.ca/research/) at the University of Toronto.

I worked at the Clean Energy Lab during the summer of 2020, where I assisted the lab in employing machine learning approaches, in particular, one-shot learning and transfer learning, to predict ionic conductivity for a database of 1 mln materials without the need for computationally expensive quantum chemistry methods. 

The deep learning model that was being evaluated on its predictive accuracy is the [Crystal Graph Convolutional Neural Network - CGCNN](https://github.com/txie-93/cgcnn). The code I've written was primarily utilized to test if the CGCNN was able to utilize molecular information such as bond angles in making its predictions and in identifying methods to incorporate such molecular information to improve the predictive capabilities of the model.     
