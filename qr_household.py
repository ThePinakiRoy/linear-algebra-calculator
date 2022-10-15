import numpy as np
import streamlit as st


def column_convertor(x):
    """
    Converts 1d array to column vector
    """
    x.shape = (1, x.shape[0])
    return x


def get_norm(x):
    """
    Returns Norm of vector x
    """
    return np.sqrt(np.sum(np.square(x)))


def householder_transformation(v):
    """
    Returns Householder matrix for vector v
    """
    st.write('v\n', v)
    size_of_v = v.shape[1]
    e1 = np.zeros_like(v)
    e1[0, 0] = 1
    norm = get_norm(v)
    st.write('norm', norm)
    vector = norm * e1
    st.write('v\n', vector)
    if v[0, 0] < 0:
        vector = - vector
    e = (v + vector).astype(np.float32)
    st.write('e\n', e)
    u = (e / get_norm(e)).astype(np.float32)
    st.write('u\n', u)
    H = np.identity(size_of_v) - ((2 * np.matmul(np.transpose(u), u)) / np.matmul(u, np.transpose(u)))
    st.write('H\n', H)
    return H


def qr_step_factorization(q, r, iterator, n):
    """
    Return Q and R matrices for iterator number of iterations.
    """
    v = column_convertor(r[iterator:, iterator])
    Hbar = householder_transformation(v)
    H = np.identity(n)
    H[iterator:, iterator:] = Hbar
    r = np.matmul(H, r)
    st.write('R\n', r)
    q = np.matmul(q, H)
    st.write('q\n', q)
    return q, r


def house_holder_method():
    # Reading order of matrix
    m = int(st.number_input('Enter order of matrix m: '))
    n = int(st.number_input('Enter order of matrix n: '))

    # Making numpy array of n x n size and initializing
    # to zero for storing matrix
    a = np.zeros((m, n))

    # Reading matrix
    st.write('Enter Matrix Coefficients:')
    for i in range(m):
        for j in range(n):
            a[i][j] = st.number_input('a[' + str(i+1) + '][' + str(j+1) + ']=', step=1, format="%i")

    st.write('matrix A', a)
    Q = np.identity(n)
    R = a.astype(np.float32)
    for i in range(min(n, m)):
        st.write('STEP', i, '-' * 20)
        # For each iteration, H matrix is calculated for (i+1)th row
        Q, R = qr_step_factorization(Q, R, i, n)
    min_dim = min(m, n)
    R = np.around(R, decimals=6)
    R = R[:min_dim, :min_dim]
    Q = np.around(Q, decimals=6)
    st.write('A after QR factorization')
    st.write('R matrix')
    st.write(R, '\n')
    st.write('Q matrix')
    st.write(Q)

