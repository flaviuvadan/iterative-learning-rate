# iterative-learning-rate
A small experiment to learn how the learning rate changes over multiple iterations of a network's learning step. 

The basis of how the learning rate decays is taken from Deep Learning by Goodfellow et. al (287).

Definition of decay:

ε<sub>k</sub> = (1 - α)ε<sub>0</sub> + αε<sub>τ</sub>

where:

ε<sub>0</sub> - initial learning rate

ε<sub>k</sub> - learning rate at iteration k

αε<sub>τ</sub> - final learning rate

α - k/τ



### Results

#### 100 iterations
![](plot_100.png)

#### 1000 iterations
![](plot_1000.png)

#### 10000 iterations
![](plot_10000.png)                

