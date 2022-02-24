# Class Discussion Notes

## Group Thoughts on Distinctions and Utility of Suffix Trees V Suffix Arrays
1. Suffix trees are better for large scale datasets (DNA) with a lot of repetition
2. Suffix trees are better for finding palindromes. 
3. If you are going to search the same string over and over, suffix trees are better because you can build an index over and over.
4. Suffix three to five times larger in their consumption of memory space.
5. Arrays are more common in most systems
6. Arrays can be thought about as compressed trees. 
7. Suffix trees adapt better to somewhat minor changes to the trees, because the changes to the index are smaller. 
8. With suffix arrays there is a trade off between performance and space. More space == better performance. Less space == lower performance. 
    - This is a result of compression / decompression
    - Similar to above, the  more similar the string, the greater the compression; but also here the greater the cost of decompression. 
9. Since the suffix arrays are sorted, when you retrieve the suffix array it can go from n(Log(n)) to n^2(log(n)). 

## Readings
1. Suffix-Arrays-Presentation is easy to understand
2. Suffix-trees-arrays-contrasted had an easy to follow presentation
3. Suffix-array : Straightforward. Included exact presentation of why suffix arrays are optimal in many cases compared to suffix trees. There is actual C++ code that was easier to follow. 
4. Suffix-trees-simple had the best example of suffix trees.
5. Suffix-tree started out pretty well, then got confusing pretty fast. Required a pen and paper to start writing it out and understanding it. 