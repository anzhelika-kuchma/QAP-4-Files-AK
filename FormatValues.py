def fDollar2(dollarValue):
    # Function will accept a value and format it to $#,###.##.

    dollarValueStr = "${:,.2f}".format(dollarValue)

    return dollarValueStr


def fDollar0(dollarValue):
    # Function will accept a value and format it to $#,###.##.

    dollarValueStr = "${:,.0f}".format(dollarValue)

    return dollarValueStr


def fComma2(value):
    # Function will accept a value and format it to #,###.##.

    valueStr = "{:,.2f}".format(value)

    return valueStr


def fComma0(value):
    # Function will accept a value and format it to #,###.

    valueStr = "{:,.0f}".format(value)

    return valueStr


def fNumber0(value):
    # Function will accept a value and format it to ####

    valueStr = "{:.0f}".format(value)

    return valueStr


def fNumber1(value):
    # Function will accept a value and format it to ####.#.

    valueStr = "{:.1f}".format(value)

    return valueStr


def fNumber2(value):
    # Function will accept a value and format it to ####.##.

    valueStr = "{:.2f}".format(value)

    return valueStr


def fDateS(dateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    dateValueStr = dateValue.strftime("%Y-%m-%d")

    return dateValueStr


def fDateM(dateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    dateValueStr = dateValue.strftime("%d-%b-%y")

    return dateValueStr


def fDateL(dateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    dateValueStr = dateValue.strftime("%A, %B %d, %Y")

    return dateValueStr

def fDateAndTime(dateValue):
    # Function will accept a value and format it to "yyyy-mm-dd, h-m-s" .

    dateValueStr = dateValue.strftime("%Y-%m-%d, %H:%M:%S")

    return dateValueStr


def fPhoneNum(value):
    # Function will accept a value and format it to (###) ###-####.

    valueStr = f"({value[0:3]}) {value[3:6]}-{value[6:]}"

    return valueStr


def fYOrN(value):
    # Function will accept a value and format it to Yes or No.

    valueStr = ""

    if value == "Y":
        valueStr = "Yes"
    elif value == "N":
        valueStr = "No"

    return valueStr