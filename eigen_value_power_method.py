import numpy as np
import streamlit as st


def eigen_value_power_method():
    # Reading order of matrix
    n = int(st.number_input('Enter order of matrix: '))

    # Making numpy array of n x n size and initializing
    # to zero for storing matrix
    a = np.zeros((n, n))

    # Reading matrix
    st.write('Enter Matrix Coefficients:')
    for i in range(n):
        for j in range(n):
            a[i][j] = st.number_input('a[' + str(i+1) + '][' + str(j+1) + ']=', step=1, format="%i")

    # Making numpy array n x 1 size and initializing to zero
    # for storing initial guess vector
    x = np.zeros((n))

    # Reading initial guess vector
    st.write('Enter initial guess vector: ')
    for i in range(n):
        x[i] = st.number_input('x[' + str(i) + ']=', step=1, format="%i")

    # Reading tolerable error
    #tolerable_error = st.number_input('Enter tolerable error: ', step=1, format="%i")

    # Reading maximum number of steps
    max_iteration = int(st.number_input('Enter maximum number of steps: '))

    # Power Method Implementation
    lambda_old = 1.0
    condition = True
    step = 1
    while condition:
        # Multiplying a and x
        x = np.matmul(a, x)

        # Finding new Eigen value and Eigen vector
        lambda_new = max(abs(x))

        x = x / lambda_new

        # Displaying Eigen value and Eigen Vector
        st.write('\nSTEP %d' % step)
        st.write('----------')
        st.write('Eigen Value = %0.4f' % lambda_new)
        st.write('Eigen Vector: ')
        # for i in range(n):
        #     st.write('%0.3f\t' % (x[i]))
        st.write(x)

        # Checking maximum iteration
        step = step + 1
        if step > max_iteration:
            st.write('Not convergent in given maximum iteration!')
            break

        # Calculating error
        error = abs(lambda_new - lambda_old)
        st.write('error=' + str(error))
        lambda_old = lambda_new
        condition = error > 0.01
