def tax(filing_status, income):
    if filing_status == 'single':
        if(income >= 0) and (income < 9275):
            tax = (.1*income)
            
        elif(income > 9275) and (income <= 37560):
            tax = (.1*9275 + .15*(income-9275))
            
        elif(income > 37560) and (income <= 91150):
            tax = (.1*9275 + (.15*(37650-9275)) + (.25*(income-37650)))
            
        elif(income > 91150) and (income <= 190150):
            tax = (.1*9275 + (.15*(37650-9275)) + (.25*(91150-37650)) + (.28*(income-91150)))
                   
        elif(income > 190150) and (income <= 413350):
            tax = (.1*9275) + (.15*(37650-9275)) + (.25*(91150-37650)) + (.28*(190150-91150)) + (.33*(income-190150))
                   
        elif(income > 413350) and (income <= 415050):
            tax = (.1*9275) + (.15*(37650-9275)) + (.25*(91150-37650)) + (.28*(190150-91150)) + (.33*(413350-190150)) + (.35*(income-413350))
                   
        elif(income > 415050):
            tax = (.1*9275 + (.15*(37650-9275)) + (.25*(91150-37650)) + (.28*(190150-91150)) + (.33*(413350-190150)) + (.35*(415050-413350)) + (.396*(income-415050)))
        
        else:
            pass          
            
    elif filing_status == 'married, filing jointly or widowed':
        if(income >= 0) and (income < 18550):
            tax = (.1*income)
            
        elif(income > 18550) and (income <= 75300):
            tax = (.1*18550) + (.15*(income-18550))
        
        elif(income > 75300) and (income <= 151900):
            tax = (.1*18550) + (.15*(75300-18550)) + (.25*(income-75300))
            
        elif(income > 151900) and (income <= 231450):
            tax = (.1*18550) + (.15*(75300-18550)) + (.25*(151900-75300)) + (.28*(income-151900))
            
        elif(income > 231450) and (income <= 413350):
            tax = (.1*18550) + (.15*(75300-18550)) + (.25*(151900-75300)) + (.28*(231450-151900)) + (.33*(income-231450))
            
        elif(income > 413350) and (income <= 466950):
            tax = (.1*18550) + (.15*(75300-18550)) + (.25*(151900-75300)) + (.28*(231450-151900)) + (.33*(413350-231450)) + (.35*(income-413350))
              
        elif(income > 466950):
            tax = (.1*18550) + (.15*(75300-18550)) + (.25*(151900-75300)) + (.28*(231450-151900)) + (.33*(413350-231450)) + (.35*(466950-413350)) + (.396*(income-466950))
            
        else:
            pass    
            
    elif filing_status == 'married, filing separately':
        if(income >= 0) and (income < 9,275):
            tax = (.1*income)
            
        elif(income > 9275) and (income <= 37650):
            tax = (.1*9275 + .15*(income-9275))
            
        elif(income > 37650) and (income <= 75950):
            tax = (.1*9275 + .15*(37650-9275) + .25*(income-37650))
            
        elif(income > 75950) and (income <= 115725):
            tax = (.1*9275 + .15*(37650-9275) + .25*(75950-37650) + .28*(income-75950))
            
        elif(income > 115725) and (income <= 206675):
            tax = (.1*9275 + .15*(37650-9275) + .25*(75950-37650) + .28*(115725-75950) + .33*(income-115725)) 
            
        elif(income > 206675) and (income <= 233475):
            tax = (.1*9275 + .15*(37650-9275) + .25*(75950-37650) + .28*(115725-75950) + .33*(206675-115725) + .35*(income-206675))     
            
        elif(income > 233475):
            tax = (.1*9275 + .15*(37650-9275) + .25*(75950-37650) + .28*(115725-75950) + .33*(206675-115725) + .35*(233475-206675) + .396*(income-233475))
        
        else:
            pass   
                   
    elif filing_status == 'head of household':
        if(income >= 0) and (income < 13250):
            tax = (.1*income)
        
        elif(income > 13250) and (income <= 50400):
            tax = (.1*13250 + .15*(income-13250))
            
        elif(income > 50400) and (income <= 130150):
            tax = (.1*13250 + .15*(50400-13250) + .25*(income-50400))
            
        elif(income > 130150) and (income <= 210800):
            tax = (.1*13250 + .15*(50400-13250) + .25*(130150-50400) + .28*(income-130150))
            
        elif(income > 210800) and (income <= 413350):
            tax = (.1*13250 + .15*(50400-13250) + .25*(130150-50400) + .28*(210800-130150) + .33*(income-210800))
            
        elif(income > 413350) and (income <= 441000):
            tax = (.1*13250 + .15*(50400-13250) + .25*(130150-50400) + .28*(210800-130150) + .33*(413350-210800) + .35*(income-413350))   
            
        elif(income > 441000):
            tax = (.1*13250 + .15*(50400-13250) + .25*(130150-50400) + .28*(210800-130150) + .33*(413350-210800) + .35*(441000-413350) + .396*(income-441000))
        
filing_status = input('Your Filing Status:')
income = int(input('How much you made last year:'))
 
def percent_of_income(tax, income):
    return((tax/income)*100)

def is_valid(filing_status, income):
    if(income < 0):
        return False
    elif filing_status == 'single' or 'married, filing jointly or widowed' or 'married, filing separately' or 'head of household':
        return True
    else:
        return False
    
def main(filing_status, income):
    if is_valid(filing_status, income):
        tax_value = tax(filing_status, income)
        percent_value = percent_of_income(tax_value, income)
        print('Tax: $' + str(tax_value))
        print('Tax as % of income:' + str(percent_value) + "%")
    else:
        print("Filing status must be 'single', 'married, filing jointly or widowed', 'married, filing separately', or 'head of household'.")
        print("Income must be greater than or equal to zero.")