# Program description: This software helps One Stop Insurance Company to enter and calculate new
#                      insurance policy information for its customers.
# Written by:          Anzhelika Kuchma
# Date written:        July 21 - July 23 - 2023

# Required libraries:
import datetime
CURR_DATE = datetime.datetime.now()
import FormatValues as FV
import time
from tqdm import trange
from colorama import Fore

# Opening the defaults file and reading the values into variables
f = open('OSICDef.dat', 'r')
NEXT_POL_NUM = int(f.readline())
COST_BASIC_PREM = float(f.readline())
ADD_CARS_DISC = float(f.readline())
COST_EXTRA_LIABIL_COV = float(f.readline())
COST_GLASS_COV = float(f.readline())
COST_LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
MONTH_PAY_PROCESS_FEE = float(f.readline())
f.close()


# Required functions:

# Main program
while True:

    # Inputs:
    customerFirstName = input('Enter the customer first name (END to quite): ').title()
    if customerFirstName == 'End':
        break

    customerLastName = input('Enter the customer last name: ').title()
    streetAdd = input('Enter a street address: ')
    city = input('Enter a city: ').title()

    provLst = ['NL', 'NS', 'PE', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NV']
    while True:
        province = input('Enter the province (LL): ').upper()
        if province == '':
            print('Error - Province cannot be blank. Please re-enter.')
        elif len(province) != 2:
            print('Error - Province must be 2 letters only. Please re-enter.')
        elif province not in provLst:
            print('Error - not a valid province. Please re-enter.')
        else:
            break

    zip = input('Enter a postal code (XXXXXX): ').upper()
    phoneNum = input('Enter a phone number (##########): ')

    carsNum = int(input('Enter a number of cars being insured: '))
    extraLiabil = input('Is extra liability up to $1,000,000 required? (Enter Y for Yes or N for No): ').upper()
    glassCov = input('Is glass coverage required? (Enter Y for Yes or N for No): ').upper()
    loanerCar = input('Is loaner car required? (Enter Y for Yes or N for No): ').upper()

    payOptLst = ['Full', 'Monthly']
    while True:
        payOpt = input('Will the customer pay in full or monthly? (Enter Full or Monthly): ').title()
        if payOpt == '':
            print('Error - Preferred payment option cannot be blank. Please re-enter.')
        elif payOpt not in payOptLst:
            print('Error - not a valid payment option. Please re-enter.')
        else:
            break

    # Calculations:
    insurPrem = COST_BASIC_PREM
    if carsNum > 1:
        insurPrem += COST_BASIC_PREM * ADD_CARS_DISC * (carsNum - 1)

    if extraLiabil == 'Y':
        extraLiabilCost = COST_EXTRA_LIABIL_COV * carsNum
    else:
        extraLiabilCost = 0

    if glassCov == 'Y':
        glassCovCost = COST_GLASS_COV * carsNum
    else:
        glassCovCost = 0

    if loanerCar == 'Y':
        loanerCarCovCost = COST_LOANER_CAR_COV * carsNum
    else:
        loanerCarCovCost = 0

    totalExtraCost = extraLiabilCost + glassCovCost + loanerCarCovCost
    totalInsurPrem = insurPrem + totalExtraCost
    hst = totalInsurPrem * HST_RATE
    totalCost = totalInsurPrem + hst

    if payOpt == 'Monthly':
        monthPay = (totalCost + MONTH_PAY_PROCESS_FEE) / 8

    invDate = CURR_DATE

    if CURR_DATE.month == 12:
        nextPayDate = datetime.datetime(CURR_DATE.year + 1, 1, 1)
    else:
        nextPayDate = datetime.datetime(CURR_DATE.year, CURR_DATE.month + 1, 1)

    # Outputs:
    print()
    print('       ONE STOP INSURANCE COMPANY')
    print('           144 MILITARY ROAD')
    print('         ST. JOHN\'S NL, A1A 2E6')
    print('             (709) 771-0923')
    print('*'*40)
    print(f'Customer Name:   {customerFirstName:<11s} {customerLastName:<11s}')
    print(f'Address:         {streetAdd:<21s}')
    print(f'                 {city:<11s} {province:<2s}, {zip:<6s}')
    print(f'Phone Number:    {FV.fPhoneNum(phoneNum):<13s}')
    print('*' * 40)
    print()
    print(f'   Number of Cars:  {carsNum:>4d}')
    print()
    print(f'   Extra Liability:    {FV.fYOrN(extraLiabil)}')
    print(f'   Glass Coverage:     {FV.fYOrN(glassCov)}')
    print(f'   Loaner Car:         {FV.fYOrN(loanerCar)}')
    print()
    print(f'   Payment Option:     {payOpt:<7s}')
    print()
    print('*' * 40)
    print()
    print(f'Insurance Premiums Cost:      {FV.fDollar2(insurPrem):>10s}')
    print()
    print(f'Extra Liability Cost:          {FV.fDollar2(extraLiabilCost):>9s}')
    print(f'Glass Cov. Cost:               {FV.fDollar2(glassCovCost):>9s}')
    print(f'Loaner Car Cov. Cost:          {FV.fDollar2(loanerCarCovCost):>9s}')
    print()
    print(f'Total Extra Cost:              {FV.fDollar2(totalExtraCost):>9s}')
    print(f'Total Insurance Premiums:      {FV.fDollar2(totalInsurPrem):>9s}')
    print(f'HST:                           {FV.fDollar2(hst):>9s}')
    print()
    print(f'Total Cost:                   {FV.fDollar2(totalCost):>10s}')

    if payOpt == 'Monthly':
        print(f'Monthly Payment:              {FV.fDollar2(monthPay):>10s}')
        print()
        print(f"Next Payment Date: {nextPayDate.date()}")

    print()
    print('*' * 40)
    print(f'{FV.fDateAndTime(CURR_DATE)}          {NEXT_POL_NUM:>10d}')

    print()
    print()
    print('Policy information is processing...')
    print()

    # Processing bar
    color = Fore.RED

    for i in trange(int(7e7),
                    bar_format='{l_bar}%s{bar}%s{r_bar}' % (color, Fore.RESET)):
        pass

    # Write the values to a file for future reference.
    f = open('Policies.dat', 'a')
    f.write(f'{NEXT_POL_NUM}, ')
    f.write(f'{CURR_DATE.date()}, ')
    f.write(f'{customerFirstName}, ')
    f.write(f'{customerLastName}, ')
    f.write(f'{streetAdd}, ')
    f.write(f'{city}, ')
    f.write(f'{province}, ')
    f.write(f'{phoneNum}, ')
    f.write(f'{str(carsNum)}, ')
    f.write(f'{extraLiabil}, ')
    f.write(f'{glassCov}, ')
    f.write(f'{loanerCar}, ')
    f.write(f'{payOpt}, ')
    f.write(f'{str(totalInsurPrem)}\n')
    f.close()

    print()
    print('Policy information is processed and saved.')
    time.sleep(1)
    print()

    NEXT_POL_NUM += 1

# Housekeeping:
# Writing the current values back to the default file:
f = open('OSICDef.dat', 'w')
f.write(f'{NEXT_POL_NUM}\n')
f.write(f'{COST_BASIC_PREM}\n')
f.write(f'{ADD_CARS_DISC}\n')
f.write(f'{COST_EXTRA_LIABIL_COV}\n')
f.write(f'{COST_GLASS_COV}\n')
f.write(f'{COST_LOANER_CAR_COV}\n')
f.write(f'{HST_RATE}\n')
f.write(f'{MONTH_PAY_PROCESS_FEE}\n')
f.close()

