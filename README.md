# Combinatorial-Algorithms
Some combinatorial algorithms for my thesis<br/>
About White-Williamson algorithm:<br/>
Given a set (for example: {2, 3, 7, 8}), let the set be a, we do the following process:<br/>
We append as first term of the set the number 0 (for example: {0, 2, 3, 7, 8})<br/>
Then, we do the following: we calculate the expression a[i]-2*i for every i=0, 1, ..., length of a<br/>
From all the calculation, we keep the i' such that the expression a[i]-2*i is minimum<br/>
After that, we append to the set a the number 1+a[i']<br/>


About Green-Kleitman/Leeb algorithm:<br/>
We take as input the whole set (for example {1, 2, 3, 4, 5, 6, 7, 8, 9}) and our initial set (for example {2, 3, 4, 7, 8})<br/>
We represent our initial set with parentheses. We put ")" if the element exists in the initial set, "(" otherwise. <br/>
for example: {2, 3, 4, 7, 8} -> {(,),),),(,(,),),(}<br/>
For all the closed parentheses, we keep the right elements (here: {2, 7, 8}). These are the basic elements.<br/>
Also, we keep the unpaired right elements of our set (here: {3, 4})<br/>
And finally, we keep the unpaired left elements of our set (here: {9})<br/>
If we append to the basic elements, the unpaired right elements and the unpaired left parentheses we have the symmetric chain decomposition.
