# LeetCode - Problem 857 - Minimum Cost to Hire K Workers

There are `N` workers. The `i`-th worker has a `quality[i]` and a minimum wage 
expectation `wage[i]`.

Now we want to hire exactly `K` workers to form a ___paid group___.  When hiring a group of K 
workers, we must pay them according to the following rules:

1.  Every worker in the paid group should be paid in the ratio of their quality 
    compared to other workers in the paid group.
1.  Every worker in the paid group must be paid at least their minimum wage 
    expectation.

Return the least amount of money needed to form a paid group satisfying the above
conditions.


 
```
Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
```

**Note:**

* `1 <= K <= N <= 10000`, where `N = quality.length = wage.length`
* `1 <= quality[i] <= 10000`
* `1 <= wage[i] <= 10000`
* Answers within `10^-5` of the correct answer will be considered correct.

## Solution Proof:

Algorithm: 

Divide ![equation](https://latex.codecogs.com/svg.latex?W_%7Bi%7D) by ![equation](https://latex.codecogs.com/svg.latex?q_%7Bi%7D), sort ![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BW_%7Bi%7D%7D%7Bq_%7Bi%7D%7D) hence

![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BW_%7B1%7D%7D%7Bq_%7B1%7D%7D%20%3C%20%5Cfrac%7BW_%7B2%7D%7D%7Bq_%7B2%7D%7D%20%3C%20%5Ccdots%20%3C%20%5Cfrac%7BW_%7Bk%7D%7D%7Bq_%7Bk%7D%7D%20%3C%20%5Cfrac%7BW_%7Bk&plus;1%7D%7D%7Bq_%7Bk&plus;1%7D%7D%20%3C%20%5Ccdots%20%3C%20%5Cfrac%7BW_%7BN%7D%7D%7Bq_%7BN%7D%7D) [ called ratio )

First step pick up first ![equation](https://latex.codecogs.com/svg.latex?k%5E%7Bth%7D) ratios.
Then sum of salaries with ratio ![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BW_%7Bk%7D%7D%7Bq_%7Bk%7D%7D) is:

![equation](https://latex.codecogs.com/svg.latex?sum_%7Bk%7D%20%3D%20%28%5Csum_%7Bi%3D1%7D%5E%7Bk-1%7Dq_%7Bi%7D&plus;q_%7Bk%7D%29%5Ctimes%5Cfrac%7BW_%7Bk%7D%7D%7Bq_%7Bk%7D%7D)

**(1)**

We can prove the ![equation](https://latex.codecogs.com/svg.latex?sum_%7Bk%7D) is valid, which means
each worker ![equation](https://latex.codecogs.com/svg.latex?i%3D1%2C...%2Ck) are paid more than the minimum
wage they expect :

![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BW_%7Bi%7D%7D%7Bk_%7Bi%7D%7D%20%3C%20%5Cfrac%7BW_%7Bk%7D%7D%7Bk_%7Bk%7D%7D%20%5Cforall%20i%20%3C%20k)

=> ![equation](https://latex.codecogs.com/svg.latex?W_%7Bi%7D%20%3C%20%5Cfrac%7BW_%7Bk%7D%7D%7Bk_%7Bk%7D%7D%20%5Ctimes%20q_%7Bi%7D)

=> In ![equation](https://latex.codecogs.com/svg.latex?sum_%7Bk%7D),

![equation](https://latex.codecogs.com/svg.latex?%28%5Csum_%7Bi%3D1%7D%5E%7Bk-1%7Dq_%7Bi%7D&plus;q%7Bk%7D%29%20%5Ctimes%20%5Cfrac%7BW_%7Bk%7D%7D%7Bq_%7Bk%7D%7D) , ![equation](https://latex.codecogs.com/svg.latex?%5Cforall%20i) , ![equation](https://latex.codecogs.com/svg.latex?q_%7Bi%7D%20%5Ctimes%20%5Cfrac%7BW_%7Bk%7D%7D%7Bq_%7Bk%7D%7D%20%3E%20W_%7Bi%7D)

means for each worker we paid enough.

**(2)**

for ![equation](https://latex.codecogs.com/svg.latex?sum_%7Bk+1%7D) ,

![equation](https://latex.codecogs.com/svg.latex?sum_%7Bk&plus;1%7D%20%3D%20%28%5Csum_%7Bi%3D1%7D%5E%7Bj-1%7Dq_%7Bi%7D%20&plus;%20%5Csum_%7Bi%3Dj&plus;1%7D%5E%7Bk%7Dq_%7Bi%7D&plus;q_%7Bk&plus;1%7D%29%20%5Ctimes%20%5Cfrac%7BW_%7Bk&plus;1%7D%7D%7Bq_%7Bk&plus;1%7D%7D), 

where,

![equation](https://latex.codecogs.com/svg.latex?q_%7Bj%7D%20%3E%20q_%7Bi%7D) , ![equation](https://latex.codecogs.com/svg.latex?%5Cforall%20i%20%3C%20k&plus;1)

is the smallest sum if we use ratio ![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BW_%7Bk&plus;1%7D%7D%7Bq_%7Bk&plus;1%7D%7D).

So as we pick up next worker with bigger ratio, 
we remove a worker with highest quality, 
this will guarantee in each step we will get
the min sum with a specific ratio.

Find all `N-k+1` sums, choose the min one as the result:

![equation](https://latex.codecogs.com/svg.latex?result%20%3D%20min%28sum_%7Bk%7D%2Csum_%7Bk&plus;1%7D%2C%5Ccdots%2Csum_%7BN%7D%29)


