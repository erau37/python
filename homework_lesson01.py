# -*- coding: utf-8 -*-
# initializing empty envelops

necessity_envelop = 0  # NEC
freedom_envelop = 0  # FFA
education_envelop = 0  # EDU
long_term_envelop = 0  # LTSS
play_envelop = 0  # PLAY
give_envelop = 0  # GIVE

# initializing percent rate
nec_rate = 0.55
ffa_rate = 0.1
edu_rate = 0.1
ltss_rate = 0.1
play_rate = 0.1
give_rate = 0.05

# initializing expected income, expected necessity and other amounts
expectedIncome = 1000

# invitation, greetings etc.
print("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")

# initializing handler for standard input
summa = 0

while summa < expectedIncome:
    line = int(input())
    summa += line

    necessity_envelop += line * nec_rate
    freedom_envelop += line * ffa_rate
    education_envelop += line * edu_rate
    long_term_envelop += line * ltss_rate
    play_envelop += line * play_rate
    give_envelop += line * give_rate

    print("\n Enter the amount please:\n")

# final output
print(f"At the end, we have:\n"
      f"    Necessity Envelop has:                       {int(necessity_envelop)}\n"
      f"    Financial Freedom Envelop has:               {int(freedom_envelop)}\n"
      f"    Education Envelop has:                       {int(education_envelop)}\n"
      f"    Long Term Saving for Spending Envelop has:   {int(long_term_envelop)}\n"
      f"    Play Envelop has:                            {int(play_envelop)}\n"
      f"    Give Envelop has:                            {int(give_envelop)}\n"
      "    _______________________________________________________________\n"
      "    Thanks for using our software :)")

# fixed the issue with Education Envelop from homework task (has: was missing)
# removed unnecessary () in line 31
# as an improvement changed variables for better readability to format - necessity_envelope
