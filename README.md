# multi-drone-quiz
The repo is a python implementation of the ESDF method presented in paper "Distance Transforms of Sampled Functions".
## Run
```bash 
python main.py
```
## Brief Explanation
The paper presented a detail 1D distance transform function DT(F)   
To compute 2D ESDF map of size (m, n),   
(1) compute 1D distance transform for each column in 2D grid.   
(2) compute 1D distance transform for each row based on (1)'s result, and then we have the 2D ESDF map.   

Computational complexity: O(m*n)
