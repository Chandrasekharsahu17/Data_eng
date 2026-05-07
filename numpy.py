{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "49b1b7a8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:12.823897Z",
     "iopub.status.busy": "2026-05-07T05:49:12.822782Z",
     "iopub.status.idle": "2026-05-07T05:49:17.638258Z",
     "shell.execute_reply": "2026-05-07T05:49:17.637176Z"
    },
    "papermill": {
     "duration": 4.822023,
     "end_time": "2026-05-07T05:49:17.640125+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:12.818102+00:00",
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
   "id": "e5145f55",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.648605Z",
     "iopub.status.busy": "2026-05-07T05:49:17.647534Z",
     "iopub.status.idle": "2026-05-07T05:49:17.653912Z",
     "shell.execute_reply": "2026-05-07T05:49:17.652517Z"
    },
    "papermill": {
     "duration": 0.012909,
     "end_time": "2026-05-07T05:49:17.655885+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.642976+00:00",
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
   "id": "4fff9994",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.662456Z",
     "iopub.status.busy": "2026-05-07T05:49:17.662060Z",
     "iopub.status.idle": "2026-05-07T05:49:17.671107Z",
     "shell.execute_reply": "2026-05-07T05:49:17.670092Z"
    },
    "papermill": {
     "duration": 0.014463,
     "end_time": "2026-05-07T05:49:17.672833+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.658370+00:00",
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
   "id": "f3ab0cca",
   "metadata": {
    "papermill": {
     "duration": 0.002432,
     "end_time": "2026-05-07T05:49:17.677950+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.675518+00:00",
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
   "id": "14ff2d4c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.684252Z",
     "iopub.status.busy": "2026-05-07T05:49:17.683891Z",
     "iopub.status.idle": "2026-05-07T05:49:17.689765Z",
     "shell.execute_reply": "2026-05-07T05:49:17.688743Z"
    },
    "papermill": {
     "duration": 0.01176,
     "end_time": "2026-05-07T05:49:17.692011+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.680251+00:00",
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
   "id": "91802200",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.698804Z",
     "iopub.status.busy": "2026-05-07T05:49:17.698486Z",
     "iopub.status.idle": "2026-05-07T05:49:17.704698Z",
     "shell.execute_reply": "2026-05-07T05:49:17.703732Z"
    },
    "papermill": {
     "duration": 0.01233,
     "end_time": "2026-05-07T05:49:17.707129+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.694799+00:00",
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
   "id": "73853c94",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.715852Z",
     "iopub.status.busy": "2026-05-07T05:49:17.715458Z",
     "iopub.status.idle": "2026-05-07T05:49:17.721712Z",
     "shell.execute_reply": "2026-05-07T05:49:17.720859Z"
    },
    "papermill": {
     "duration": 0.01199,
     "end_time": "2026-05-07T05:49:17.723005+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.711015+00:00",
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
   "id": "9be29fc7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.729991Z",
     "iopub.status.busy": "2026-05-07T05:49:17.729571Z",
     "iopub.status.idle": "2026-05-07T05:49:17.735266Z",
     "shell.execute_reply": "2026-05-07T05:49:17.734559Z"
    },
    "papermill": {
     "duration": 0.011679,
     "end_time": "2026-05-07T05:49:17.737519+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.725840+00:00",
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
   "id": "ec9f3644",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.745007Z",
     "iopub.status.busy": "2026-05-07T05:49:17.744721Z",
     "iopub.status.idle": "2026-05-07T05:49:17.750812Z",
     "shell.execute_reply": "2026-05-07T05:49:17.750068Z"
    },
    "papermill": {
     "duration": 0.012123,
     "end_time": "2026-05-07T05:49:17.752923+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.740800+00:00",
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
   "id": "d34791a0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.760138Z",
     "iopub.status.busy": "2026-05-07T05:49:17.759867Z",
     "iopub.status.idle": "2026-05-07T05:49:17.766589Z",
     "shell.execute_reply": "2026-05-07T05:49:17.765372Z"
    },
    "papermill": {
     "duration": 0.012575,
     "end_time": "2026-05-07T05:49:17.768775+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.756200+00:00",
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
   "id": "c9f6c876",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.776406Z",
     "iopub.status.busy": "2026-05-07T05:49:17.776096Z",
     "iopub.status.idle": "2026-05-07T05:49:17.785010Z",
     "shell.execute_reply": "2026-05-07T05:49:17.783622Z"
    },
    "papermill": {
     "duration": 0.014616,
     "end_time": "2026-05-07T05:49:17.786592+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.771976+00:00",
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
   "id": "bc6000c5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.794042Z",
     "iopub.status.busy": "2026-05-07T05:49:17.793727Z",
     "iopub.status.idle": "2026-05-07T05:49:17.799695Z",
     "shell.execute_reply": "2026-05-07T05:49:17.798817Z"
    },
    "papermill": {
     "duration": 0.011845,
     "end_time": "2026-05-07T05:49:17.801568+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.789723+00:00",
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
   "id": "cbc39a56",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.810982Z",
     "iopub.status.busy": "2026-05-07T05:49:17.809824Z",
     "iopub.status.idle": "2026-05-07T05:49:17.817465Z",
     "shell.execute_reply": "2026-05-07T05:49:17.816551Z"
    },
    "papermill": {
     "duration": 0.014698,
     "end_time": "2026-05-07T05:49:17.819309+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.804611+00:00",
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
   "execution_count": 13,
   "id": "65724e31",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.826607Z",
     "iopub.status.busy": "2026-05-07T05:49:17.826314Z",
     "iopub.status.idle": "2026-05-07T05:49:17.831491Z",
     "shell.execute_reply": "2026-05-07T05:49:17.830621Z"
    },
    "papermill": {
     "duration": 0.010736,
     "end_time": "2026-05-07T05:49:17.833132+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.822396+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 6]]\n"
     ]
    }
   ],
   "source": [
    "print(arr[1:2,0:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6df12493",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.840152Z",
     "iopub.status.busy": "2026-05-07T05:49:17.839909Z",
     "iopub.status.idle": "2026-05-07T05:49:17.845168Z",
     "shell.execute_reply": "2026-05-07T05:49:17.843749Z"
    },
    "papermill": {
     "duration": 0.011014,
     "end_time": "2026-05-07T05:49:17.847150+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.836136+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(arr[0][0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "814fadf7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2026-05-07T05:49:17.855762Z",
     "iopub.status.busy": "2026-05-07T05:49:17.855301Z",
     "iopub.status.idle": "2026-05-07T05:49:17.861237Z",
     "shell.execute_reply": "2026-05-07T05:49:17.860122Z"
    },
    "papermill": {
     "duration": 0.012999,
     "end_time": "2026-05-07T05:49:17.863494+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.850495+00:00",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 7  8]\n",
      " [11 12]]\n"
     ]
    }
   ],
   "source": [
    "# print(arr[1:])\n",
    "print(arr[1:,2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c8fa0bf",
   "metadata": {
    "papermill": {
     "duration": 0.003098,
     "end_time": "2026-05-07T05:49:17.870238+00:00",
     "exception": false,
     "start_time": "2026-05-07T05:49:17.867140+00:00",
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
   "duration": 8.630197,
   "end_time": "2026-05-07T05:49:18.294546+00:00",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2026-05-07T05:49:09.664349+00:00",
   "version": "2.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
