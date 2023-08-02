{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4bcc54e8",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/n0/rkwtckfd7j35dbrwbf4389fw0000gn/T/ipykernel_53147/2106408788.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     45\u001b[0m     \u001b[0;31m# Add a source term:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     46\u001b[0m     \u001b[0mQ\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnPts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 47\u001b[0;31m     \u001b[0mQ\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m3\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mx\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m7\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m100\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m     \u001b[0;31m# solve for Temperature:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from tridiagonal import solve_tridiagonal\n",
    "\n",
    "# ----------------------------------------------------------------------\n",
    "# Main code\n",
    "# ----------------------------------------------------------------------\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    dx = 0.25\n",
    "\n",
    "    # set x with 1 ghost cell on both sides:\n",
    "    x = np.arange(-dx, 10 + 2 * dx, dx)\n",
    "\n",
    "    t_lower = 200.0\n",
    "    t_upper = 1000.0\n",
    "\n",
    "    nPts = len(x)\n",
    "    lam = 10.0\n",
    "    dz = x[1] - x[0]\n",
    "    DZ = dz * dx\n",
    "\n",
    "    # set default coefficients for the solver:\n",
    "    a = np.zeros(nPts) - 1\n",
    "    b = np.zeros(nPts) + 2\n",
    "    c = np.zeros(nPts) - 1\n",
    "    d = np.zeros(nPts)\n",
    "    #d = (Q*(dx)**2)/lam\n",
    "\n",
    "    # boundary conditions (bottom - fixed):\n",
    "    a[0] = 1\n",
    "    b[0] = -1\n",
    "    c[0] = 0\n",
    "    d[0] = t_lower\n",
    "\n",
    "    # top - fixed:\n",
    "    a[-1] = 0\n",
    "    b[-1] = 1\n",
    "    c[-1] = 0\n",
    "    d[-1] = t_upper\n",
    "\n",
    "    # Add a source term:\n",
    "    Q = np.zeros(nPts)\n",
    "    Q[(x > 3 and x < 7)] = 100\n",
    "    \n",
    "    # solve for Temperature:\n",
    "    t = solve_tridiagonal(a, b, c, d)\n",
    "\n",
    "    # plot:\n",
    "    fig = plt.figure(figsize = (10,10))\n",
    "    ax = fig.add_subplot(111)\n",
    "\n",
    "    ax.plot(x, t)\n",
    "\n",
    "    plotfile = 'conduction_v1.png'\n",
    "    print('writing : ',plotfile)    \n",
    "    fig.savefig(plotfile)\n",
    "    plt.close()\n",
    "    plt.show()\n",
    "    \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "79349f01",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/n0/rkwtckfd7j35dbrwbf4389fw0000gn/T/ipykernel_53147/1567282554.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     45\u001b[0m     \u001b[0;31m# Add a source term:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     46\u001b[0m     \u001b[0mQ\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnPts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 47\u001b[0;31m     \u001b[0mQ\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m3\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mx\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m7\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m100\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m     \u001b[0;31m# solve for Temperature:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from tridiagonal import solve_tridiagonal\n",
    "\n",
    "# ----------------------------------------------------------------------\n",
    "# Main code\n",
    "# ----------------------------------------------------------------------\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    dx = 0.25\n",
    "\n",
    "    # set x with 1 ghost cell on both sides:\n",
    "    x = np.arange(-dx, 10 + 2 * dx, dx)\n",
    "\n",
    "    t_lower = 200.0\n",
    "    t_upper = 1000.0\n",
    "\n",
    "    nPts = len(x)\n",
    "    lam = 10.0\n",
    "    dz = x[1] - x[0]\n",
    "    DZ = dz * dx\n",
    "\n",
    "    # set default coefficients for the solver:\n",
    "    a = np.zeros(nPts) - 1\n",
    "    b = np.zeros(nPts) + 2\n",
    "    c = np.zeros(nPts) - 1\n",
    "    d = np.zeros(nPts)\n",
    "    #d = (Q*(dx)**2)/lam\n",
    "\n",
    "    # boundary conditions (bottom - fixed):\n",
    "    a[0] = 0\n",
    "    b[0] = 1\n",
    "    c[0] = 0\n",
    "    d[0] = t_lower\n",
    "\n",
    "    # top - fixed:\n",
    "    a[-1] = 0\n",
    "    b[-1] = 1\n",
    "    c[-1] = 0\n",
    "    d[-1] = t_upper\n",
    "\n",
    "    # Add a source term:\n",
    "    Q = np.zeros(nPts)\n",
    "    Q[(x > 3 and x < 7)] = 100\n",
    "    \n",
    "    # solve for Temperature:\n",
    "    t = solve_tridiagonal(a, b, c, d)\n",
    "\n",
    "    # plot:\n",
    "    fig = plt.figure(figsize = (10,10))\n",
    "    ax = fig.add_subplot(111)\n",
    "\n",
    "    ax.plot(x, t)\n",
    "\n",
    "    plotfile = 'conduction_v1.png'\n",
    "    print('writing : ',plotfile)    \n",
    "    fig.savefig(plotfile)\n",
    "    plt.close()\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f231ec8c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0c50240",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
