set terminal png size 1024, 768
set output ARG2
set style data lines
set key right
set datafile separator ","

# Training loss vs. training iterations
set title "Training loss vs. training iterations"
set xlabel "Training iterations"
set ylabel "Training loss"
plot ARG1 using 1:ARG3

# the passed results ARG should be the titles of file, instead of number of column

