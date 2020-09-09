{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from car import ElectricCar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017 Telsa Model\n",
      "This car has a 70-kwh battery\n",
      "This car can go approximately 240 miles on a full charge\n"
     ]
    }
   ],
   "source": [
    "my_telsa = ElectricCar('telsa', 'model', 2017)\n",
    "print(my_telsa.get_descriptive())\n",
    "\n",
    "my_telsa.battery.describe_battery()\n",
    "my_telsa.battery.get_range()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "from car import Car, ElectricCar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2018 Mercedes Benz\n",
      "2019 Telsa Modula\n"
     ]
    }
   ],
   "source": [
    "my_bettle = Car('mercedes', 'benz', 2018)\n",
    "print(my_bettle.get_descriptive())\n",
    "\n",
    "my_telsa = ElectricCar('telsa', 'modula', 2019)\n",
    "print(my_telsa.get_descriptive())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing entire module\n",
    "\n",
    "import car"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2018 Mercedes Benz\n",
      "2019 Telsa Modula\n"
     ]
    }
   ],
   "source": [
    "my_bettle = car.Car('mercedes', 'benz', 2018)\n",
    "print(my_bettle.get_descriptive())\n",
    "\n",
    "my_telsa = car.ElectricCar('telsa', 'modula', 2019)\n",
    "print(my_telsa.get_descriptive())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "zip?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 12, 123,  45,  34,  23,  43,  23,  43])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.array([12,123,45,34,23,43,23,43])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
