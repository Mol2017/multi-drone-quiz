import time
from result import *


def esdf(M, N, obstacle_list):
    """
    Implemented the distance transformation from "Distance Transforms of Sampled Functions"
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    grid_map = np.zeros((M, N))
    for obs in obstacle_list:
        grid_map[obs[0], obs[1]] = 1

    # 1) deal with distance transform in cols
    esdf_map = np.zeros((M, N))
    for j in range(N):
        # construct input for 1d distance transform
        pos = np.array([])
        for i in range(M):
            if grid_map[i, j] == 1:
                pos = np.append(pos, i)
        # perform 1d distance transform
        D = distance_transform(M, pos, np.zeros(M))
        esdf_map[:, j] = D

    # 2) deal with distance transform in rows
    for i in range(M):
        # construct input for 1d distance transform
        pos = np.array([])
        f = np.array([])
        for j in range(N):
            if esdf_map[i, j] != float("inf"):
                pos = np.append(pos, j)
                f = np.append(f, esdf_map[i, j])
            else:
                f = np.append(f, 0.)
        # perform 1d distance transform
        D = distance_transform(N, pos.astype(int), f)
        esdf_map[i, :] = D
    return np.sqrt(esdf_map)


def distance_transform(n, pos, f):
    """
    Perform 1d distance transformation
    e.g.
    [Inf, 0, 4]
    input: n = 3, pos = [1, 2], f = [0, 0, 4]
    output: [1, 0, 1]

    :param n: vector size
    :param pos: pos where there is a parabola (n,)
    :param f: addition value besides l2-norm  (n,)
    :return: An array. The value of each cell means the closest distance to the obstacle (n,)
    """
    parabola_size = pos.size
    if parabola_size == 0:
        return np.full(n, float("inf"))

    k = 0
    v = np.array([])
    v = np.append(v, pos[k])

    z = np.array([])
    z = np.append(z, float("-inf"))
    z = np.append(z, float("inf"))

    idx = 1
    while idx < parabola_size:
        q = pos[idx].astype(int)
        s = ((f[q] + q*q) - (f[v[k].astype(int)] + v[k]*v[k])) / (2*q - 2*v[k])
        if s <= z[k]:
            k = k - 1
            continue
        else:
            k = k + 1
            v = np.append(v, q)
            z[k] = s
            z = np.append(z, float("inf"))
            idx += 1

    k = 0
    D = np.zeros(n)
    for i in range(n):
        while z[k+1] < i:
            k = k + 1
        D[i] = (i - v[k]) * (i - v[k]) + f[v[k].astype(int)]
    return D


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
