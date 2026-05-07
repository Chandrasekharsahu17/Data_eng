{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "da0e5ee6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:35.946158Z",
     "iopub.status.busy": "2026-05-07T05:07:35.945758Z",
     "iopub.status.idle": "2026-05-07T05:07:41.430214Z",
     "shell.execute_reply": "2026-05-07T05:07:41.428990Z"
    },
    "papermill": {
     "duration": 5.49191,
     "end_time": "2026-05-07T05:07:41.432531+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:35.940621+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\r\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1b3414c5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.441807Z",
     "iopub.status.busy": "2026-05-07T05:07:41.441401Z",
     "iopub.status.idle": "2026-05-07T05:07:41.446562Z",
     "shell.execute_reply": "2026-05-07T05:07:41.445648Z"
    },
    "papermill": {
     "duration": 0.012763,
     "end_time": "2026-05-07T05:07:41.448583+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.435820+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9786be6c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.456127Z",
     "iopub.status.busy": "2026-05-07T05:07:41.455788Z",
     "iopub.status.idle": "2026-05-07T05:07:41.466263Z",
     "shell.execute_reply": "2026-05-07T05:07:41.465387Z"
    },
    "papermill": {
     "duration": 0.016443,
     "end_time": "2026-05-07T05:07:41.468198+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.451755+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "(5,)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3, 4, 5]])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## 1d array \n",
    "\n",
    "a=np.array([1,2,3,4,5])\n",
    "print(type(a))\n",
    "print(a.shape)\n",
    "a2=a.reshape(1,5)\n",
    "a2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "021df6b3",
   "metadata": {
    "papermill": {
     "duration": 0.002971,
     "end_time": "2026-05-07T05:07:41.474346+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.471375+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### this is 2 dimension array as [[ are there at starting and closing "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ab3c5c78",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.482100Z",
     "iopub.status.busy": "2026-05-07T05:07:41.481643Z",
     "iopub.status.idle": "2026-05-07T05:07:41.487573Z",
     "shell.execute_reply": "2026-05-07T05:07:41.486706Z"
    },
    "papermill": {
     "duration": 0.01224,
     "end_time": "2026-05-07T05:07:41.489550+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.477310+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2164a287",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.497958Z",
     "iopub.status.busy": "2026-05-07T05:07:41.497264Z",
     "iopub.status.idle": "2026-05-07T05:07:41.503984Z",
     "shell.execute_reply": "2026-05-07T05:07:41.503114Z"
    },
    "papermill": {
     "duration": 0.013177,
     "end_time": "2026-05-07T05:07:41.505970+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.492793+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 4)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a3=np.array([[1,2,3,4],[3,4,5,7]])\n",
    "a3.shape\n",
    "\n",
    "## 2 dimesnion array as with shape as 2 rows and 4 columns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "893e2180",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.514645Z",
     "iopub.status.busy": "2026-05-07T05:07:41.513904Z",
     "iopub.status.idle": "2026-05-07T05:07:41.520984Z",
     "shell.execute_reply": "2026-05-07T05:07:41.519835Z"
    },
    "papermill": {
     "duration": 0.01379,
     "end_time": "2026-05-07T05:07:41.523083+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.509293+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 3, 5, 7, 9]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(1,10,2).reshape(1,5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "65aecc49",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.531638Z",
     "iopub.status.busy": "2026-05-07T05:07:41.531026Z",
     "iopub.status.idle": "2026-05-07T05:07:41.537793Z",
     "shell.execute_reply": "2026-05-07T05:07:41.536800Z"
    },
    "papermill": {
     "duration": 0.013482,
     "end_time": "2026-05-07T05:07:41.539932+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.526450+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1],\n",
       "       [3],\n",
       "       [5],\n",
       "       [7],\n",
       "       [9]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(1,10,2).reshape(5,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bfd95e6b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.549024Z",
     "iopub.status.busy": "2026-05-07T05:07:41.548265Z",
     "iopub.status.idle": "2026-05-07T05:07:41.555197Z",
     "shell.execute_reply": "2026-05-07T05:07:41.554260Z"
    },
    "papermill": {
     "duration": 0.013799,
     "end_time": "2026-05-07T05:07:41.557268+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.543469+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1., 1., 1., 1.],\n",
       "       [1., 1., 1., 1., 1., 1.],\n",
       "       [1., 1., 1., 1., 1., 1.]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ones((3,6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ced789ca",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.566760Z",
     "iopub.status.busy": "2026-05-07T05:07:41.565640Z",
     "iopub.status.idle": "2026-05-07T05:07:41.572444Z",
     "shell.execute_reply": "2026-05-07T05:07:41.571603Z"
    },
    "papermill": {
     "duration": 0.013454,
     "end_time": "2026-05-07T05:07:41.574334+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.560880+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0., 0., 0.],\n",
       "       [0., 1., 0., 0., 0.],\n",
       "       [0., 0., 1., 0., 0.],\n",
       "       [0., 0., 0., 1., 0.],\n",
       "       [0., 0., 0., 0., 1.]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.eye((5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "844d5ca9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.583965Z",
     "iopub.status.busy": "2026-05-07T05:07:41.583555Z",
     "iopub.status.idle": "2026-05-07T05:07:41.591946Z",
     "shell.execute_reply": "2026-05-07T05:07:41.590955Z"
    },
    "papermill": {
     "duration": 0.015633,
     "end_time": "2026-05-07T05:07:41.593959+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.578326+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11 25  7  9  7]\n",
      "[ -9 -21  -1  -1   3]\n",
      "[10 46 12 20 10]\n",
      "[100 529  16  25   4]\n"
     ]
    }
   ],
   "source": [
    "a1=np.array([1,2,3,4,5])\n",
    "a2=np.array([10,23,4,5,2])\n",
    "\n",
    "### element wise addition , sub , multipication, divison\n",
    "print(a1+a2)\n",
    "print(a1-a2)\n",
    "print(a1*a2)\n",
    "print(a2*a2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "77d25e7b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.602784Z",
     "iopub.status.busy": "2026-05-07T05:07:41.602420Z",
     "iopub.status.idle": "2026-05-07T05:07:41.608658Z",
     "shell.execute_reply": "2026-05-07T05:07:41.607816Z"
    },
    "papermill": {
     "duration": 0.013083,
     "end_time": "2026-05-07T05:07:41.610669+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.597586+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3.16227766 4.79583152 2.         2.23606798 1.41421356]\n",
      "[2.20264658e+04 9.74480345e+09 5.45981500e+01 1.48413159e+02\n",
      " 7.38905610e+00]\n",
      "[-0.54402111 -0.8462204  -0.7568025  -0.95892427  0.90929743]\n",
      "[2.30258509 3.13549422 1.38629436 1.60943791 0.69314718]\n"
     ]
    }
   ],
   "source": [
    "## Universal Functions \n",
    "\n",
    "\n",
    "print(np.sqrt(a2))\n",
    "\n",
    "print(np.exp(a2))\n",
    "\n",
    "print(np.sin(a2))\n",
    "\n",
    "print(np.log(a2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a6b41bfa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:07:41.620208Z",
     "iopub.status.busy": "2026-05-07T05:07:41.619843Z",
     "iopub.status.idle": "2026-05-07T05:07:41.626424Z",
     "shell.execute_reply": "2026-05-07T05:07:41.625626Z"
    },
    "papermill": {
     "duration": 0.013628,
     "end_time": "2026-05-07T05:07:41.628454+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.614826+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4],\n",
       "       [ 5,  6,  7,  8],\n",
       "       [ 9, 10, 11, 12]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## array slicing \n",
    "\n",
    "arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])\n",
    "\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "931a85c7",
   "metadata": {
    "papermill": {
     "duration": 0.003526,
     "end_time": "2026-05-07T05:07:41.635694+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:07:41.632168+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 31328,
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 9.630961,
   "end_time": "2026-05-07T05:07:42.058820+00:00",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2026-05-07T05:07:32.427859+00:00",
   "version": "2.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
