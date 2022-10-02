# multi-drone-quiz
The repo is a python implementation of the ESDF method presented in paper "Distance Transforms of Sampled Functions".
## Run
```bash 
python main.py
```
## Brief Explanation
The paper presented a detail 1D distance transform function DT(F)   
To compute 2D ESDF map,   
First, we compute 1D distance transform for each column in 2D grid.   
Second, we compute 1D distance transform for each row based on (1)'s result.   
