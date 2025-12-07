
# Financial Markets
# Which financial market deals with short-term funds (maturity up to one year)?
# A. Capital Market
# B. Money Market
# C. Derivative Market
# D. Forex Market
# Answer: B
# Treasury bills are instruments of short-term borrowing issued by the government and are also called:
# A. Trade bills
# B. Call money
# C. Zero-coupon bonds
# D. Commercial papers
# Answer: C
# The process of holding shares in electronic form is known as:
# A. Demutualization
# B. Dematerialization
# C. Speculation
# D. None of the above
# Answer: B
# The basic function of financial markets is to channel funds from lenders-savers to:
# A. The government
# B. Foreign investors
# C. Borrowers-spenders
# D. Other financial institutions
# Answer: C


print('Welcome to Financial Management Quiz!')

playing = input('Did you want to play? ')

if playing.lower() == 'yes' or playing.upper() == 'yes':
    print('Let\'s play')
else:
    print('let\'s catch up later')
    quit()

score = 0
print('Score:', score)
print('''Instrution
      Score increase by 10 points for each question answered correctly.
      input option from a - d for your respective answer.
      let\'s go''')

answer = input('''Question 1: What is the primary objective of financial management?
    A: Maximization of profit
    B. Maximization of shareholder's wealth
    C. Ensuring financial discipline in the firm
    D. All of these 
    Answer: ''')
if answer.lower() == 'b' or answer.upper() == 'b':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 2: Cost of capital is the:
    A. Rate of return expected by investors
    B. Cost incurred for a specific project
    C. Dividend paid to shareholders
    D. Interest paid on bank loans 
    Answer: ''')
if answer.lower() == 'a' or answer.upper() == 'a':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 3: The concept of time value of money implies that:
    A. Cash flows occurring earlier are less valuable than those occurring later.
    B. Cash flows occurring earlier are more valuable than those occurring later.
    C. The future value of cash flows is always lower than the present value.
    D. Time has no impact on the value of money. 
    Answer: ''')
if answer.lower() == 'b' or answer.upper() == 'b':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 4: Which institution is often referred to as the "lender of last resort"?
    A. Commercial bank
    B. Agricultural bank
    C. Industrial bank
    D. Central bank 
    Answer: ''')
if answer.lower() == 'd' or answer.upper() == 'D':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 5: A stale cheque is a cheque that is older than:
    A. 3 months
    B. 6 months
    C. 12 months
    D. Not yet due
    Answer: ''')
if answer.lower() == 'b' or answer.upper() == 'b':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 6: Which of the following is the main source of income for a commercial bank?
    A Interest Income
    B Investment Income
    C Commission
    D Exchange & Brokerage
    Answer: ''')
if answer.lower() == 'a' or answer.upper() == 'a':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 7: Which financial market deals with short-term funds (maturity up to one year)?
    A. Capital Market
    B. Money Market
    C. Derivative Market
    D. Forex Market
    Answer: ''')
if answer.lower() == 'b' or answer.upper() == 'b':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 8: Treasury bills are instruments of short-term borrowing issued by the government and are also called:
    A. Trade bills
    B. Call money
    C. Zero-coupon bonds
    D. Commercial papers
    Answer:  ''')
if answer.lower() == 'c' or answer.upper() == 'c':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 9: The process of holding shares in electronic form is known as:
    A. Demutualization
    B. Dematerialization
    C. Speculation
    D. None of the above
    Answer:  ''')
if answer.lower() == 'b' or answer.upper() == 'b':
    print('Correct!')
    score += 10
else:
    print('Incorrect')

answer = input('''Question 9: The basic function of financial markets is to channel funds from lenders-savers to:
    A. The government
    B. Foreign investors
    C. Borrowers-spenders
    D. Other financial institutions
    Answer:  ''')
if answer.lower() == 'c' or answer.upper() == 'c':
    print('Correct!')
    score += 10
else:
    print('Incorrect')


print(f'You got {int(score/10)} score correctly')
print(f'You got {score}%')