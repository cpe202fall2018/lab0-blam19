def weight_on_planets():
   earthweight = int(input('What do you weigh on earth? '))
   marsweight = earthweight * .38
   jupiterweight = earthweight * 2.34
   print('\nOn Mars you would weigh {0:.2f} pounds.\nOn Jupiter you would weigh {1:.2f} pounds.'.format(marsweight,
                                                                                                        jupiterweight))


if __name__ == '__main__':
   weight_on_planets()