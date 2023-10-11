#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 11th, 2023
# This program asks the user for the radius of
# a sphere in cm. It then calculates and displays
# the surface area and volume of the sphere.
import constants


def main():
    # user inputs the radius of the sphere into the terminal
    radius = float(input("Enter the radius of the sphere (cm): "))

    # terminal calculates the area and volume of the sphere
    surface_area = 4 * constants. PI * radius ** 2
    volume = 4 / 3 * constants. PI * radius ** 3
    # terminal displays the surface area and volume of the sphere
    print("")
    print("The Surface Area is = {} cm^2".format(surface_area))
    print("The Volume is = {} cm^3".format(volume))


if __name__ == "__main__":
    main()
